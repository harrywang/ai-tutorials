import asyncio
from fastapi import FastAPI, Request
from sse_starlette import EventSourceResponse
from fastapi import APIRouter

router = APIRouter()

@router.get("/jokes")
async def jokes(request: Request):
    async def get_messages():
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
        ]
        for joke in jokes:
            yield f"{joke}"
            await asyncio.sleep(2)

    return EventSourceResponse(get_messages())