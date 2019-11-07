FROM ubuntu:16.04
MAINTAINER jeon95u@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g' /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN apt-get -qq -y install git curl build-essential

RUN apt-get -qq -y install apache2
RUN apt-get -qq -y install php
RUN echo "mysql-server mysql-server/root_password password jeong.su" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password jeong.su" | debconf-set-selections
RUN apt-get -qq -y install mysql-server
RUN apt-get -qq -y install libapache2-mod-php
RUN apt-get -qq -y install php-mysql

COPY html /var/www/html
RUN rm -r /var/www/html/index.html

EXPOSE 80

COPY init.sql /init.sql
COPY run.sh /run.sh
RUN chmod +x /run.sh
CMD /run.sh