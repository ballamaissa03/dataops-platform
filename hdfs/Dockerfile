FROM ubuntu:22.04
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
RUN apt-get update && apt-get install -y openjdk-11-jdk wget && rm -rf /var/lib/apt/lists/*
EXPOSE 9870 9000
CMD ["bash"]
