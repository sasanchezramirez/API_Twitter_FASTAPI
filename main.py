from fastapi import FastAPI

app = FastAPI()

@app.get(
    path="/"
)
def home():
    return {"twitter_APi" : "it works"}