from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Kapil').master('local').getOrCreate()
df = spark.createDataFrame([(1, 'One'), (2, 'Two')], ['col1', 'col2'])
df.show()
spark.stop()
