FROM apache/spark:3.4.1
USER root
RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*
RUN pip3 install pandas numpy pyspark==3.4.1
WORKDIR /opt/spark-apps
EXPOSE 8080 7077 4040
CMD ["/opt/spark/bin/spark-class", "org.apache.spark.deploy.master.Master"]
