FROM ubuntu:16.04
MAINTAINER kks26692@gmail.com

RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g' /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y python python-pip
RUN pip install flask

COPY server /server/

EXPOSE 80

RUN chmod +x /server/run.sh
CMD /server/run.sh