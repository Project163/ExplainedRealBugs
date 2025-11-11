<div align="center">
  <h1>ExplainedRealBugs</h1>
</div>

[简体中文](README.zh-CN.md)

## Introduction

ExplainedRealBugs (Based on defects4j) is a framework designed to automate the process of mining bug data from various software repositories and issue trackers. It provides a streamlined workflow to identify, collect, and process bug-related information, creating a structured dataset for analysis and research.

## Project Purpose

The primary goal of this project is to build a comprehensive bug repository. It achieves this by:

1.  Cloning Git repositories of specified projects.
2.  Downloading bug reports from various issue trackers like Jira, GitHub, and Bugzilla.
3.  Cross-referencing Git commit logs with bug reports to identify bug-fixing commits.
4.  Generating patch files (`.diff` or `.patch`) that represent the code changes for each bug fix.
5.  Consolidating this information into a structured format, including a CSV file (`active-bugs.csv`) that links bug reports to their corresponding fixing commits.
6.  Gathering the bug reports and associated data.
7.  Providing a cleanup script to remove data for specific projects.

## Features

*   **Automated Bug Mining**: Automatically clones repositories, downloads bug reports, and identifies bug-fixing commits.
*   **Multi-Tracker Support**: Supports issue trackers like Jira, GitHub, and Bugzilla.
*   **Structured Output**: Generates a clean, structured dataset including patch files and a CSV mapping bugs to commits.
*   **Error Logging**: All error messages during the mining process are logged to `error.txt` for easy debugging.
*   **Data Cleanup**: Includes a script to selectively remove all cached and output data for specified projects.

## Bug Repository Overview

Currently, the repository contains bug data for **299** projects, with a total of **59,934** bugs. Below is a summary of the bug counts for each project.

<details>
<summary>Click to expand for a detailed list of all projects</summary>

### 表格 1

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ActiveAdmin | 148 | Babel | 72 | Catch2 | 338 |
| ActixWeb | 41 | Bazel | 379 | Cayenne_jgroups | 2 |
| Akka | 110 | Bcel | 124 | Cayenne_jms | 2 |
| Alacritty | 632 | Beam | 2984 | Cayenne_xmpp | 2 |
| Alamofire | 14 | Bevy | 1050 | Chalk | 33 |
| Alembic | 121 | Black | 268 | ChartJS | 69 |
| AssertJ | 577 | Bleve | 143 | ChartsSwift | 118 |
| Assimp | 128 | Bsf | 11 | Chi | 24 |
| AutoMapper | 206 | CakePHP | 336 | Cli | 239 |
| Axum | 24 | Capybara | 110 | Click | 85 |

--------------------

### 表格 2

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Closure | 480 | CypressTestingLibrary | 12 | DoctrineDBAL | 50 |
| CodeIgniter | 545 | D3 | 273 | DoctrineORM | 66 |
| Codec | 173 | Daemon | 131 | Dosgi_common | 17 |
| Collections | 204 | Dbcp | 196 | Doxia_module_apt | 50 |
| Compress | 509 | Dbutils | 30 | EFCore | 740 |
| Configuration | 326 | Deltaspike_api | 111 | Egui | 116 |
| Crypto | 90 | Devise | 164 | Electron | 5 |
| Csv | 141 | Diesel | 265 | ElectronFiddle | 5 |
| Curl | 839 | Digester | 39 | Email | 51 |
| Cypress | 12 | DockerCLI | 21 | Eslint | 694 |

--------------------

### 表格 3

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Etcd | 55 | Flume_ngcore | 193 | GoRedis | 50 |
| Exec | 50 | Fmt | 62 | GoSwagger | 357 |
| ExoPlayer | 9 | Forem | 37 | Gofumpt | 76 |
| Fabric | 13 | Functor | 6 | Goreleaser | 395 |
| Fastify | 72 | GPerfTools | 2 | Gorm | 33 |
| Fastlane | 46 | GRPC | 53 | Graph | 10 |
| Fiber | 30 | Geometry_core | 5 | Guava | 33 |
| FileUpload | 85 | Gitea | 723 | Gulp | 44 |
| Flake8 | 101 | Glfw | 376 | Hbase_common | 554 |
| FluentValidation | 14 | Glm | 1 | Helix | 56 |

--------------------

