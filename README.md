# 🚗 Campaign Lifecycle Management ETL Project

## 📌 Project Overview
- **Project Name:** Campaign Lifecycle Management ETL  
- **Client:**  
- **Objective:** Extract, transform, and load multi-source data into **BigQuery gold tables** and **MySQL** for analytics.  
- **Tech Stack:**  
  - ☁️ **Cloud:** GCP (BigQuery, Dataproc, Composer, Secret Manager, Cloud Logging & Monitoring)  
  - 🛠 **ETL:** Dataform, PySpark  
  - 🔄 **Orchestration:** Airflow DAGs  
  - 🔧 **CI/CD:** GitHub + Cloud Build  

---

## 🗂 Phase 1 – Ingestion
- Raw sources: SAP, Vista, IQM, CSV files  
-  

---

## 🗂 Phase 2 – Airflow Setup & DAGs
- DAGs:  
  1. **Dataform DAG** – transforms staging → gold  
  2. **Dataproc DAG** – executes PySpark job → MySQL  
  3. **Orchestration DAG** – triggers DAGs in sequence  
- Connections: Airflow Admin Connections for BigQuery, Dataproc, MySQL  
- Scheduling: Daily at 12 PM  
- Monitoring: Airflow UI, task logs  

---

## 🗂 Phase 3 – Staging & Transformation
- Staging tables: Raw CSV/API → BigQuery staging  
- Gold tables: Dimension & fact tables  
- Dataform: Handles `stg → gold` transformations  
- Assertions: Ensure uniqueness, completeness, referential integrity  

---

## 🗂 Phase 4 – PySpark ETL
- Reads gold tables from BigQuery  
- Repartitions for parallelism & batch optimization  
- Writes into **star schema** tables in MySQL (`fact_sales`, `dim_car`, `dim_dealer`)  

---

## 🗂 Phase 5 – Orchestration & Dependency
- DAG Flow:  
- Handles **retries & SLA**  
- Email alerts on failures  

---

## 🗂 Phase 6 – CI/CD & Git
- Branches: `main`, `dev`, `feature/*`  
- Pipeline: Cloud Build / GitHub Actions  
- Installs dependencies  
- Runs unit tests & Dataform assertions  
- Deploys DAGs to Composer  

---

## 🗂 Phase 7 – Data Security & Compliance
- IAM roles: Least privilege  
- Secret Manager: MySQL credentials  
- Encryption: BigQuery & GCS at rest, SSL for MySQL  
- Audit logging: Cloud Logging & Airflow logs  
- Data masking: Hash PII (e.g., `CUSTOMER_NAME`)  

---

## 🗂 Phase 8 – Data Modeling & Star Schema
### Fact Tables
| Table | Measures | Description |
|-------|----------|------------|
| `fact_sales` | PRICE, SALE_DATE | Sales metrics |
| `fact_service` | COST, SERVICE_DATE | Service metrics |

### Dimension Tables
| Table | Attributes |
|-------|------------|
| `dim_car` | CAR_ID, MODEL, VARIANT, ENGINE_TYPE, PLANT, MANUFACTURE_DATE |
| `dim_part` | PART_ID, PART_NAME, CAR_ID, SUPPLIER, COST, UPDATED_DATE |
| `dim_dealer` | DEALER_ID, DEALER_NAME, COUNTRY, CITY, CONTACT |
| `dim_service` | SERVICE_ID, CAR_ID, SERVICE_TYPE, SERVICE_CENTER, SERVICE_DATE, COST |

- Partition fact tables by date for performance  
- Handle Slowly Changing Dimensions (SCD)  

---

## 🗂 Phase 9 – Monitoring & Observability
- Airflow UI: DAG & task execution, retries, SLA alerts  
- Cloud Logging: Aggregated logs  
- Cloud Monitoring: Metrics & alerts  
- Data Quality Checks:  
- ✅ Completeness  
- ✅ Uniqueness  
- ✅ Referential integrity  
- ✅ Range & format validation  
- ✅ Duplicate detection  

---

## 🗂 Phase 10 – Documentation 

### Architecture Diagram
Raw Data (CSV/API) 📥
│
▼
GCS / BigQuery Staging (Dataform) 🏗
│
▼
Gold Tables in BigQuery (Star Schema) ⭐
│
▼
Dataproc PySpark 🔥
│
▼
MySQL (Analytics / BI) 💾


