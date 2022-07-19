from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

INPUT_PATH = 'data/input/records.json'

OUTPUT_PATH_ITEMS = 'data/output/items/'
OUTPUT_PATH_NFE = 'data/output/nfe/'

class NfeExpand():
    def __init__(self, spark):
        self.spark = spark
        
    def expand(self, df):
        '''Expand items in the dataframe'''
        return df.withColumn('items', explode('ItemList'))\
            .withColumn('ProductName', col('items.ProductName'))\
            .withColumn('Value', col('items.Value'))\
            .withColumn('Quantity', col('items.Quantity'))

    def run(self):
        '''Save the expanded dataset and split it into a relational model'''
        df = spark.read.option("multiline", "true").json(INPUT_PATH)

        df_expanded = self.expand(df)
        
        df_nfe = df.select('CreateDate', 'Discount', 'EmissionDate', 'NFeID', 'NFeNumber')
        
        df_items = df_expanded.select('NFeID', 'ProductName', 'Value', 'Quantity')
        
        df_nfe.coalesce(1).write.mode('overwrite').parquet(OUTPUT_PATH_NFE)
        df_items.coalesce(1).write.mode('overwrite').parquet(OUTPUT_PATH_ITEMS)
        

if __name__ == '__main__':
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("test_app") \
        .getOrCreate()

    expand = NfeExpand(spark)
    expand.run()