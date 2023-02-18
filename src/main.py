from fastapi import FastAPI

from predict import predict


app = FastAPI()


@app.post("/story_generator")
def generate_story(keywords: str, sep=','):
    return predict(keywords, sep)
