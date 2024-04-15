FROM python:3.10-alpine

WORKDIR /app

RUN mkdir queries blastdb \
    && apk add cifs-utils psmisc \
    && mount -t cifs //blastdb.biocloudlabs.es/blastdb /app/blastdb -o guest

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]