### 表格 4

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Helm | 136 | Imaging | 143 | James_project_mailet_standard | 40 |
| Hivemall_core | 28 | Incubator_tamaya_api | 13 | James_project_server_container_core | 44 |
| Homebrew | 138 | Istio | 21 | Jci_core | 8 |
| HttpClient5 | 143 | JUnit5 | 797 | Jelly_core | 1 |
| Httpcomponents_core_h2 | 21 | JXR | 41 | Jena_core | 202 |
| Httpcomponents_core_httpcore5 | 86 | Jackrabbit_filevault_vault_core | 174 | JestDom | 10 |
| Httpie | 69 | Jackrabbit_filevault_vault_validation | 42 | Jexl | 251 |
| Hyper | 320 | Jackrabbit_oak_core | 1912 | Jinja2 | 82 |
| IO | 419 | JacksonDatabind | 844 | Johnzon_core | 81 |
| Iced | 33 | James_project_core | 21 | Johnzon_jaxrs | 14 |

--------------------

### 表格 5

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Johnzon_jsonb | 85 | Laravel | 45 | MShade | 135 |
| Johnzon_jsonschema | 4 | LeakCanary | 283 | Math | 671 |
| Johnzon_mapper | 120 | LessJS | 261 | Math_4j | 423 |
| Jsoup | 427 | LibGDX | 590 | Maven2_artifact | 76 |
| JxPath | 59 | Libuv | 101 | Maven2_project | 190 |
| K6 | 282 | Logging | 42 | Maven_checkstyle_plugin | 109 |
| Karaf_main | 142 | Logrus | 28 | MetaModel_core | 48 |
| Kingfisher | 3 | LottieAndroid | 332 | MetaModel_csv | 11 |
| Knox_assertion_common | 17 | MDeploy | 40 | MetaModel_excel | 8 |
| Lang | 641 | MGpg | 27 | MetaModel_jdbc | 37 |

--------------------

### 表格 6

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MetaModel_pojo | 4 | Neovim | 97 | Ognl | 109 |
| MetaModel_salesforce | 4 | Net | 271 | OkHttp | 30 |
| Minaftp_api | 18 | Netty | 365 | Oozie_client | 118 |
| Mitmproxy | 502 | NewtonsoftJson | 14 | PHPStan | 17 |
| Mockito | 365 | NextJS | 85 | PHPUnit | 967 |
| Monolog | 160 | Nifi_mock | 72 | PM2 | 94 |
| Mrunit | 50 | NodeFetch | 19 | Pandas | 31 |
| Mshared_archiver | 22 | Numbers_angle | 2 | Paramiko | 96 |
| Mypy | 662 | OBSStudio | 86 | Pdfbox_fontbox | 453 |
| NUnit | 180 | Oak_commons | 39 | Pdfbox_pdfbox | 3119 |

--------------------

### 表格 7

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Pest | 6 | Proxy | 5 | Quarkus | 280 |
| PhpFaker | 6 | Psalm | 1282 | Rails | 245 |
| Pillow | 91 | Pug | 179 | Rand | 54 |
| PlayFramework | 190 | Pundit | 13 | Rat_core | 124 |
| Playwright | 87 | PycaCryptography | 182 | Rat_plugin | 93 |
| Poetry | 49 | Pydantic | 193 | Rave_commons | 4 |
| Polars | 3 | Pylint | 384 | Rave_core | 27 |
| Polly | 39 | Pytest | 532 | Rave_web | 22 |
| Pool | 187 | Qpid_client | 255 | Rclone | 1433 |
| Prettier | 10 | Qpidjms_client | 658 | Rdf_jena | 1 |

--------------------

### 表格 8

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ReactHookForm | 491 | Rocket | 272 | Serilog | 81 |
| ReactRouter | 114 | Rollup | 178 | Shindig_common | 78 |
| Redis | 113 | RspecCore | 285 | Shiro_core | 98 |
| Redux | 51 | RxJava | 22 | Shiro_web | 53 |
| ReduxToolkit | 15 | SFML | 74 | Sidekiq | 358 |
| Release_plugin | 15 | SQLAlchemy | 571 | Slim | 81 |
| Reqwest | 106 | Sass | 82 | Sling_apiregions | 19 |
| Retrofit | 21 | Scxml | 123 | Sling_classloader | 35 |
| Rich | 9 | SeaORM | 6 | Sling_cpconverter | 169 |
| Ripper | 448 | Sentry_ccommon | 24 | Sling_discovery | 15 |

--------------------

