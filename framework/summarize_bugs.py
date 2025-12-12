#!/usr/bin/env python3
# framework/summarize_bugs_md.py
#
# 该脚本用于扫描 bug-mining/ 目录下的所有项目,
# 并生成一个汇总的 Markdown 文件。
# 
# 修改记录:
# - 将 Issue IDs 列替换为指向 active-bugs.csv 的链接，以防止表格行过高。

import os
import csv
import re
import sys

try:
    import config
except ImportError:
    print("Error: 无法导入 config.py。请确保此脚本与 config.py 在同一目录中。", file=sys.stderr)
    sys.exit(1)

def main():
    # --- 1. 定义路径 ---
    
    # SCRIPT_DIR 是 framework/ 目录
    SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # BUG_MINING_DIR 是 ../bug-mining/
    BUG_MINING_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'bug-mining'))
    
    # OUTPUT_MD 是 ../bug_summary.md
    OUTPUT_MD = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'bug_summary.md'))
    
    # 从 config.py 获取 report.id 列的名称
    ISSUE_ID_COLUMN = config.BUGS_CSV_ISSUE_ID

    print(f"扫描目标目录: {BUG_MINING_DIR}")

    if not os.path.exists(BUG_MINING_DIR):
        print(f"Error: 目录未找到: {BUG_MINING_DIR}", file=sys.stderr)
        print("请先运行 fast_bug_miner.py 来生成 bug-mining 目录。", file=sys.stderr)
        sys.exit(1)

    all_project_stats = []
    total_bug_count = 0  # 初始化总缺陷计数器

    # --- 2. 遍历 bug-mining 目录 ---
    # 获取目录列表并排序，保证输出顺序一致
    project_dirs = sorted(os.listdir(BUG_MINING_DIR))
    
    for project_id in project_dirs:
        project_path = os.path.join(BUG_MINING_DIR, project_id)
        
        # 确保只处理目录
        if not os.path.isdir(project_path):
            continue

        csv_path = os.path.join(project_path, 'active-bugs.csv')
        
        # 检查 active-bugs.csv 是否存在
        if os.path.exists(csv_path):
            print(f"  -> 正在处理: {project_id}")
            bug_count = 0
            
            # 虽然我们不再在表格中打印 ID 列表，但我们仍然需要读取 CSV 来计算 bug_count
            # 并且进行基本的格式校验
            try:
                with open(csv_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    
                    # 读取表头
                    try:
                        header = next(reader)
                    except StopIteration:
                        print(f"     [Warning] {project_id} 的 active-bugs.csv 是空的, 已跳过。")
                        continue
                        
                    # 查找 "report.id" 列的索引
                    try:
                        id_index = header.index(ISSUE_ID_COLUMN)
                    except ValueError:
                        print(f"     [Error] {project_id} 的 CSV 文件中未找到列: '{ISSUE_ID_COLUMN}', 已跳过。", file=sys.stderr)
                        continue

                    # 遍历所有数据行进行计数
                    for row in reader:
                        if not row or len(row) <= id_index:
                            continue
                        bug_count += 1
                        # 我们不再收集具体的 ID 列表，只统计数量

                if bug_count > 0:
                    # 构建相对路径链接: bug-mining/<project_id>/active-bugs.csv
                    relative_link = f"bug-mining/{project_id}/active-bugs.csv"
                    all_project_stats.append([project_id, bug_count, relative_link])
                    total_bug_count += bug_count
                else:
                    print(f"     [Info] {project_id} 已处理, 但未找到缺陷行。")

            except Exception as e:
                print(f"     [Error] 处理 {project_id} 时发生错误: {e}", file=sys.stderr)

        else:
            pass

    # --- 3. 写入汇总的 Markdown 文件 ---
    if not all_project_stats:
        print("未找到任何项目数据, 汇总文件未生成。")
        return

    print(f"\n正在将汇总数据写入: {OUTPUT_MD}")

    try:
        with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
            # 3.1 写入文件头和总数
            f.write("# Project Bug Summary\n\n")
            f.write(f"**Total Bug Count:** {total_bug_count}\n\n")
            f.write(f"**Total Projects:** {len(all_project_stats)}\n\n")
            
            # 3.2 写入表格表头 
            # 将 "Issue IDs" 替换为 "Source File"
            f.write("| No. | Project ID | Bug Count | Source File |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            
            # 3.3 写入所有项目的数据
            for idx, row in enumerate(all_project_stats, 1):
                p_id, count, link_path = row
                # 生成 Markdown 链接 [View CSV](path)
                md_link = f"[View CSV]({link_path})"
                f.write(f"| {idx} | {p_id} | {count} | {md_link} |\n")

    except IOError as e:
        print(f"Error: 无法写入汇总文件: {e}", file=sys.stderr)
        sys.exit(1)

    print("汇总完成。")
    print(f"Markdown 文件已生成: {OUTPUT_MD}")
    print(f"所有项目的缺陷总数 (Total Bug Count): {total_bug_count}")

if __name__ == "__main__":
    main()