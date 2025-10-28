from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder \
    .appName("KafkaSparkStreamingCarEval") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType() \
    .add("buying", StringType()) \
    .add("maint", StringType()) \
    .add("doors", StringType()) \
    .add("persons", StringType()) \
    .add("lug_boot", StringType()) \
    .add("safety", StringType()) \
    .add("class", StringType())

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "car-evaluations") \
    .load()

df_parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

df_count = df_parsed.groupBy("class").count()

query = df_count.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
