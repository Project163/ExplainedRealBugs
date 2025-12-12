import os
import json
import time
import requests
import math
from concurrent.futures import ThreadPoolExecutor


# 1. Configuration and Constants
# API Key
API_KEY = os.getenv("SILICONCLOUD_API_KEY")
if not API_KEY:
    raise ValueError("[Error]: Please set the 'SILICONCLOUD_API_KEY' environment variable")

API_URL = "https://api.siliconflow.cn/v1/embeddings"
MODEL_NAME = "BAAI/bge-m3"

WORK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bug-classification'))

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(__file__), 'cache'), exist_ok=True)

INPUT_FILE = os.path.abspath(os.path.join(WORK_DIR, 'parsed_data.jsonl'))
OUTPUT_FILE = os.path.abspath(os.path.join(WORK_DIR, 'classified_data_embedding.jsonl'))
CACHE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cache', 'embedding_cache.json'))

MAX_WORKERS = 10
REQUEST_DELAY = 0.05

# Text truncation length
# Embedding models have a maximum token limit (BGE typically 8k tokens).
# If the text is too long (e.g., contains long stack traces), it can cause a 413 error.
# 20000 characters roughly correspond to 5000-8000 tokens, which is a safe value.
MAX_CHARS = 20000 


# 2. Fine-grained Label Definitions
LABEL_DESCRIPTIONS = {
    # --- Crash & Stability ---
    "Crash/UnhandledException": "The application crashed due to an unhandled exception or error.",
    "Crash/NullPointer": "The application crashed specifically due to a null pointer or nil reference.",
    "Crash/Memory": "The application crashed due to out of memory or memory leaks.",
    "Stability/Freeze": "The application becomes unresponsive, freezes, or hangs indefinitely.",

    # --- UI/UX ---
    "UI/Layout": "Elements are misaligned, overlapping, or have incorrect spacing/margin.",
    "UI/Visual": "Visual glitches, wrong colors, blurry images, or broken icons.",
    "UI/Responsive": "The interface breaks or looks bad on different screen sizes or mobile devices.",
    "UX/Navigation": "User flow is confusing, navigation links are broken, or buttons are hard to find.",
    "Accessibility": "Issues with screen readers, keyboard navigation, or color contrast compliance.",

    # --- Logic & Functional ---
    "Logic/Calculation": "Mathematical errors, incorrect totals, or wrong data processing logic.",
    "Logic/Workflow": "The business process flow is stuck or transitions to an incorrect state.",
    "Data/Corruption": "Data is saved incorrectly, missing, or corrupted in the database.",
    "Data/Format": "Dates, numbers, or currencies are displayed in the wrong format.",

    # --- Network & API ---
    "Network/Timeout": "The request timed out or the connection was refused.",
    "Network/APIError": "The API returned a 500 error, 404 not found, or invalid JSON response.",
    "Connectivity": "Issues related to internet connection, offline mode, or socket disconnections.",

    # --- Environment & Build ---
    "Build/Dependency": "Errors related to missing libraries, gems, npm packages, or version conflicts.",
    "Env/Compatibility": "The issue only occurs on a specific OS (Windows/Linux) or Browser (IE/Firefox).",
    "Dev/Test": "Issues related to failing unit tests, CI pipelines, or test configuration.",

    # --- Text & Documentation ---
    "Text/Typo": "Spelling mistakes, grammatical errors, or wrong labels in the UI.",
    "Docs/Missing": "Documentation is outdated, missing, or misleading.",
    
    # --- Security ---
    "Security/Auth": "Issues with login, logout, password reset, or permissions.",
    "Security/Vulnerability": "Potential security risks like XSS, SQL Injection, or sensitive data exposure.",

    # --- Other ---
    "Other": "A generic bug that does not fit into any other specific category."
}


