from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from typing import Optional

router = APIRouter()

class JokeResponse(BaseModel):
    joke: str
    type: str

@router.get("/random", response_model=JokeResponse)
async def get_random_joke():
    """Get a random joke"""
    try:
        async with httpx.AsyncClient() as client:
            # Try official-joke-api first
            response = await client.get(
                "https://official-joke-api.appspot.com/random_joke",
                timeout=10.0
            )
            response.raise_for_status()
            data = response.json()
            
            joke_text = f"{data.get('setup', '')} {data.get('punchline', '')}"
            return JokeResponse(
                joke=joke_text.strip(),
                type=data.get('type', 'general')
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch joke: {str(e)}")

@router.get("/by-type/{joke_type}")
async def get_joke_by_type(joke_type: str):
    """Get a joke by type (general, programming, knock-knock)"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://official-joke-api.appspot.com/jokes/{joke_type}/random",
                timeout=10.0
            )
            response.raise_for_status()
            data = response.json()
            
            if isinstance(data, list):
                data = data[0]
            
            joke_text = f"{data.get('setup', '')} {data.get('punchline', '')}"
            return JokeResponse(
                joke=joke_text.strip(),
                type=data.get('type', joke_type)
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch joke: {str(e)}")

@router.get("/types")
async def get_joke_types():
    """Get available joke types"""
    return {
        "types": [
            "general",
            "programming",
            "knock-knock"
        ]
    }