from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, col

spark = SparkSession.builder \
    .appName("AnalyseQualiteAirSenegal") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("=== Chargement des données ===")
df = spark.read.csv("/data/qualite_air_senegal.csv", header=True, inferSchema=True)
df.show()

print("=== Statistiques par ville ===")
stats = df.groupBy("ville").agg(
    avg("pm25").alias("pm25_moyen"),
    max("pm25").alias("pm25_max"),
    avg("pm10").alias("pm10_moyen"),
    avg("no2").alias("no2_moyen")
).orderBy("pm25_moyen", ascending=False)
stats.show()

print("=== Jours critiques (PM2.5 > 50) ===")
critique = df.filter(col("pm25") > 50).select("date", "ville", "pm25")
critique.show()

print("=== Analyse terminée ===")
spark.stop()
