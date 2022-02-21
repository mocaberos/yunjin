from fastapi import APIRouter

from .endpoints import health_router, twitter_router

v1_api_router = APIRouter(prefix='/v1')
v1_api_router.include_router(health_router)
v1_api_router.include_router(twitter_router)
