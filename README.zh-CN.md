<div align="center">
  <h1>ExplainedRealBugs</h1>
</div>

[English](README.md)

## 介绍

ExplainedRealBugs（基于 defects4j）是一个旨在自动化从各种软件仓库和问题跟踪器中挖掘缺陷数据的框架。它提供了一个简化的工作流程来识别、收集和处理与缺陷相关的信息，从而创建一个用于分析和研究的结构化数据集。

## 项目目标

该项目的主要目标是构建一个全面的缺陷存储库。它通过以下方式实现这一目标：

1.  克隆指定项目的 Git 仓库。
2.  从 Jira、GitHub 和 Bugzilla 等各种问题跟踪器下载缺陷报告。
3.  将 Git 提交日志与缺陷报告进行交叉引用，以识别修复缺陷的提交。
4.  生成代表每个缺陷修复的代码更改的补丁文件（`.diff` 或 `.patch`）。
5.  将此信息整合为结构化格式，包括一个将缺陷报告链接到其相应修复提交的 CSV 文件（`active-bugs.csv`）。
6.  收集缺陷报告及相关数据。
7.  提供清理脚本以删除特定项目的数据。

## 功能特性

*   **自动化缺陷挖掘**: 自动克隆仓库、下载缺陷报告并识别缺陷修复提交。
*   **多跟踪器支持**: 支持 Jira、GitHub 和 Bugzilla 等问题跟踪器。
*   **结构化输出**: 生成干净、结构化的数据集，包括补丁文件和将缺陷映射到提交的 CSV 文件。
*   **缺陷日志记录**: 挖掘过程中的所有缺陷消息都会记录到 `error.txt` 中，便于调试。
*   **数据清理**: 包含一个脚本，可选择性地删除指定项目的所有缓存和输出数据。

## 缺陷库概览

目前，该缺陷库包含了 **322** 个项目的缺陷数据，总计 **141,589** 个缺陷。以下是每个项目缺陷数量的摘要。

<details>
<summary>点击展开以查看所有项目的详细列表</summary>

### 表格 1

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ActiveAdmin | 148 | Axum | 24 | CakePHP | 336 |
| ActiveMQ | 3527 | Babel | 72 | Camel | 7294 |
| ActixWeb | 41 | Bazel | 379 | Capybara | 110 |
| Akka | 110 | Bcel | 124 | Cassandra | 6901 |
| Alacritty | 632 | Beam | 2984 | Catch2 | 338 |
| Alamofire | 14 | Bevy | 1050 | Cayenne_jgroups | 2 |
| Alembic | 121 | Black | 268 | Cayenne_jms | 2 |
| AssertJ | 577 | Bleve | 143 | Cayenne_xmpp | 2 |
| Assimp | 128 | Bsf | 11 | Chalk | 33 |
| AutoMapper | 206 | CXF | 3805 | ChartJS | 69 |

--------------------

### 表格 2

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ChartsSwift | 118 | Crypto | 90 | Derby | 3182 |
| Chi | 24 | Csv | 141 | Devise | 164 |
| Cli | 239 | Curl | 839 | Diesel | 265 |
| Click | 85 | Cypress | 12 | Digester | 39 |
| Closure | 480 | CypressTestingLibrary | 12 | DockerCLI | 21 |
| CodeIgniter | 545 | D3 | 273 | DoctrineDBAL | 50 |
| Codec | 173 | Daemon | 131 | DoctrineORM | 66 |
| Collections | 204 | Dbcp | 196 | Dosgi_common | 17 |
| Compress | 509 | Dbutils | 30 | Doxia_module_apt | 50 |
| Configuration | 326 | Deltaspike_api | 111 | EFCore | 740 |

--------------------

