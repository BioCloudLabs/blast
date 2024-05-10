FROM alpine:latest

WORKDIR /var/www/app

COPY . .

RUN apk update && \
    apk add --no-cache \
        apache2 \
        apache2-mod-wsgi \
        python3 \
        py3-pip \
        nodejs \
        npm \
        cifs-utils && \
    rm -rf /var/cache/apk/* && \
    mkdir blastdb queries results && \
    mount -t cifs //blastdb.biocloudlabs.es/blastdb blastdb/ && \
    pip install --no-cache-dir -r requirements.txt && \
    npm install --prefix static && \
    npm run build --prefix static && \
    mv httpd.conf /etc/apache2/sites-available/httpd.conf && \
    a2dissite 000-default.conf && \
    a2enmod ssl && \
    a2ensite httpd.conf

EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]








