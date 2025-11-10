from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

# Step 1: Initialize Spark Session
spark = SparkSession.builder \
    .appName("JLR_Service_ETL") \
    .getOrCreate()

# Step 2: Read service data CSV from GCS
gcs_path = "gs://jlr-service-data/raw/*.csv"
service_df = spark.read.option("header", "true").csv(gcs_path)

# Step 3: Basic Cleaning
clean_df = (
    service_df.dropna()  # Remove rows with nulls
    .withColumn("service_center", trim(col("service_center")))
    .withColumn("vehicle_model", trim(col("vehicle_model")))
)

# Step 4: Read CLM data from BigQuery (for enrichment)
clm_df = spark.read.format("bigquery").option("table", "boxwood-axon-470816-b1.jlr_dataset.clm_campaign_data").load()

# Step 5: Join Service + CLM data
final_df = clean_df.join(clm_df, on="vehicle_id", how="left")

# Step 6: Write cleaned data to BigQuery
final_df.write.format("bigquery") \
    .option("table", "boxwood-axon-470816-b1.jlr_dataset.service_cleaned_data") \
    .mode("overwrite") \
    .save()

# Step 7: Stop Spark
spark.stop()
