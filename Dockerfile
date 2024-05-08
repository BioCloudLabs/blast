FROM alpine:latest

WORKDIR /var/www/blast

COPY . .

RUN apk update && \
    apk add --no-cache \
        apache2 \
        apache2-mod-wsgi \
        python3 \
        py3-pip \
        nodejs \
        npm \
        nfs-utils && \
    rm -rf /var/cache/apk/* && \
    mkdir blastdb queries results && \
    mount -t nfs 4.233.220.168:/mnt/blastdb blastdb && \
    pip install --no-cache-dir -r requirements.txt && \
    npm install --prefix static && \
    npm run build --prefix static && \
    mv httpd.conf /etc/apache2/sites-available/httpd.conf && \
    a2dissite 000-default.conf && \
    a2enmod headers && \
    a2enmod ssl && \
    a2ensite httpd.conf

EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]








