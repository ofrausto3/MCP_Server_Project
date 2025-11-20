from pyspark.sql import SparkSession
from config import settings


class SparkClient:
    _spark = None

    @classmethod
    def get_spark(cls) -> SparkSession:
        if cls._spark is None:
            cls._spark = (
                SparkSession.builder
                .appName(settings.spark_app_name)
                .master(settings.spark_master)
                .getOrCreate()
            )
        return cls._spark
