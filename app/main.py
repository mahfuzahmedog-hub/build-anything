"""Build Anything — FastAPI web application."""

import os
from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine
from app.routes import items


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Build Anything", version="0.1.0", lifespan=lifespan)

START_TIME = datetime.now(UTC)

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(items.router)


@app.get("/")
async def index():
    return FileResponse(os.path.join(static_dir, "index.html"))


@app.get("/dashboard")
async def dashboard():
    return FileResponse(os.path.join(static_dir, "dashboard.html"))


@app.get("/api/status")
async def status():
    uptime = (datetime.now(UTC) - START_TIME).total_seconds()
    return {"status": "ok", "uptime_seconds": round(uptime, 1)}
