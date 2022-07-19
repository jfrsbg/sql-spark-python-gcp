from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sparkSum, round as sparkRound

INPUT_PATH = 'data/input/input.json'

OUTPUT_PATH = 'data/output/'

class CalculateTotal():
    def __init__(self, spark):
        self.spark = spark


    def run(self):
        df = spark.read.option("multiline", "true").json(INPUT_PATH)

        df = df.withColumn('desconto_percentual', col('desconto_percentual').cast('double'))\
            .na.fill(0)\
            .withColumn('total_liquido', col('total_bruto') - (col('total_bruto') * col('desconto_percentual') / 100))\
            .agg(sparkRound(sparkSum('total_liquido'), 2).alias('total_liquido'))

        df.coalesce(1).write.mode('overwrite').parquet(OUTPUT_PATH)

if __name__ == '__main__':
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("test_app") \
        .getOrCreate()

    calculate_total = CalculateTotal(spark)
    calculate_total.run()