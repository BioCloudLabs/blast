FROM debian:bullseye-slim

RUN apt-get update && \
    apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip

RUN mkdir blastdb

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








