import spacy as spacy
from fastapi import FastAPI
from typing import List, Dict

from model import PredictedEntity, Input

app = FastAPI()
nlp = spacy.load("en_core_web_sm")


@app.get("/health")
async def ping() -> Dict:
    """ Healthcheck endpoint """
    return {"status": "healthy"}


@app.post("/predict")
def predict(inp: Input) -> List[PredictedEntity]:
    """ Return embedding of a document given its body """

    # The code below is definitely not production-ready but rather quick implementation to show working server
    # In the real prod system it would make sense to implement batching

    doc = nlp(inp.mail_body)
    result = []
    for ent in doc.ents:
        if ent.label_ == "ORG":
            result.append({"entity_text": ent.text, "start": ent.start_char, "end": ent.end_char})
    return result
