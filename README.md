
## 🛠 Project: End-to-End ETL Pipeline using Dataform, Dataflow & Airflow

## Event-driven & Scheduled ETL Pipeline on Google Cloud

This project implements a **complete ETL workflow** where:

1. Raw data from **BigQuery (multiple projects)** is transformed via **Dataform** (Bronze → Silver → Gold).  
2. Processed data is then loaded into **MySQL** using **Dataflow (Apache Beam)** pipelines.  
3. The **Airflow DAG** orchestrates the workflow daily, monitors logs, and sends email notifications.  

![flow-diagram](flow-diagram.png)

---

### 🗂 Project Structure


## 📁 Project Structure

```text
gcp_data_engineering_project/
│
├── dataform/                        # Dataform ETL repository
│   ├── definitions/                 # SQLX scripts for transformations
│   │   ├── bronze/                  # 🔹 Raw → Bronze layer transformations (initial cleaning)
│   │   ├── silver/                  # 🔹 Bronze → Silver layer (enriched/processed)
│   │   ├── gold/                    # 🔹 Silver → Gold layer (business-ready tables)
│   │   └── final/                   # 🔹 Optional final aggregated views
│   ├── includes/                    # 🔹 Reusable macros/functions for SQL transformations
│   ├── workflow_settings.yaml       # 🔹 Workflow dependencies & task order
│   ├── dataform.json                # 🔹 Project configuration (warehouse, schema)
│   └── package.json                 # 🔹 Node.js dependencies for Dataform CLI
│
├── dataflow/                         # Dataflow / Apache Beam pipelines
│   ├── config/
│   │   └── tables_config.py         # 📋 BigQuery → MySQL table mapping, primary keys, load type
│   ├── utils/
│   │   ├── secret_manager.py        # 🔐 Fetch secrets from GCP Secret Manager
│   │   └── mysql_utils.py           # 🐬 MySQL connection & SCD1 upsert functions
│   └── bq_to_mysql_scd1.py          # 🌊 Main Dataflow pipeline script
│
├── airflow/                          # Airflow DAGs for orchestration
│   └── dags/
│       └── etl_gold_to_mysql.py     # 🕑 DAG triggers Dataform + Dataflow pipelines with email notifications
│
├── cloudbuild.yaml                   # ☁️ Cloud Build CI/CD config for automated deployment
├── requirements.txt                  # 📦 Python dependencies (apache-beam, mysql-connector, airflow)
└── README.md                         # 📝 Project overview & instructions






---

### ✅ Prerequisites

- Python 3.8+  
- Google Cloud SDK installed (`gcloud init`)  
- Google Cloud project with billing enabled  
- Enable the following APIs:
  - Dataform API  
  - Dataflow API  
  - BigQuery API  
  - Secret Manager API  
  - Cloud Composer (Airflow) API  
- MySQL instance available to load data  
- Optional: Cloud Build for CI/CD automation  

---

### ✅ Use Case

- Transform raw BigQuery tables across projects via **Dataform** (Bronze → Silver → Gold)  
- Perform **SCD Type 1** incremental updates to MySQL  
- Schedule pipelines **daily at 12 AM** via **Airflow**  
- Monitor pipeline execution, send email notifications, and maintain logs  

---

### 🔧 Setup Instructions

#### 1️⃣ Clone Repository

```bash
git clone https://github.com/iamVinayak50/Enterprise-Data-Pipeline-etl.git
cd gcp_data_engineering_project



### 👨‍💻 Author

Hi, my name is **Vinayak Shegar**.  
I am a **GCP Data Engineer** with 4 years of experience in building **scalable ETL pipelines** using **Dataform, Dataflow, Airflow, BigQuery, and MySQL**.  

You can reach me via email or connect with me on LinkedIn to discuss GCP data engineering projects, best practices, or collaborations! 🚀  

![Coding GIF](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

