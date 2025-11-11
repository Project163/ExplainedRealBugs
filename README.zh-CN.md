<div align="center">
  <h1>ExplainedRealBugs</h1>
</div>

[English](README.md)

## 介绍

ExplainedRealBugs（基于 defects4j）是一个旨在自动化从各种软件仓库和问题跟踪器中挖掘错误数据的框架。它提供了一个简化的工作流程来识别、收集和处理与错误相关的信息，从而创建一个用于分析和研究的结构化数据集。

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

## 缺陷库概览

目前，该缺陷库包含了 **298** 个项目的错误数据，总计 **56,950** 个错误。以下是每个项目错误数量的摘要。

<details>
<summary>点击展开以查看所有项目的详细列表</summary>

### 表格 1

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ActiveAdmin | 148 | Babel | 72 | Cayenne_jgroups | 2 |
| ActixWeb | 41 | Bazel | 379 | Cayenne_jms | 2 |
| Akka | 110 | Bcel | 124 | Cayenne_xmpp | 2 |
| Alacritty | 632 | Bevy | 1050 | Chalk | 33 |
| Alamofire | 14 | Black | 268 | ChartJS | 69 |
| Alembic | 121 | Bleve | 143 | ChartsSwift | 118 |
| AssertJ | 577 | Bsf | 11 | Chi | 24 |
| Assimp | 128 | CakePHP | 336 | Cli | 239 |
| AutoMapper | 206 | Capybara | 110 | Click | 85 |
| Axum | 24 | Catch2 | 338 | Closure | 480 |

--------------------

### 表格 2

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CodeIgniter | 545 | D3 | 273 | DoctrineORM | 66 |
| Codec | 173 | Daemon | 131 | Dosgi_common | 17 |
| Collections | 204 | Dbcp | 196 | Doxia_module_apt | 50 |
| Compress | 509 | Dbutils | 30 | EFCore | 740 |
| Configuration | 326 | Deltaspike_api | 111 | Egui | 116 |
| Crypto | 90 | Devise | 164 | Electron | 5 |
| Csv | 141 | Diesel | 265 | ElectronFiddle | 5 |
| Curl | 839 | Digester | 39 | Email | 51 |
| Cypress | 12 | DockerCLI | 21 | Eslint | 694 |
| CypressTestingLibrary | 12 | DoctrineDBAL | 50 | Etcd | 55 |

--------------------

### 表格 3

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Exec | 50 | Fmt | 62 | GoSwagger | 357 |
| ExoPlayer | 9 | Forem | 37 | Gofumpt | 76 |
| Fabric | 13 | Functor | 6 | Goreleaser | 395 |
| Fastify | 72 | GPerfTools | 2 | Gorm | 33 |
| Fastlane | 46 | GRPC | 53 | Graph | 10 |
| Fiber | 30 | Geometry_core | 5 | Guava | 33 |
| FileUpload | 85 | Gitea | 723 | Gulp | 44 |
| Flake8 | 101 | Glfw | 376 | Hbase_common | 554 |
| FluentValidation | 14 | Glm | 1 | Helix | 56 |
| Flume_ngcore | 193 | GoRedis | 50 | Helm | 136 |

--------------------

### 表格 4

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Hivemall_core | 28 | Incubator_tamaya_api | 13 | James_project_server_container_core | 44 |
| Homebrew | 138 | Istio | 21 | Jci_core | 8 |
| HttpClient5 | 143 | JUnit5 | 797 | Jelly_core | 1 |
| Httpcomponents_core_h2 | 21 | JXR | 41 | Jena_core | 202 |
| Httpcomponents_core_httpcore5 | 86 | Jackrabbit_filevault_vault_core | 174 | JestDom | 10 |
| Httpie | 69 | Jackrabbit_filevault_vault_validation | 42 | Jexl | 251 |
| Hyper | 320 | Jackrabbit_oak_core | 1912 | Jinja2 | 82 |
| IO | 419 | JacksonDatabind | 844 | Johnzon_core | 81 |
| Iced | 33 | James_project_core | 21 | Johnzon_jaxrs | 14 |
| Imaging | 143 | James_project_mailet_standard | 40 | Johnzon_jsonb | 85 |

--------------------

### 表格 5

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Johnzon_jsonschema | 4 | LeakCanary | 283 | Math | 671 |
| Johnzon_mapper | 120 | LessJS | 261 | Math_4j | 423 |
| Jsoup | 427 | LibGDX | 590 | Maven2_artifact | 76 |
| JxPath | 59 | Libuv | 101 | Maven2_project | 190 |
| K6 | 282 | Logging | 42 | Maven_checkstyle_plugin | 109 |
| Karaf_main | 142 | Logrus | 28 | MetaModel_core | 48 |
| Kingfisher | 3 | LottieAndroid | 332 | MetaModel_csv | 11 |
| Knox_assertion_common | 17 | MDeploy | 40 | MetaModel_excel | 8 |
| Lang | 641 | MGpg | 27 | MetaModel_jdbc | 37 |
| Laravel | 45 | MShade | 135 | MetaModel_pojo | 4 |