### 表格 3

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Egui | 116 | Fastlane | 46 | Functor | 6 |
| Electron | 5 | Felix | 3126 | GPerfTools | 2 |
| ElectronFiddle | 5 | Fiber | 30 | GRPC | 53 |
| Email | 51 | FileUpload | 85 | Geometry_core | 5 |
| Eslint | 694 | Flake8 | 101 | Gitea | 723 |
| Etcd | 55 | Flink | 7956 | Glfw | 376 |
| Exec | 50 | FluentValidation | 14 | Glm | 1 |
| ExoPlayer | 9 | Flume_ngcore | 193 | GoRedis | 50 |
| Fabric | 13 | Fmt | 62 | GoSwagger | 357 |
| Fastify | 72 | Forem | 37 | Gofumpt | 76 |

--------------------

### 表格 4

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Goreleaser | 395 | Hive | 8938 | Imaging | 143 |
| Gorm | 33 | Hivemall_core | 28 | Incubator_tamaya_api | 13 |
| Graph | 10 | Homebrew | 138 | Istio | 21 |
| Groovy | 5019 | HttpClient5 | 143 | JUnit5 | 797 |
| Guava | 33 | Httpcomponents_core_h2 | 21 | JXR | 41 |
| Gulp | 44 | Httpcomponents_core_httpcore5 | 86 | Jackrabbit_filevault_vault_core | 174 |
| Hadoop | 3048 | Httpie | 69 | Jackrabbit_filevault_vault_validation | 42 |
| Hbase_common | 554 | Hyper | 320 | Jackrabbit_oak_core | 1912 |
| Helix | 56 | IO | 419 | JacksonDatabind | 844 |
| Helm | 136 | Iced | 33 | James_project_core | 21 |

--------------------

### 表格 5

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| James_project_mailet_standard | 40 | Johnzon_jsonb | 85 | Lang | 641 |
| James_project_server_container_core | 44 | Johnzon_jsonschema | 4 | Laravel | 45 |
| Jci_core | 8 | Johnzon_mapper | 120 | LeakCanary | 283 |
| Jelly_core | 1 | Jsoup | 427 | LessJS | 261 |
| Jena_core | 202 | JxPath | 59 | LibGDX | 590 |
| JestDom | 10 | K6 | 282 | Libuv | 101 |
| Jexl | 251 | Kafka | 4311 | Log4j2 | 1664 |
| Jinja2 | 82 | Karaf_main | 142 | Logging | 42 |
| Johnzon_core | 81 | Kingfisher | 3 | Logrus | 28 |
| Johnzon_jaxrs | 14 | Knox_assertion_common | 17 | LottieAndroid | 332 |

--------------------

### 表格 6

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MCompiler | 138 | MetaModel_core | 48 | Mrunit | 50 |
| MDeploy | 40 | MetaModel_csv | 11 | Mshared_archiver | 22 |
| MGpg | 27 | MetaModel_excel | 8 | Mypy | 662 |
| MJavadoc | 273 | MetaModel_jdbc | 37 | NUnit | 180 |
| MShade | 135 | MetaModel_pojo | 4 | Neovim | 97 |
| Math | 671 | MetaModel_salesforce | 4 | Net | 271 |
| Math_4j | 423 | Minaftp_api | 18 | Netty | 365 |
| Maven2_artifact | 76 | Mitmproxy | 502 | NewtonsoftJson | 14 |
| Maven2_project | 190 | Mockito | 365 | NextJS | 85 |
| Maven_checkstyle_plugin | 109 | Monolog | 160 | Nifi_mock | 72 |

--------------------

### 表格 7

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| NodeFetch | 19 | Pandas | 31 | Poetry | 49 |
| Numbers_angle | 2 | Paramiko | 96 | Polars | 3 |
| OBSStudio | 86 | Pdfbox_fontbox | 453 | Polly | 39 |
| Oak_commons | 39 | Pdfbox_pdfbox | 3119 | Pool | 187 |
| Ognl | 109 | Pest | 6 | Prettier | 10 |
| OkHttp | 30 | PhpFaker | 6 | Proxy | 5 |
| Oozie_client | 118 | Pig | 2036 | Psalm | 1282 |
| PHPStan | 17 | Pillow | 91 | Pug | 179 |
| PHPUnit | 967 | PlayFramework | 190 | Pundit | 13 |
| PM2 | 94 | Playwright | 87 | PycaCryptography | 182 |

--------------------