# 3. Utility Functions
def get_embedding(text):
    """
    Call API to get the embedding vector for the given text.
    """
    if not text:
        return None

    # If the text is too long, truncate it to the first MAX_CHARS characters
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    # Preprocessing: remove newline characters
    cleaned_text = text.replace("\n", " ").strip()
    
    payload = {
        "model": MODEL_NAME,
        "input": cleaned_text,
        "encoding_format": "float"
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 413:
            print(f"[Error]: 413, Text is still too long. Current length: {len(cleaned_text)}")
            return None

        response.raise_for_status()
        data = response.json()
        return data['data'][0]['embedding']
    except Exception as e:
        print(f"Embedding API Error: {e}")
        return None

def cosine_similarity(v1, v2):
    """
    Calculate the cosine similarity between two vectors.
    """
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude1 = math.sqrt(sum(a * a for a in v1))
    magnitude2 = math.sqrt(sum(b * b for b in v2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

def load_cache():
    """Load embedding cache from local file"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[Warning]: Failed to load cache file: {e}")
    return {}

def save_cache(cache_data):
    """Save cache to local file"""
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)
        print(f"Updated label embedding cache: {CACHE_FILE}")
    except Exception as e:
        print(f"[Error] Failed to save cache: {e}")

# 4. Main Logic
def get_label_embeddings_with_cache():
    """
    Get embeddings for all labels.
    Prefer using cache; if description changes or no cache, call API to compute.
    """
    print("Preparing label embeddings...")
    
    # 1. Load existing cache
    cache = load_cache()
    embeddings = {}
    cache_updated = False
    
    # 2. Iterate over the labels defined in the current code
    print(f"Checking {len(LABEL_DESCRIPTIONS)} label definitions...")
    
    for label, description in LABEL_DESCRIPTIONS.items():
        # Check if the label exists in cache and the description matches
        if label in cache and cache[label].get('description') == description:
            # Cache hit
            embeddings[label] = cache[label]['vector']
        else:
            # Cache miss (new label or description changed), need to recompute
            status = "Description updated" if label in cache else "New label"
            print(f"  - [{status}] Computing vector: {label}")
            
            vec = get_embedding(description)
            if vec:
                embeddings[label] = vec
                # Update cache structure
                cache[label] = {
                    'description': description,
                    'vector': vec
                }
                cache_updated = True
                time.sleep(0.1)
            else:
                print(f"  - [Error] Failed to generate vector: {label}")

    # 3. Clean up deleted labels (if a label is removed from the code, it should also be removed from the cache)
    current_keys = set(LABEL_DESCRIPTIONS.keys())
    cached_keys = set(cache.keys())
    deprecated_keys = cached_keys - current_keys
    
    if deprecated_keys:
        print(f"  - Cleaning up {len(deprecated_keys)} deprecated cache labels...")
        for k in deprecated_keys:
            del cache[k]
        cache_updated = True

    # 4. If there are updates, write back to disk
    if cache_updated:
        save_cache(cache)
    else:
        print("All labels hit the cache, no need to call the API.")
        
    return embeddings

def classify_bug_vector(bug_vec, label_embeddings):
    best_label = "Other"
    best_score = -1.0

    for label, label_vec in label_embeddings.items():
        score = cosine_similarity(bug_vec, label_vec)
        if score > best_score:
            best_score = score
            best_label = label
            
    return best_label, best_score

def process_line(line_data, label_embeddings):
    """
    Process a single line of data
    """
    bug_text = line_data.get("llm_input_text", "")
    if not bug_text:
        return None

    bug_vec = get_embedding(bug_text)
    if not bug_vec:
        return "Error"

    predicted_label, score = classify_bug_vector(bug_vec, label_embeddings)
    return predicted_label

def main():
    label_embeddings = get_label_embeddings_with_cache()

    if not label_embeddings:
        print("[Error]: Unable to generate label embeddings.")
        return

    print("-" * 50)
    print(f"Label embeddings ready, starting to process {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"[Error]: File not found {INPUT_FILE}")
        return

    print(f"There are {len(lines)} lines of data to process.")

    # Create a list to store (original data, Future object)
    # This way can iterate in the original order when writing results
    tasks = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 1. Submit all tasks
        for i, line in enumerate(lines):
            try:
                data = json.loads(line)
                future = executor.submit(process_line, data, label_embeddings)
                tasks.append((data, future))
            except json.JSONDecodeError:
                print(f"Line {i+1} JSON error")
                # If JSON parsing fails, we add None to the task list to keep index alignment (or ignore directly)
                # For simplicity, ignore the line and do not add to tasks

        print("All tasks submitted, waiting for results and writing in order...")

        # 2. Get results in order and write
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            processed_count = 0
            
            for original_data, future in tasks:
                # future.result() will block until the specific task is completed
                # This ensures it process results in the order of the tasks list
                predicted_label = future.result()
                
                if predicted_label:
                    new_data = {
                        "project_id": original_data.get("project_id"),
                        "bug_id": original_data.get("bug_id"),
                        "source_type": original_data.get("source_type"),
                        "label": predicted_label,
                        "llm_input_text": original_data.get("llm_input_text")
                    }
                    outfile.write(json.dumps(new_data, ensure_ascii=False) + '\n')
                
                processed_count += 1
                if processed_count % 10 == 0:
                    print(f"Processed: {processed_count}/{len(tasks)}")
                
                # Simple rate control
                time.sleep(REQUEST_DELAY)

    print(f"Processing complete. Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()