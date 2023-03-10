FROM python:3.10
RUN mkdir /otree
WORKDIR /otree
RUN pip install \
    otree \
    psycopg2 
CMD ["sh", "-c", "sleep 10; otree prodserver1of2 0.0.0.0:8000 & sleep 10; otree prodserver2of2"]