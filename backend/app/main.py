from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

# Import routers
from app.api.routes import auth, broadcast, chats, folders, proxy, jokes
from app.core.database import init_db

load_dotenv()

app = FastAPI(
    title="📱 Telegram Broadcast Panel",
    description="Веб-панель для управления Telegram рассылками",
    version="1.0.0"
)

# CORS Middleware
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
@app.on_event("startup")
async def startup():
    await init_db()

# Routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(broadcast.router, prefix="/api/broadcast", tags=["Broadcast"])
app.include_router(chats.router, prefix="/api/chats", tags=["Chats"])
app.include_router(folders.router, prefix="/api/folders", tags=["Folders"])
app.include_router(proxy.router, prefix="/api/proxy", tags=["Proxy"])
app.include_router(jokes.router, prefix="/api/jokes", tags=["Jokes"])

# Health check
@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/")
async def root():
    return {
        "message": "📱 Telegram Broadcast Panel API",
        "docs": "/docs",
        "version": "1.0.0"
    }

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )