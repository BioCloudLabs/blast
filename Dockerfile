FROM debian:bullseye-slim

WORKDIR /var/www/app

COPY . .

RUN apt-get update && \
    apt-get install -y \
        apache2 \
        libapache2-mod-wsgi-py3 \
        python3 \
        python3-pip \
        npm \
        wget && \
    wget -O- https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/cache/apt/* && \
    mkdir blastdb queries results && \
    pip install --no-cache-dir -r requirements.txt && \
    npm install --prefix static && \
    npm run build --prefix static && \
    mv httpd.conf /etc/apache2/sites-available/httpd.conf && \
    a2dissite 000-default.conf && \
    a2enmod ssl && \
    a2ensite httpd.conf

EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]