--------------------

### 表格 6

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MetaModel_salesforce | 4 | Net | 271 | OkHttp | 30 |
| Minaftp_api | 18 | Netty | 365 | Oozie_client | 118 |
| Mitmproxy | 502 | NewtonsoftJson | 14 | PHPStan | 17 |
| Mockito | 365 | NextJS | 85 | PHPUnit | 967 |
| Monolog | 160 | Nifi_mock | 72 | PM2 | 94 |
| Mrunit | 50 | NodeFetch | 19 | Pandas | 31 |
| Mshared_archiver | 22 | Numbers_angle | 2 | Paramiko | 96 |
| Mypy | 662 | OBSStudio | 86 | Pdfbox_fontbox | 453 |
| NUnit | 180 | Oak_commons | 39 | Pdfbox_pdfbox | 3119 |
| Neovim | 97 | Ognl | 109 | Pest | 6 |

--------------------

### 表格 7

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PhpFaker | 6 | Psalm | 1282 | Rails | 245 |
| Pillow | 91 | Pug | 179 | Rand | 54 |
| PlayFramework | 190 | Pundit | 13 | Rat_core | 124 |
| Playwright | 87 | PycaCryptography | 182 | Rat_plugin | 93 |
| Poetry | 49 | Pydantic | 193 | Rave_commons | 4 |
| Polars | 3 | Pylint | 384 | Rave_core | 27 |
| Polly | 39 | Pytest | 532 | Rave_web | 22 |
| Pool | 187 | Qpid_client | 255 | Rclone | 1433 |
| Prettier | 10 | Qpidjms_client | 658 | Rdf_jena | 1 |
| Proxy | 5 | Quarkus | 280 | ReactHookForm | 491 |

--------------------

### 表格 8

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ReactRouter | 114 | Rollup | 178 | Shindig_common | 78 |
| Redis | 113 | RspecCore | 285 | Shiro_core | 98 |
| Redux | 51 | RxJava | 22 | Shiro_web | 53 |
| ReduxToolkit | 15 | SFML | 74 | Sidekiq | 358 |
| Release_plugin | 15 | SQLAlchemy | 571 | Slim | 81 |
| Reqwest | 106 | Sass | 82 | Sling_apiregions | 19 |
| Retrofit | 21 | Scxml | 123 | Sling_classloader | 35 |
| Rich | 9 | SeaORM | 6 | Sling_cpconverter | 169 |
| Ripper | 448 | Sentry_ccommon | 24 | Sling_discovery | 15 |
| Rocket | 272 | Serilog | 81 | Sling_html | 3 |

--------------------

### 表格 9

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Sling_log | 55 | SqlxGo | 28 | Tauri | 632 |
| Sling_messaging_mail | 5 | SqlxRust | 86 | Testcontainers | 2 |
| Sling_metrics | 8 | Starship | 39 | Text | 90 |
| Sling_osgi | 9 | Storm_client | 176 | Tez_common | 72 |
| Sling_scheduler | 31 | Storybook | 31 | ThreeJS | 11 |
| Sling_threads | 25 | Streamlit | 183 | Tika | 1477 |
| Sling_validation | 18 | Struts1_core | 35 | Tika_app | 54 |
| Sling_webconsole | 1 | SvelteKit | 570 | Tika_core | 419 |
| Spdlog | 121 | Symfony | 38 | Tiles_core | 5 |
| SpringFramework | 5 | Syncthing | 1507 | Tinkerpop_gremlin_core | 173 |

--------------------

### 表格 10

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Twill_dcore | 8 | Webbeans_web | 92 | Xmlgraphics | 25 |
| TypeORM | 168 | Webpack | 152 | Xunit | 155 |
| Uvicorn | 11 | Wicket_cdi | 18 | Yew | 35 |
| Vagrant | 232 | Wicket_core | 1619 | Yii2 | 929 |
| Validator | 119 | Wicket_request | 151 | YugabyteDB | 328 |
| Vcpkg | 66 | Wicket_spring | 35 | Zaproxy | 404 |
| Vfs | 309 | Wicket_util | 110 | Zerolog | 20 |
| Vue2 | 473 | Wink_common | 89 | Zlib | 1 |
| Vysper_nbxml | 9 | Xbean_naming | 57 |  |  |
| Weaver_processor | 2 | Xbean_reflect | 59 |  |  |

--------------------


</details>

如需查看完整的错误报告 ID 列表及其他详细信息，请参阅 [`bug_summary.csv`](bug_summary.csv) 文件。

## 入门指南

请按照以下步骤设置和运行错误挖掘框架。

### 先决条件

*   Ubuntu（我们使用的是 24.04）
*   Python 3（我们使用的是 3.12）
*   Git

### 安装

1.  **克隆存储库：**
    ```sh
    git clone https://github.com/Project163/ExplainedRealBugs.git
    cd ExplainedRealBugs
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
