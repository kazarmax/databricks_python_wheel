from datetime import datetime
from pyspark.sql import SparkSession

from .config import raw_data_path
from .load_data import load_data
#from .process_data import process_data

def hello():
    print("Hello")

def main():


    # Initialize Spark session
    spark = (SparkSession
             .builder
             .appName("Databricks Python Wheel Project")
             .getOrCreate())

    # Load raw data in a dataframe
    df_raw = load_data(spark, raw_data_path)

   # Process data
   #df_processed = process_data(spark, df_raw, start_date, end_date)

   # Write cleaned data
   #df_cleaned = output_cleaned(spark, df_processed)


if __name__ == "__main__":
    main()