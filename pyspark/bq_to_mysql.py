from pyspark.sql import SparkSession

# ------------------------------
# 1. Start Spark Session
# ------------------------------
spark = SparkSession.builder \
    .appName("BQ-to-MySQL-JDBC") \
    .config(
        "spark.jars.packages",
        "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.30.1,"
        "mysql:mysql-connector-java:8.0.33"
    ) \
    .getOrCreate()

# ------------------------------
# 2. BigQuery details
# ------------------------------
bq_project = "boxwood-axon-470816-b1"
bq_dataset = "gold"
materialize_dataset = "temp_materialize"

# TABLE MAPPING
tables = {
    "car_part_summary": "car_part_summary",
    "plant_summary": "plant_summary"
    
}

# ------------------------------
# 3. MySQL JDBC connection
# ------------------------------
mysql_url = "jdbc:mysql://10.36.96.4:3306/prod-test"

mysql_properties = {
    "user": "prod",
    "password": "prod",
    "driver": "com.mysql.cj.jdbc.Driver",
}

# ------------------------------
# 4. Loop through tables
# ------------------------------
for bq_table, mysql_table in tables.items():

    print(f"\nProcessing {bq_table} → {mysql_table}")

    # --- 4.1 Read BigQuery ---
    df = (
        spark.read.format("bigquery")
        .option("project", bq_project)
        .option("dataset", bq_dataset)
        .option("table", bq_table)
        .option("viewsEnabled", "true")
        .option("materializationDataset", materialize_dataset)
        .load()
    )

    # --- 4.2 Increase parallelism ---
    df = df.repartition(16)

    # --- 4.3 Write into MySQL with optimization ---
    df.write \
        .format("jdbc") \
        .option("url", mysql_url) \
        .option("dbtable", mysql_table) \
        .option("user", mysql_properties["user"]) \
        .option("password", mysql_properties["password"]) \
        .option("driver", mysql_properties["driver"]) \
        .option("batchsize", 20000) \
        .option("truncate", "true") \
        .option("isolationLevel", "NONE") \
        .option("rewriteBatchedStatements", "true") \
        .mode("overwrite") \
        .save()

    print(f"Loaded successfully into {mysql_table} ✔")

# ------------------------------
# 5. Stop Spark
# ------------------------------
spark.stop()
