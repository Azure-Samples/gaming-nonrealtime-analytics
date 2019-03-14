# Databricks notebook source

dbutils.widgets.text("year", "2019", "Year")
dbutils.widgets.text("month", "03", "Month")
dbutils.widgets.text("day", "01", "Day")

# COMMAND ----------

y = dbutils.widgets.get("year")
m = dbutils.widgets.get("month")
d = dbutils.widgets.get("day")

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

dbutils.fs.ls("wasbs://ehcapture-analytics@storagenrtanalytics.blob.core.windows.net/ehnrtanalytics/ehnrtanalytics-output/1/2019/03/04/20/53")

# COMMAND ----------

# Path format: partition/year/month/day/hour/minute/
input_loc = "wasbs://ehcapture-analytics@storagenrtanalytics.blob.core.windows.net/ehnrtanalytics/ehnrtanalytics-output/*/{}/{}/{}/*/*/".format(y, m, d)


# COMMAND ----------

df = spark.read.format("avro").load(input_loc)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.count()

# COMMAND ----------

df2 = df.select(df.Body.cast('string'))

# COMMAND ----------

display(df2)

# COMMAND ----------

df2.write.json('wasbs://ehcapture-analytics@storagenrtanalytics.blob.core.windows.net/temp_out/', mode="overwrite")

# COMMAND ----------

dbutils.fs.ls("wasbs://ehcapture-analytics@storagenrtanalytics.blob.core.windows.net/temp_out/")

# COMMAND ----------

dfjs = spark.read.json("wasbs://ehcapture-analytics@storagenrtanalytics.blob.core.windows.net/temp_out/") 

# COMMAND ----------

schema = StructType([StructField("version", StringType()), StructField("userid", StringType()), StructField("platform", StringType())])
dfx = dfjs.select(from_json("Body", schema).alias("B"))

# COMMAND ----------

display(dfx)

# COMMAND ----------

dfx2 = dfx.select("B.*")

# COMMAND ----------

display(dfx2)

# COMMAND ----------

display(dfx2.groupBy("platform").count())

# COMMAND ----------

out_loc = "wasbs://ehcapture-analytics@storagenrtanalytics.blob.core.windows.net/csv_out/{}/{}/{}".format(year, month, day)
dfx2.write.csv(out_loc, header=True, mode="overwrite")

# COMMAND ----------


