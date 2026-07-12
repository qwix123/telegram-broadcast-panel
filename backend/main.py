#!/usr/bin/env python3
import os
from app.main import app
import uvicorn

if __name__ == "__main__":
    host = os.getenv("BACKEND_HOST", "0.0.0.0")
    port = int(os.getenv("BACKEND_PORT", "8000"))
    debug = os.getenv("BACKEND_DEBUG", "false").lower() == "true"
    workers = int(os.getenv("BACKEND_WORKERS", "1"))
    
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=debug,
        workers=workers if not debug else 1,
        log_level="info",
    )