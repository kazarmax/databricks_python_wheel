from pyspark.sql import DataFrame


def load_data(spark, file_path) -> DataFrame:
    """
    Load raw data Json file into a single DataFrame
    """
    df = spark.read.format("json") \
        .load(f"file:{file_path}") 

    return df
