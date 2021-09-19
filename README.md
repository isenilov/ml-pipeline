# Basic yet complete Machine Learning pipeline for NLP tasks

This repository accompanies the article
(TODO: add link)
on building basic yet complete ML pipelines for solving NLP tasks.

## Requirements

[Docker](https://www.docker.com/)

[telnet](https://www.unix.com/man-page/linux/1/telnet/)

Please refer to installation instructions for your system if needed.

## Running the pipeline

### Running the pipeline

The whole pipeline of 4 services (mail server, database, prediction service and orchestrator) can be started with one command:

`docker-compose -f docker-compose.yaml up --build`

It should start printing log messages from the services.

### Sending an email

The pipeline is triggered by an unread email appearing in the mailbox. In order to send one, `telnet` util can be used.

Connecting to the IMAP mail server:
`telnet localhost 3025`

Sending the email with telnet:
```
EHLO user
MAIL FROM:<example@some-domain.com>
RCPT TO:<user>
DATA
Subject: Hello World
 
Hello!

She works at Apple now but before that she worked at Microsoft.
.
QUIT
```

If everything went well, something like this should appear in logs:
```
orchestrator_1                   | Polling mailbox...
prediction-worker_1              | INFO:     172.19.0.5:55294 - "POST /predict HTTP/1.1" 200 OK
orchestrator_1                   | Recoded to DB with id=34: [{'entity_text': 'Apple', 'start': 24, 'end': 29}, {'entity_text': 'Microsoft', 'start': 58, 'end': 67}]
```

### Checking the result

The data must also be recorded to the database.
In order to check that, any DB client can be used with the following connection parameters:
```
host: localhost
port: 5432
database: maildb
username: pguser
pasword: password
```

and running `SELECT * FROM mail LIMIT 10` query.