FROM python:3.10-alpine

WORKDIR /app

RUN mkdir queries blastdb \
&& curl -O ftp://ftp.ncbi.nih.gov/blast/db/pdbaa.tar.gz \
&& curl -O ftp://ftp.ncbi.nih.gov/blast/db/pdbnt.tar.gz \
&& tar -zxvf pdbaa.tar.gz -C blastdb \
&& tar -zxvf pdbnt.tar.gz -C blastdb

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

COPY . /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]