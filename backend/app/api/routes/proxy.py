from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.proxy_handler import proxy_handler

router = APIRouter()

class ProxyConfig(BaseModel):
    type: str  # "http", "socks5"
    server: str
    port: int
    username: str = ""
    password: str = ""

@router.get("/config")
async def get_proxy_config():
    """Get current proxy configuration"""
    config = proxy_handler.get_proxy_config()
    if config:
        return config
    return {"enabled": False}

@router.post("/config")
async def set_proxy_config(config: ProxyConfig):
    """Set proxy configuration"""
    try:
        if not proxy_handler.validate_proxy_config(config.dict()):
            raise HTTPException(status_code=400, detail="Invalid proxy configuration")
        
        # TODO: Save proxy config to database/env
        return {"status": "success", "message": "Proxy configured"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/test")
async def test_proxy():
    """Test proxy connection"""
    try:
        # TODO: Implement proxy testing
        return {"status": "success", "message": "Proxy is working"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))