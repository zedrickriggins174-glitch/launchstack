"""
FastAPI application with Clerk authentication, Supabase database, and Redis cache.

Deploy to Railway in one click — all services are pre-configured.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import health, items

app = FastAPI(
      title=settings.app_name,
      description="FastAPI starter with Clerk Auth, Supabase, and Redis on Railway",
      version="1.0.0",
)

# -- CORS --
# TODO: Replace "*" with your frontend domain(s) before going to production.
# Example: ["https://myapp.com", "http://localhost:3000"]
app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)

# -- Routes --
app.include_router(health.router)
app.include_router(items.router, prefix="/api/v1")
