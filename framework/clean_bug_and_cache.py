#!/usr/bin/env python3
# framework/clean_project_data.py

import os
import sys
import shutil
import argparse
try:
    import config
except ImportError:
    print("Error: 无法导入 config.py。请确保此脚本与 config.py 在同一目录中。", file=sys.stderr)
    sys.exit(1)

def safe_remove_directory(path_to_remove):
    """
    安全地递归删除一个目录。
    如果目录不存在，则跳过。
    """
    if not os.path.exists(path_to_remove):
        print(f"  -> 跳过 (不存在): {path_to_remove}")
        return
    
    if not os.path.isdir(path_to_remove):
        print(f"  -> 跳过 (不是目录): {path_to_remove}")
        return

    try:
        shutil.rmtree(path_to_remove)
        print(f"  -> [成功] 已删除: {path_to_remove}")
    except OSError as e:
        print(f"  -> [失败] 无法删除 {path_to_remove}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(
        description="清理特定项目在 bug-mining, cache, 和 shared_issues 中的数据污染。",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # 允许用户指定输入文件，默认为 framework/delete.txt
    default_input = os.path.join(config.SCRIPT_DIR, 'delete.txt')
    parser.add_argument(
        '-i', '--input', 
        dest='input_file', 
        default=default_input,
        help=f"指定包含项目列表的输入文件 (默认: {default_input})"
    )

    args = parser.parse_args()
    input_file = args.input_file

    if not os.path.exists(input_file):
        print(f"Error: 输入文件未找到: {input_file}", file=sys.stderr)
        sys.exit(1)

    print(f"--- 开始使用 {input_file} 清理项目缓存 ---")

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            try:
                parts = line.split('\t')
                
                # 检查行是否格式正确 (至少需要5列)
                if len(parts) < 5:
                    print(f"\n[警告] 跳过格式错误的行 {line_num}: {line}", file=sys.stderr)
                    continue

                # 1. 获取 project_id (第一列)
                project_id = parts[0]
                
                # 2. 获取 issue_tracker_name (第四列)
                issue_tracker_name = parts[3]
                
                # 3. 获取 issue_tracker_project_id (第五列)
                issue_tracker_project_id = parts[4]

                print(f"\n正在清理项目: {project_id}")

                # --- 构造目标路径 ---

                # 目标 1: bug-mining/<project_id>
                #
                bug_mining_path = os.path.join(config.OUTPUT_DIR, project_id)

                # 目标 2: cache/<project_id>
                #
                cache_path = os.path.join(config.CACHE_DIR, project_id)

                # 目标 3: cache/shared_issues/<issue_cache_key>
                #
                issue_cache_key = f"{issue_tracker_name}_{issue_tracker_project_id}"
                shared_issues_path = os.path.join(config.SHARED_ISSUES_DIR, issue_cache_key)
                
                # --- 执行安全删除 ---
                safe_remove_directory(bug_mining_path)
                safe_remove_directory(cache_path)
                safe_remove_directory(shared_issues_path)

            except IndexError as e:
                print(f"\n[错误] 跳过格式错误的行 {line_num} (列索引超出范围): {e}", file=sys.stderr)
            except Exception as e:
                print(f"\n[严重错误] 处理行 {line_num} 时发生意外: {e}", file=sys.stderr)

    print("\n--- 清理完成 ---")

if __name__ == "__main__":
    main()