### 表格 8

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Pydantic | 193 | Rave_commons | 4 | Release_plugin | 15 |
| Pylint | 384 | Rave_core | 27 | Reqwest | 106 |
| Pytest | 532 | Rave_web | 22 | Retrofit | 21 |
| Qpid_client | 255 | Rclone | 1433 | Rich | 9 |
| Qpidjms_client | 658 | Rdf_jena | 1 | Ripper | 448 |
| Quarkus | 280 | ReactHookForm | 491 | Rocket | 272 |
| Rails | 245 | ReactRouter | 114 | Rollup | 178 |
| Rand | 54 | Redis | 113 | RspecCore | 285 |
| Rat_core | 124 | Redux | 51 | RxJava | 22 |
| Rat_plugin | 93 | ReduxToolkit | 15 | SFML | 74 |

--------------------

### 表格 9

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SQLAlchemy | 571 | Slim | 81 | Sling_scheduler | 31 |
| Sass | 82 | Sling_apiregions | 19 | Sling_threads | 25 |
| Scxml | 123 | Sling_classloader | 35 | Sling_validation | 18 |
| SeaORM | 6 | Sling_cpconverter | 169 | Sling_webconsole | 1 |
| Sentry_ccommon | 24 | Sling_discovery | 15 | Solr | 5327 |
| Serilog | 81 | Sling_html | 3 | Spark | 10342 |
| Shindig_common | 78 | Sling_log | 55 | Spdlog | 121 |
| Shiro_core | 98 | Sling_messaging_mail | 5 | SpringFramework | 5 |
| Shiro_web | 53 | Sling_metrics | 8 | SqlxGo | 28 |
| Sidekiq | 358 | Sling_osgi | 9 | SqlxRust | 86 |

--------------------

### 表格 10

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Starship | 39 | Syncthing | 1507 | Tiles_core | 5 |
| Storm_client | 176 | Tauri | 632 | Tinkerpop_gremlin_core | 173 |
| Storybook | 31 | Testcontainers | 2 | Twill_dcore | 8 |
| Streamlit | 183 | Text | 90 | TypeORM | 168 |
| Struts1_core | 35 | Tez_common | 72 | Uvicorn | 11 |
| Subversion | 39 | ThreeJS | 11 | Vagrant | 232 |
| Surefire | 779 | Thrift | 2310 | Validator | 119 |
| SvelteKit | 570 | Tika | 1477 | Vcpkg | 66 |
| Symfony | 38 | Tika_app | 54 | Vfs | 309 |
| Synapse | 449 | Tika_core | 419 | Vue2 | 473 |

--------------------

### 表格 11

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Vysper_nbxml | 9 | Xbean_naming | 57 | Zookeeper | 1191 |
| Weaver_processor | 2 | Xbean_reflect | 59 |  |  |
| Webbeans_web | 92 | Xmlgraphics | 25 |  |  |
| Webpack | 152 | Xunit | 155 |  |  |
| Wicket_cdi | 18 | Yew | 35 |  |  |
| Wicket_core | 1619 | Yii2 | 929 |  |  |
| Wicket_request | 151 | YugabyteDB | 328 |  |  |
| Wicket_spring | 35 | Zaproxy | 404 |  |  |
| Wicket_util | 110 | Zerolog | 20 |  |  |
| Wink_common | 89 | Zlib | 1 |  |  |

--------------------



</details>

如需查看完整的缺陷报告 ID 列表及其他详细信息，请参阅 [`bug_summary.csv`](bug_summary.csv) 文件。

## 入门指南

请按照以下步骤设置和运行缺陷挖掘框架。

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

该脚本将处理必要的缓存和输出目录的创建。在此过程中遇到的任何缺陷都将记录在根目录下的 `error.txt` 文件中，以方便调试。

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
    ├── active-bugs.csv      # CSV 文件，将缺陷 ID 映射到修复提交
    └── patches/             # 包含每个缺陷补丁文件的目录
        ├── 1.src.patch
        └── ...
    └── reports/            # 包含每个缺陷下载的报告文件的目录
        ├── 1.report.xxx
        └── ...
```
