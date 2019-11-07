FROM ubuntu:16.04
MAINTAINER jeon95u@gmail.com

COPY server /server/

RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g' /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python python-pip
RUN pip install flask

EXPOSE 80

RUN chmod +x /server/run.sh
CMD /server/run.sh