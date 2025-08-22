from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import logging
from datetime import datetime
from typing import AsyncGenerator

from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Orionix AI Backend")
    
    # Initialize Redis connection pool
    app.state.redis = await aioredis.from_url(
        settings.REDIS_URL, encoding="utf-8", decode_responses=True
    )
    
    # Initialize database connection pool
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    app.state.async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    yield
    
    # Shutdown
    logger.info("Shutting down Orionix AI Backend")
    await app.state.redis.close()
    await engine.dispose()

# Create FastAPI app
app = FastAPI(
    title="Orionix AI API",
    description="Advanced AI Assistant Platform",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

# Dependency to get async database session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with app.state.async_session() as session:
        try:
            yield session
        finally:
            await session.close()

# Dependency to get Redis connection
async def get_redis():
    return app.state.redis

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
