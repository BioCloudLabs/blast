FROM debian:bullseye-slim

RUN apt-get update && \
    apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    openssl

RUN mkdir blastdb

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/biocloudlabs.key \
    -out /etc/ssl/certs/biocloudlabs.cer \
    -subj "CN=*.biocloudlabs.es"

COPY ./requirements.txt /var/www/blast/requirements.txt
RUN pip install -r /var/www/blast/requirements.txt

COPY ./httpd.conf /etc/apache2/sites-available/httpd.conf

COPY ./ /var/www/blast

RUN a2dissite 000-default.conf
RUN a2ensite httpd.conf
RUN a2enmod ssl

EXPOSE 443

WORKDIR /var/www/blast

CMD /usr/sbin/apache2ctl -D FOREGROUND