### 表格 9

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Sling_html | 3 | SpringFramework | 5 | Syncthing | 1507 |
| Sling_log | 55 | SqlxGo | 28 | Tauri | 632 |
| Sling_messaging_mail | 5 | SqlxRust | 86 | Testcontainers | 2 |
| Sling_metrics | 8 | Starship | 39 | Text | 90 |
| Sling_osgi | 9 | Storm_client | 176 | Tez_common | 72 |
| Sling_scheduler | 31 | Storybook | 31 | ThreeJS | 11 |
| Sling_threads | 25 | Streamlit | 183 | Tika | 1477 |
| Sling_validation | 18 | Struts1_core | 35 | Tika_app | 54 |
| Sling_webconsole | 1 | SvelteKit | 570 | Tika_core | 419 |
| Spdlog | 121 | Symfony | 38 | Tiles_core | 5 |

--------------------

### 表格 10

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tinkerpop_gremlin_core | 173 | Weaver_processor | 2 | Xbean_reflect | 59 |
| Twill_dcore | 8 | Webbeans_web | 92 | Xmlgraphics | 25 |
| TypeORM | 168 | Webpack | 152 | Xunit | 155 |
| Uvicorn | 11 | Wicket_cdi | 18 | Yew | 35 |
| Vagrant | 232 | Wicket_core | 1619 | Yii2 | 929 |
| Validator | 119 | Wicket_request | 151 | YugabyteDB | 328 |
| Vcpkg | 66 | Wicket_spring | 35 | Zaproxy | 404 |
| Vfs | 309 | Wicket_util | 110 | Zerolog | 20 |
| Vue2 | 473 | Wink_common | 89 | Zlib | 1 |
| Vysper_nbxml | 9 | Xbean_naming | 57 |  |  |

--------------------


</details>

For a complete list of bug report IDs and other details, please see the [`bug_summary.csv`](bug_summary.csv) file.

## Getting Started

Follow these steps to set up and run the bug mining framework.

### Prerequisites

*   Ubuntu(We are using 24.04)
*   Python 3(We are using 3.12)
*   Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Project163/ExplainedRealBugs.git
    cd ExplainedRealBugs
    ```

2.  **Install Python dependencies:**
    The framework requires `requests` and `beautifulsoup4`. Install them using the provided requirements file.
    ```sh
    pip install -r framework/requirements.txt
    ```
    Alternatively, you can install them manually:
    ```sh
    pip install requests beautifulsoup4
    ```

### Configuration

1.  **Define Target Projects:**
    Edit the `framework/example.txt` file(if it not exists, you can create it manually) to specify the projects you want to mine. Each line represents a project and should be a **tab-separated** list with the following format:
    `project_id	project_name	repository_url	issue_tracker_name	issue_tracker_project_id	bug_fix_regex`

    Example line:
    `Bsf	bsf	https://github.com/apache/commons-bsf.git	jira	BSF	/(BSF-\\d+)/mi	.`

    Where:
    *   `issue_tracker_name` can be `github`, `jira`, `bugzilla(Waiting for update)`, etc. (see [`SUPPORTED_TRACKERS`](framework/download_issues.py) in [`framework/download_issues.py`](framework/download_issues.py)).

2.  **(Optional) GitHub API Token:**
    To avoid rate-limiting issues when downloading from GitHub, it is highly recommended to set a personal access token as an environment variable.
    - Linux
    ```sh
    export GH_TOKEN="your_github_personal_access_token"
    ```
    - Windows(Still waiting for update)
    ```bash
    set GH_TOKEN "your_github_personal_access_token"
    ```
### Running the Miner

Execute the main script to start the mining process. The script will read the projects from `framework/example.txt` and process them sequentially.

```sh
python framework/fast_bug_miner.py
```

The script will handle the creation of necessary cache and output directories. Any errors encountered during the process will be logged to `error.txt` in the root directory for debugging.

### Cleaning Up Data

The framework includes a script to clean up all data (mined output and cache) for specific projects. This is useful for removing corrupted data or starting fresh.

1.  **Create a `delete.txt` file:**
    Create a file named `framework/delete.txt`. This file should list the projects you want to clean, following the same format as `framework/example.txt`.

2.  **Run the cleanup script:**
    ```sh
    python framework/clean_bug_and_cache.py
    ```
    You can also specify a different input file using the `-i` flag:
    ```sh
    python framework/clean_bug_and_cache.py -i path/to/your/project_list.txt
    ```

### Output

The mined data for each project will be stored in the `bug-mining/` directory. For each `project_id` defined in the input file, you will find a corresponding folder:

```
bug-mining/
└── <project_id>/
    ├── active-bugs.csv      # CSV file mapping bug IDs to fixing commits
    └── patches/             # Directory containing patch files for each bug
        ├── 1.src.patch
        └── ...
    └── reports/            # Directory containing downloaded report files for each bug
        ├── 1.report.xxx
        └── ...
```
