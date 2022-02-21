from fastapi import APIRouter

from src.api.v1_apis.schemas import Message

router = APIRouter(prefix='/sys', tags=['sys'])


@router.get('/health', response_model=Message)
def health_api():
    """ヘルスチェック用"""
    return {'message': 'Success!'}
