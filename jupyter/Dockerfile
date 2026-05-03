FROM jupyter/base-notebook:latest
USER root
RUN pip install --no-cache-dir pyspark==3.4.1 pandas numpy matplotlib seaborn scikit-learn
USER jovyan
WORKDIR /home/jovyan/work
EXPOSE 8888
CMD ["start-notebook.sh", "--NotebookApp.token=''"]
