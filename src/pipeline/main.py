from datetime import datetime
from pyspark.sql import SparkSession
from .config import raw_data_path
from .load_data import load_data
from .transform_data import transform_data
from .write_data import merge_delta_table

def hello():
    print("Hello3")


def main():
    # Initialize Spark session
    spark = (SparkSession
             .builder
             .appName("Databricks Python Wheel Project")
             .getOrCreate())

    # Load raw data in a dataframe
    df_raw = load_data(spark, raw_data_path)

    # Transform raw data
    df_transformed = transform_data(df_raw)

    # Write transformed data
    merge_delta_table(  spark = spark, 
                        df = df_transformed,
                        table_name = "adzuna_jobs", 
                        join_keys = ["job_id"],
                        partition_by_key = "job_created_date"
                      )


if __name__ == "__main__":
    main()