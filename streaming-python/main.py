from fastapi import FastAPI
from jokes import router as jokes

app = FastAPI()

app.include_router(jokes)

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}