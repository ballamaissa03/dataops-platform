FROM apache/airflow:2.7.0
USER airflow
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark pandas numpy
EXPOSE 8080
CMD ["airflow", "standalone"]
