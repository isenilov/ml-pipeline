import json
import time

import psycopg2 as psycopg2
import requests
from imap_tools import AND, MailBoxUnencrypted

sql = """INSERT INTO mail (subject, body, labels) VALUES (%s, %s, %s) RETURNING id;"""

time.sleep(10)

mb = MailBoxUnencrypted(host="mail", port=3143).login("user", "pass")

with psycopg2.connect(
        host="db",
        database="maildb",
        user="pguser",
        password="password") as conn:
    while True:
        print("Polling mailbox...")
        time.sleep(5)
        messages = mb.fetch(criteria=AND(seen=False),
                            mark_seen=True,
                            bulk=True)
        for msg in messages:
            labels = requests.post("http://prediction-worker:1390/predict", json={"mail_body": msg.text})
            cur = conn.cursor()
            cur.execute(sql, (msg.subject, msg.text, json.dumps(labels.json())))
            id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            print(f"Recorded to DB with id={id}: {labels.json()}")
