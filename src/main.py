from fastapi import FastAPI
from src.routes import website_info
import uvicorn

app = FastAPI(title="AI Website Info")
app.include_router(website_info.router, prefix="/api", tags=["Website Info"])


