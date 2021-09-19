FROM python:3.8

RUN pip install imap-tools==0.47.0 requests==2.26.0 psycopg2==2.9.1

COPY main.py /app/

WORKDIR /app/

CMD ["python", "-u", "main.py"]
