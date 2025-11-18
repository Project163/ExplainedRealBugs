import os
import json
import argparse
from bs4 import BeautifulSoup
import re

# Cleaning helper functions

def clean_text(text):
    """A simple text cleaning function to remove code blocks, HTML tags, and normalize whitespace."""
    if not text:
        return ""
    # Remove code blocks
    text = re.sub(r'```.*?(```|$)', '', text, flags=re.DOTALL)
    text = re.sub(r'{code:.*?}.*?({code}|$)', '', text, flags=re.DOTALL)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Parsing functions for jira
def parse_jira_xml(xml_content):
    try:
        soup = BeautifulSoup(xml_content, 'xml')
        
        # 1. Fetch title
        title_node = soup.find('summary')
        title = clean_text(title_node.get_text()) if title_node else "No Title Found"
        
        # 2. Fetch description
        desc_node = soup.find('description')
        description = clean_text(desc_node.get_text()) if desc_node else ""
        
        # 3. Fetch all comments
        comments = []
        for comment in soup.find_all('comment'):
            comment_body = comment.get_text()
            if comment_body.strip(): # Ensure we don't add empty comments
                comments.append(clean_text(comment_body))
            
        return format_for_llm(title, description, comments)
    except Exception as e:
        print(f"[Warning]: Failed to parse Jira XML: {e}")
        return None

def parse_github_json(report_json, timeline_json):
    try:
        # 1. Fetch Title
        title = clean_text(report_json.get('title')) #

        # 2. Fetch Description
        description = clean_text(report_json.get('body')) #
        
        comments = []
        if timeline_json:
            # 3. Iterate over Timeline and look for "commented" events
            for event in timeline_json:
                if event.get('event') == 'commented' and event.get('body'):
                    comment_body = event['body']
                    if comment_body.strip(): # Ensure we don't add empty comments
                        comments.append(clean_text(comment_body))
                    
        return format_for_llm(title, description, comments)
    except Exception as e:
        print(f"[Warning]: Failed to parse GitHub JSON: {e}")
        return None

def parse_google_json(report_json):
    try:
        # 1. Fetch Title
        title = clean_text(report_json.get('summary')) #
        
        all_comments = report_json.get('comments', [])
        description = ""
        discussion_comments = []

        if all_comments:
            # 2. Fetch Description(For Google, the first comment is usually the description)
            description = clean_text(all_comments[0].get('content'))

            # 3. Fetch Discussion Comments
            if len(all_comments) > 1:
                for comment in all_comments[1:]:
                    comment_body = comment.get('content')
                    if comment_body and comment_body.strip():
                        discussion_comments.append(clean_text(comment_body))
        
        return format_for_llm(title, description, discussion_comments)
    except Exception as e:
        print(f"[Warning]: Failed to parse Google JSON: {e}")
        return None


def format_for_llm(title, description, comments):
    """
    Format the extracted data into a single string suitable for LLM input.
    """
    llm_text = f"Title: {title if title else 'N/A'}\n\n"
    llm_text += f"Description:\n{description if description else 'N/A'}\n\n"
    
    if comments:
        llm_text += "Discussion:\n"
        llm_text += "\n---\n".join(comments)
        
    return llm_text


def main(bug_mining_root, output_file):
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    processed_count = 0
    
    with open(output_file, 'w', encoding='utf-8') as f_out:

        # 1. Iterate over project directories
        project_ids = sorted([d for d in os.listdir(bug_mining_root) if os.path.isdir(os.path.join(bug_mining_root, d))])
        
        for project_id in project_ids:
            project_dir = os.path.join(bug_mining_root, project_id)
                
            reports_dir = os.path.join(project_dir, 'reports')
            if not os.path.isdir(reports_dir):
                continue
                
            print(f"--- Processing Project: {project_id} ---")

            # 2. Iterate over reports directory
            files = os.listdir(reports_dir)
            report_files = {} # key: bug_id, value: { 'report': 'path', 'timeline': 'path' }

            for file in files:
                match = re.match(r'(\d+)(\.timeline)?\.(json|xml)', file)
                if not match:
                    continue
                
                bug_id = match.group(1)
                is_timeline = bool(match.group(2))
                ext = match.group(3)
                
                if bug_id not in report_files:
                    report_files[bug_id] = {'report': None, 'timeline': None, 'ext': None}
                
                if is_timeline:
                    report_files[bug_id]['timeline'] = os.path.join(reports_dir, file)
                else:
                    report_files[bug_id]['report'] = os.path.join(reports_dir, file)
                    report_files[bug_id]['ext'] = ext

            # 3. Process collected files
            for bug_id in sorted(report_files.keys(), key=int):
                paths = report_files[bug_id]
                
                if not paths['report']:
                    continue
                    
                llm_input_text = None
                source_type = "unknown"

                try:
                    if paths['ext'] == 'xml':
                        source_type = "jira"
                        with open(paths['report'], 'r', encoding='utf-8') as f:
                            llm_input_text = parse_jira_xml(f.read())
                            
                    elif paths['ext'] == 'json':
                        with open(paths['report'], 'r', encoding='utf-8') as f_rep:
                            report_data = json.load(f_rep)
                        
                        if paths['timeline']: 
                            source_type = "github"
                            timeline_data = None
                            with open(paths['timeline'], 'r', encoding='utf-8') as f_time:
                                timeline_data = json.load(f_time)
                            llm_input_text = parse_github_json(report_data, timeline_data)
                        else:
                            source_type = "google"
                            llm_input_text = parse_google_json(report_data)

                    # 4. Write to output if we have valid llm_input_text
                    if llm_input_text:
                        output_record = {
                            "project_id": project_id,
                            "bug_id": bug_id,
                            "source_type": source_type,
                            "llm_input_text": llm_input_text
                        }
                        f_out.write(json.dumps(output_record) + '\n')
                        processed_count += 1
                        
                except Exception as e:
                    print(f"[Error] Failed processing {project_id}/{bug_id} ({paths['report']}): {e}")

    print(f"\n=================================================")
    print(f"Parsing complete. Processed {processed_count} reports.")
    print(f"Output saved to: {output_file}")
    print(f"=================================================")


if __name__ == "__main__":
    
    DEFAULT_BUG_MINING_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bug-mining'))
    DEFAULT_OUTPUT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bug_classification', 'parsed_data.jsonl'))

    parser = argparse.ArgumentParser(description="Parse bug reports into a clean JSONL format for LLM classification.")
    parser.add_argument(
        '-i', '--input_dir', 
        default=DEFAULT_BUG_MINING_DIR,
        help=f"Path to the 'bug-mining' root directory. Default: {DEFAULT_BUG_MINING_DIR}"
    )
    parser.add_argument(
        '-o', '--output_file', 
        default=DEFAULT_OUTPUT_FILE,
        help=f"Path to the output .jsonl file. Default: {DEFAULT_OUTPUT_FILE}"
    )
    args = parser.parse_args()

    main(args.input_dir, args.output_file)