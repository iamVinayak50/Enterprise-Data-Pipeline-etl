# Enterprise Data Pipeline ETL

![Project Banner](images/banner.png)

## Project Overview

**Enterprise Data Pipeline ETL** is an end-to-end data engineering solution built on **Google Cloud Platform (GCP)** and **Airflow**. The project automates the process of extracting data from multiple sources, transforming it, and loading it into analytics-ready storage, enabling **data-driven decision making**.  

This project demonstrates a **full ETL pipeline**, from raw data ingestion to transformation and final analytics-ready MySQL tables, including automation and CI/CD.

---

## Problem Statement

In many enterprises, data resides in **multiple sources** (APIs, GCS buckets, BigQuery projects). Manually extracting and transforming data is error-prone and time-consuming. The challenge was to:

1. **Extract** data from multiple heterogeneous sources.
2. **Transform** raw data into structured and analytics-ready format.
3. **Load** clean data into a **centralized warehouse** (BigQuery) and MySQL.
4. **Automate** the pipeline with **Airflow** and **CI/CD**.

---

## What Was Done

As a Data Engineer on this project, I implemented:

1. **Data Extraction**
   - Pulled data from **public APIs**.
   - Ingested files from **Google Cloud Storage**.
   - Queried data from **another BigQuery project**.

2. **Data Transformation**
   - Applied **cleaning**, **normalization**, and simple **business calculations**.
   - Converted raw JSON data into **pandas DataFrames** for processing.
   - Added **timestamps** and calculated derived fields for analytics.

3. **Data Loading**
   - Loaded transformed data into **BigQuery** tables for storage and analytics (Bronze/Silver layer).
   - Loaded final transformed data into **MySQL** (Gold layer) using **truncate & load** strategy.

4. **Pipeline Orchestration**
   - Created **Airflow DAGs** for each data source.
   - Designed the workflow: API/GCS/BQ → BigQuery → Transformation → MySQL.
   - Ensured tasks could run **daily** and handle retries on failure.

5. **CI/CD Automation**
   - Configured **Cloud Build** triggers for automatic deployment of DAGs to **Cloud Composer**.
   - Integrated **GitHub** with Cloud Build for version-controlled pipeline management.

---

## Architecture

![Architecture Diagram](images/architecture.png)

---

## Technologies Used

- **Python** (pandas, requests, SQLAlchemy) – ETL scripting & transformations  
- **Apache Airflow / Cloud Composer** – Pipeline orchestration  
- **Google BigQuery** – Data warehouse for raw and transformed data  
- **Google Cloud Storage (GCS)** – Raw data storage  
- **MySQL** – Final analytics database  
- **GitHub + Cloud Build** – CI/CD for DAG deployment  

---

## DAGs Overview

| DAG Name                  | Purpose                                             |
|----------------------------|---------------------------------------------------|
| `extract_api_to_bq`        | Extract from API → Load to BigQuery               |
| `extract_gcs_to_bq`        | Load raw JSON from GCS → BigQuery                 |
| `extract_bq_other_to_bq`   | Copy data from another BigQuery project → BQ      |
| `bq_to_mysql`              | Transform BQ data → Load into MySQL              |

---

## Folder Structure


---

## Setup Instructions

1. Clone the repository:



✅ This version clearly states:

- **What the project is**  
- **Problem it solves**  
- **What you did as a Data Engineer**  
- **Technologies and workflow**  
- **DAGs and CI/CD setup**  

---


