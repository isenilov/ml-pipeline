FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install spacy==3.1.2 && \
    python -m spacy download en_core_web_sm && \
    apt-get update && \
    apt-get install -y jq && \
    apt-get clean

EXPOSE 1390

COPY server.py model.py /app/

HEALTHCHECK --interval=60s --timeout=1s CMD curl -s http://localhost:1390/health | jq -e '.status=="healthy"'

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "1390"]
