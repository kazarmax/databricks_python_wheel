from pyspark.sql import DataFrame
from pyspark.sql.functions import col, explode, current_timestamp, to_date


def transform_data(df_raw: DataFrame) -> DataFrame:
    """
    Transforms raw json data from df_raw
    """
    df = df_raw.withColumn("item", explode("items")) \
    .select(
        col("item.id").alias("job_id"),
        col("item.title").alias("job_title"),
        col("item.location.display_name").alias("job_location"),
        col("item.company.display_name").alias("company_name"),
        col("item.category.label").alias("job_category"),
        col("item.description").alias("job_description"),
        col("item.redirect_url").alias("job_url"),
        col("item.created").alias("job_created") ) \
    .withColumn("job_created", col("job_created").cast("timestamp")) \
    .withColumn("job_created_date", to_date("job_created")) \
    .withColumn("elt_updated", current_timestamp()) \
    .dropDuplicates(["job_id"])

    return df