FROM python:3.10-alpine

WORKDIR /app

RUN mkdir queries blastdb \
    && apk add nfs-utils \
    && mount -t nfs blastdb.biocloudlabs.es:/mnt/blastdb /app/blastdb

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]