FROM alpine:latest

WORKDIR /var/www/blast

COPY . .

RUN apk update && \
    apk add apache2 \
    apache2-mod-wsgi \
    python3 \
    py3-pip \
    nodejs \
    npm \
    nfs-utils

RUN mkdir blastdb \
    queries \
    results

RUN mount -t nfs blastdb.biocloudlabs.es:/mnt/blastdb blastdb

RUN pip install -r requirements.txt

RUN cd static && \
    npm install && \
    npm run build 

RUN mv httpd.conf /etc/apache2/sites-available/httpd.conf

RUN a2dissite 000-default.conf
RUN a2enmod headers
RUN a2enmod ssl
RUN a2ensite httpd.conf

EXPOSE 443

CMD /usr/sbin/apache2ctl -D FOREGROUND








