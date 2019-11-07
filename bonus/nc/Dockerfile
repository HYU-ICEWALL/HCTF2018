FROM	ubuntu:16.04
MAINTAINER	kks26692@gmail.com

ENV user=nc

RUN useradd -m -d /home/$user/ -s /bin/bash $user
RUN echo "$user     hard    nproc   20" >> /etc/security/limits.conf

RUN apt-get update
RUN apt-get install -y xinetd python

COPY ./nc /home/$user/nc
COPY ./xinetd_conf /etc/xinetd.d/xinetd_conf

RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user

EXPOSE 1004

CMD ["/usr/sbin/xinetd", "-d"]