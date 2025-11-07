<div align="center">
  <h1>HugeBugRepository</h1>
</div>

[English](README.md)

## 介绍

HugeBugRepository（基于 defects4j）是一个旨在自动化从各种软件仓库和问题跟踪器中挖掘错误数据的框架。它提供了一个简化的工作流程来识别、收集和处理与错误相关的信息，从而创建一个用于分析和研究的结构化数据集。

## 项目目标

该项目的主要目标是构建一个全面的错误存储库。它通过以下方式实现这一目标：

1.  克隆指定项目的 Git 仓库。
2.  从 Jira、GitHub 和 Bugzilla 等各种问题跟踪器下载错误报告。
3.  将 Git 提交日志与错误报告进行交叉引用，以识别修复错误的提交。
4.  生成代表每个错误修复的代码更改的补丁文件（`.diff` 或 `.patch`）。
5.  将此信息整合为结构化格式，包括一个将错误报告链接到其相应修复提交的 CSV 文件（`active-bugs.csv`）。
6.  收集错误报告及相关数据。
7.  提供清理脚本以删除特定项目的数据。

## 功能特性

*   **自动化错误挖掘**: 自动克隆仓库、下载错误报告并识别错误修复提交。
*   **多跟踪器支持**: 支持 Jira、GitHub 和 Bugzilla 等问题跟踪器。
*   **结构化输出**: 生成干净、结构化的数据集，包括补丁文件和将错误映射到提交的 CSV 文件。
*   **错误日志记录**: 挖掘过程中的所有错误消息都会记录到 `error.txt` 中，便于调试。
*   **数据清理**: 包含一个脚本，可选择性地删除指定项目的所有缓存和输出数据。

## 入门指南

请按照以下步骤设置和运行错误挖掘框架。

### 先决条件

*   Ubuntu（我们使用的是 24.04）
*   Python 3（我们使用的是 3.12）
*   Git

### 安装

1.  **克隆存储库：**
    ```sh
    git clone <your-repository-url>
    cd HugeBugRepository
    ```

2.  **安装 Python 依赖项：**
    该框架需要 `requests` 和 `beautifulsoup4`。请使用提供的需求文件进行安装。
    ```sh
    pip install -r framework/requirements.txt
    ```
    除此之外，您还可以手动安装它们：
    ```sh
    pip install requests beautifulsoup4
    ```

### 配置

1.  **定义目标项目：**
    编辑 `framework/example.txt` 文件（若文件不存在，您可以手动创建它）以指定要挖掘的项目。每行代表一个项目，应为以下格式的制表符分隔列表：
    `project_id	project_name	repository_url	issue_tracker_name	issue_tracker_project_id	bug_fix_regex`

    示例行：
    `Bsf	bsf	https://github.com/apache/commons-bsf.git	jira	BSF	/(BSF-\\d+)/mi	.`

    其中：
    *   `issue_tracker_name` 可以是 `github`、`jira`、`bugzilla（等待更新）`等（请参阅 [`framework/download_issues.py`](framework/download_issues.py) 中的 [`SUPPORTED_TRACKERS`](framework/download_issues.py)）。

2.  **（可选）GitHub API 令牌：**
    为避免从 GitHub 下载时出现速率限制问题，强烈建议将个人访问令牌设置为环境变量。
    - Linux
    ```sh
    export GH_TOKEN="your_github_personal_access_token"
    ```
    - Windows (仍待更新)
    ```bash
    set GH_TOKEN "your_github_personal_access_token"
    ```
### 运行挖掘器

执行主脚本以启动挖掘过程。该脚本将从 `framework/example.txt` 读取项目并按顺序处理它们。

```sh
python framework/fast_bug_miner.py
```

该脚本将处理必要的缓存和输出目录的创建。在此过程中遇到的任何错误都将记录在根目录下的 `error.txt` 文件中，以方便调试。

### 清理数据

该框架包含一个脚本，用于清理特定项目的所有数据（挖掘输出和缓存）。这对于删除损坏的数据或重新开始非常有用。

1.  **创建 `delete.txt` 文件：**
    创建一个名为 `framework/delete.txt` 的文件。该文件应列出您要清理的项目，格式与 `framework/example.txt` 相同。

2.  **运行清理脚本：**
    ```sh
    python framework/clean_bug_and_cache.py
    ```
    您也可以使用 `-i` 标志指定不同的输入文件：
    ```sh
    python framework/clean_bug_and_cache.py -i path/to/your/project_list.txt
    ```

### 输出

每个项目的挖掘数据将存储在 `bug-mining/` 目录中。对于输入文件中定义的每个 `project_id`，您将找到一个相应的文件夹：

```
bug-mining/
└── <project_id>/
    ├── active-bugs.csv      # CSV 文件，将错误 ID 映射到修复提交
    └── patches/             # 包含每个错误补丁文件的目录
        ├── 1.src.patch
        └── ...
    └── reports/            # 包含每个错误下载的报告文件的目录
        ├── 1.report.xxx
        └── ...
```
