from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')  # o el modelo que prefieras

class Texts(BaseModel):
    texts: list[str]

@app.post('/encode')
def encode(texts: Texts):
    embeddings = model.encode(texts.texts)
    return {'embeddings': embeddings.tolist()}
