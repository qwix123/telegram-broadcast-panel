from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.core.security import create_access_token, get_password_hash, verify_password
from app.core.telegram_client import telegram_manager
from datetime import timedelta

router = APIRouter()

class PhoneRequest(BaseModel):
    phone_number: str

class CodeRequest(BaseModel):
    phone_number: str
    code: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    first_name: str

@router.post("/request-code")
async def request_code(request: PhoneRequest):
    """Request authentication code"""
    try:
        await telegram_manager.initialize(request.phone_number)
        result = await telegram_manager.send_code_request(request.phone_number)
        return {
            "status": "success",
            "message": "Code sent successfully",
            "phone_code_hash": result.phone_code_hash
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=LoginResponse)
async def login(request: CodeRequest):
    """Login with phone and code"""
    try:
        await telegram_manager.sign_in(request.phone_number, request.code)
        user = await telegram_manager.get_me()
        
        access_token = create_access_token(
            data={"user_id": user.id, "phone": request.phone_number},
            expires_delta=timedelta(days=7)
        )
        
        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
            user_id=user.id,
            first_name=user.first_name or "User"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/logout")
async def logout():
    """Logout and disconnect"""
    try:
        await telegram_manager.disconnect()
        return {"status": "success", "message": "Logged out successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))