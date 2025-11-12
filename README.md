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

Currently, the repository contains bug data for **317** projects, with a total of **128,502** bugs. Below is a summary of the bug counts for each project.

<details>
<summary>Click to expand for a detailed list of all projects</summary>

### Table 1

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

### Table 2

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

### Table 3

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

### Table 4

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Goreleaser | 395 | Hivemall_core | 28 | Incubator_tamaya_api | 13 |
| Gorm | 33 | Homebrew | 138 | Istio | 21 |
| Graph | 10 | HttpClient5 | 143 | JUnit5 | 797 |
| Groovy | 5019 | Httpcomponents_core_h2 | 21 | JXR | 41 |
| Guava | 33 | Httpcomponents_core_httpcore5 | 86 | Jackrabbit_filevault_vault_core | 174 |
| Gulp | 44 | Httpie | 69 | Jackrabbit_filevault_vault_validation | 42 |
| Hadoop | 3048 | Hyper | 320 | Jackrabbit_oak_core | 1912 |
| Hbase_common | 554 | IO | 419 | JacksonDatabind | 844 |
| Helix | 56 | Iced | 33 | James_project_core | 21 |
| Helm | 136 | Imaging | 143 | James_project_mailet_standard | 40 |

--------------------

### Table 5

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| James_project_server_container_core | 44 | Johnzon_jsonschema | 4 | Laravel | 45 |
| Jci_core | 8 | Johnzon_mapper | 120 | LeakCanary | 283 |
| Jelly_core | 1 | Jsoup | 427 | LessJS | 261 |
| Jena_core | 202 | JxPath | 59 | LibGDX | 590 |
| JestDom | 10 | K6 | 282 | Libuv | 101 |
| Jexl | 251 | Kafka | 4311 | Logging | 42 |
| Jinja2 | 82 | Karaf_main | 142 | Logrus | 28 |
| Johnzon_core | 81 | Kingfisher | 3 | LottieAndroid | 332 |
| Johnzon_jaxrs | 14 | Knox_assertion_common | 17 | MCompiler | 138 |
| Johnzon_jsonb | 85 | Lang | 641 | MDeploy | 40 |

--------------------

### Table 6

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MGpg | 27 | MetaModel_excel | 8 | Mypy | 662 |
| MJavadoc | 273 | MetaModel_jdbc | 37 | NUnit | 180 |
| MShade | 135 | MetaModel_pojo | 4 | Neovim | 97 |
| Math | 671 | MetaModel_salesforce | 4 | Net | 271 |
| Math_4j | 423 | Minaftp_api | 18 | Netty | 365 |
| Maven2_artifact | 76 | Mitmproxy | 502 | NewtonsoftJson | 14 |
| Maven2_project | 190 | Mockito | 365 | NextJS | 85 |
| Maven_checkstyle_plugin | 109 | Monolog | 160 | Nifi_mock | 72 |
| MetaModel_core | 48 | Mrunit | 50 | NodeFetch | 19 |
| MetaModel_csv | 11 | Mshared_archiver | 22 | Numbers_angle | 2 |

--------------------

### Table 7

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OBSStudio | 86 | Pdfbox_fontbox | 453 | Pool | 187 |
| Oak_commons | 39 | Pdfbox_pdfbox | 3119 | Prettier | 10 |
| Ognl | 109 | Pest | 6 | Proxy | 5 |
| OkHttp | 30 | PhpFaker | 6 | Psalm | 1282 |
| Oozie_client | 118 | Pillow | 91 | Pug | 179 |
| PHPStan | 17 | PlayFramework | 190 | Pundit | 13 |
| PHPUnit | 967 | Playwright | 87 | PycaCryptography | 182 |
| PM2 | 94 | Poetry | 49 | Pydantic | 193 |
| Pandas | 31 | Polars | 3 | Pylint | 384 |
| Paramiko | 96 | Polly | 39 | Pytest | 532 |

--------------------

### Table 8

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qpid_client | 255 | Rclone | 1433 | Rich | 9 |
| Qpidjms_client | 658 | Rdf_jena | 1 | Ripper | 448 |
| Quarkus | 280 | ReactHookForm | 491 | Rocket | 272 |
| Rails | 245 | ReactRouter | 114 | Rollup | 178 |
| Rand | 54 | Redis | 113 | RspecCore | 285 |
| Rat_core | 124 | Redux | 51 | RxJava | 22 |
| Rat_plugin | 93 | ReduxToolkit | 15 | SFML | 74 |
| Rave_commons | 4 | Release_plugin | 15 | SQLAlchemy | 571 |
| Rave_core | 27 | Reqwest | 106 | Sass | 82 |
| Rave_web | 22 | Retrofit | 21 | Scxml | 123 |

--------------------

### Table 9

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SeaORM | 6 | Sling_cpconverter | 169 | Sling_webconsole | 1 |
| Sentry_ccommon | 24 | Sling_discovery | 15 | Solr | 5327 |
| Serilog | 81 | Sling_html | 3 | Spark | 10342 |
| Shindig_common | 78 | Sling_log | 55 | Spdlog | 121 |
| Shiro_core | 98 | Sling_messaging_mail | 5 | SpringFramework | 5 |
| Shiro_web | 53 | Sling_metrics | 8 | SqlxGo | 28 |
| Sidekiq | 358 | Sling_osgi | 9 | SqlxRust | 86 |
| Slim | 81 | Sling_scheduler | 31 | Starship | 39 |
| Sling_apiregions | 19 | Sling_threads | 25 | Storm_client | 176 |
| Sling_classloader | 35 | Sling_validation | 18 | Storybook | 31 |

--------------------

### Table 10

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Streamlit | 183 | Tez_common | 72 | Uvicorn | 11 |
| Struts1_core | 35 | ThreeJS | 11 | Vagrant | 232 |
| Subversion | 39 | Thrift | 2310 | Validator | 119 |
| Surefire | 779 | Tika | 1477 | Vcpkg | 66 |
| SvelteKit | 570 | Tika_app | 54 | Vfs | 309 |
| Symfony | 38 | Tika_core | 419 | Vue2 | 473 |
| Syncthing | 1507 | Tiles_core | 5 | Vysper_nbxml | 9 |
| Tauri | 632 | Tinkerpop_gremlin_core | 173 | Weaver_processor | 2 |
| Testcontainers | 2 | Twill_dcore | 8 | Webbeans_web | 92 |
| Text | 90 | TypeORM | 168 | Webpack | 152 |

--------------------

### Table 11

| project_id | bug_count | project_id | bug_count | project_id | bug_count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Wicket_cdi | 18 | Yew | 35 |  |  |
| Wicket_core | 1619 | Yii2 | 929 |  |  |
| Wicket_request | 151 | YugabyteDB | 328 |  |  |
| Wicket_spring | 35 | Zaproxy | 404 |  |  |
| Wicket_util | 110 | Zerolog | 20 |  |  |
| Wink_common | 89 | Zlib | 1 |  |  |
| Xbean_naming | 57 | Zookeeper | 1191 |  |  |
| Xbean_reflect | 59 |  |  |  |  |
| Xmlgraphics | 25 |  |  |  |  |
| Xunit | 155 |  |  |  |  |

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
