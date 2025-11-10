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

Currently, the repository contains bug data for **227** projects, with a total of **44,419** bugs. Below is a summary of the bug counts for each project.

<details>
<summary>Click to expand for a detailed list of all projects</summary>

| Project ID | Bug Count | Project ID | Bug Count | Project ID | Bug Count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ActixWeb | 41 | CakePHP | 336 | Collections | 204 |
| Akka | 110 | Catch2 | 338 | Compress | 509 |
| Alacritty | 632 | Cayenne_jgroups | 2 | Configuration | 326 |
| Assimp | 128 | Cayenne_jms | 2 | Crypto | 90 |
| Babel | 72 | Cayenne_xmpp | 2 | Csv | 141 |
| Bazel | 379 | Chalk | 33 | Cypress | 12 |
| Bcel | 124 | Chi | 24 | D3 | 273 |
| Bevy | 1050 | Cli | 239 | Daemon | 131 |
| Black | 268 | Closure | 480 | Dbcp | 196 |
| Bsf | 11 | Codec | 173 | Dbutils | 30 |
| Deltaspike_api | 111 | Etcd | 55 | GRPC | 53 |
| Diesel | 265 | Exec | 50 | Geometry_core | 5 |
| Digester | 39 | Fastify | 72 | Gitea | 723 |
| DockerCLI | 21 | Fastlane | 46 | Gorm | 33 |
| Dosgi_common | 17 | Fiber | 30 | Graph | 10 |
| Doxia_module_apt | 50 | FileUpload | 85 | Guava | 33 |
| Electron | 5 | Flume_ngcore | 193 | Hbase_common | 554 |
| ElectronFiddle | 5 | Fmt | 62 | Helix | 56 |
| Email | 51 | Forem | 37 | Helm | 136 |
| Eslint | 694 | Functor | 6 | Hivemall_core | 28 |
| Homebrew | 138 | JUnit5 | 797 | Jena_core | 202 |
| HttpClient5 | 143 | JXR | 41 | Jexl | 251 |
| Httpcomponents_core_h2 | 21 | Jackrabbit_filevault_vault_core | 174 | Johnzon_core | 81 |
| Httpcomponents_core_httpcore5 | 86 | Jackrabbit_filevault_vault_validation | 42 | Johnzon_jaxrs | 14 |
| Httpie | 69 | Jackrabbit_oak_core | 1912 | Johnzon_jsonb | 85 |
| Hyper | 320 | James_project_core | 21 | Johnzon_jsonschema | 4 |
| IO | 419 | James_project_mailet_standard | 40 | Johnzon_mapper | 120 |
| Imaging | 143 | James_project_server_container_core | 44 | JxPath | 59 |
| Incubator_tamaya_api | 13 | Jci_core | 8 | K6 | 282 |
| Istio | 21 | Jelly_core | 1 | Karaf_main | 142 |
| Knox_assertion_common | 17 | Maven2_artifact | 76 | Mitmproxy | 502 |
| Lang | 641 | Maven2_project | 190 | Mockito | 365 |
| Laravel | 45 | Maven_checkstyle_plugin | 109 | Monolog | 160 |
| LibGDX | 590 | MetaModel_core | 48 | Mrunit | 50 |
| Logging | 42 | MetaModel_csv | 11 | Mshared_archiver | 22 |
| MDeploy | 40 | MetaModel_excel | 8 | Mypy | 662 |
| MGpg | 27 | MetaModel_jdbc | 37 | Neovim | 97 |
| MShade | 135 | MetaModel_pojo | 4 | Net | 271 |
| Math | 671 | MetaModel_salesforce | 4 | Netty | 365 |
| Math_4j | 423 | Minaftp_api | 18 | Nifi_mock | 72 |
| NodeFetch | 19 | Pdfbox_pdfbox | 3119 | Pug | 179 |
| Numbers_angle | 2 | Pest | 6 | Pydantic | 193 |
| OBSStudio | 86 | PhpFaker | 6 | Pylint | 384 |
| Oak_commons | 39 | Pillow | 91 | Pytest | 532 |
| Ognl | 109 | PlayFramework | 190 | Qpid_client | 255 |
| OkHttp | 30 | Playwright | 87 | Qpidjms_client | 658 |
| Oozie_client | 118 | Poetry | 49 | Quarkus | 280 |
| PHPUnit | 967 | Pool | 187 | Rails | 245 |
| Pandas | 31 | Prettier | 10 | Rat_core | 124 |
| Pdfbox_fontbox | 453 | Proxy | 5 | Rat_plugin | 93 |
| Rave_commons | 4 | Rich | 9 | Shiro_web | 53 |
| Rave_core | 27 | Ripper | 448 | Sidekiq | 358 |
| Rave_web | 22 | Rocket | 272 | Slim | 81 |
| Rclone | 1433 | Rollup | 178 | Sling_apiregions | 19 |
| Rdf_jena | 1 | RspecCore | 285 | Sling_classloader | 35 |
| Redis | 113 | RxJava | 22 | Sling_cpconverter | 169 |
| Redux | 51 | Scxml | 123 | Sling_discovery | 15 |
| Release_plugin | 15 | Sentry_ccommon | 24 | Sling_html | 3 |
| Reqwest | 106 | Shindig_common | 78 | Sling_log | 55 |
| Retrofit | 21 | Shiro_core | 98 | Sling_messaging_mail | 5 |
| Sling_metrics | 8 | Streamlit | 183 | Tika_app | 54 |
| Sling_osgi | 9 | Struts1_core | 35 | Tika_core | 419 |
| Sling_scheduler | 31 | SvelteKit | 570 | Tiles_core | 5 |
| Sling_threads | 25 | Symfony | 38 | Tinkerpop_gremlin_core | 173 |
| Sling_validation | 18 | Syncthing | 1507 | Twill_dcore | 8 |
| Sling_webconsole | 1 | Tauri | 632 | TypeORM | 168 |
| SpringFramework | 5 | Text | 90 | Uvicorn | 11 |
| Starship | 39 | Tez_common | 72 | Validator | 119 |
| Storm_client | 176 | ThreeJS | 11 | Vcpkg | 66 |
| Storybook | 31 | Tika | 1477 | Vfs | 309 |
| Vue2 | 473 | Wink_common | 89 |  |  |
| Vysper_nbxml | 9 | Xbean_naming | 57 |  |  |
| Weaver_processor | 2 | Xbean_reflect | 59 |  |  |
| Webbeans_web | 92 | Xmlgraphics | 25 |  |  |
| Webpack | 152 | Yew | 35 |  |  |
| Wicket_cdi | 18 | Yii2 | 929 |  |  |
| Wicket_core | 1619 | YugabyteDB | 328 |  |  |
| Wicket_request | 151 |  |  |  |  |
| Wicket_spring | 35 |  |  |  |  |
| Wicket_util | 110 |  |  |  |  |

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
