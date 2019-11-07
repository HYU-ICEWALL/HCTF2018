FROM       ubuntu:16.04
MAINTAINER kks26692@gmail.com

# Environment
ENV user=bf

# add user && config
RUN useradd -m -d /home/$user/ -s /bin/bash $user
RUN echo "$user     hard    nproc   20" >> /etc/security/limits.conf

# update && install xinetd
RUN apt-get update
RUN apt-get install -y xinetd python

# COPY
COPY ./bf /home/$user/bf
COPY ./xinetd_conf /etc/xinetd.d/xinetd_conf

# apply permissions
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user

# EXPOSE
EXPOSE 1002

# CMD
CMD ["/usr/sbin/xinetd", "-d"]