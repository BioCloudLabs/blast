FROM debian:bullseye-slim

RUN apt-get update && \
    apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    npm \
    wget

RUN wget -O- https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

COPY ./ /var/www/blast

RUN pip install -r /var/www/blast/requirements.txt

RUN cd /var/www/blast/static && \
    npm install && \
    npm audit fix --force && \
    npm run build 


RUN mv /var/www/blast/httpd.conf /etc/apache2/sites-available/httpd.conf

RUN a2dissite 000-default.conf
RUN a2enmod headers
RUN a2enmod ssl
RUN a2ensite httpd.conf

EXPOSE 443

WORKDIR /var/www/blast

CMD /usr/sbin/apache2ctl -D FOREGROUND








