from typing import *
from fastapi import APIRouter, Query

from src.api.v1_apis.schemas import Tweets, UserProfile, UserID, UserName
from src.funcs import search_tweets, get_user_profile, name_to_id, id_to_name, user_timeline

router = APIRouter(prefix='/twitter', tags=['twitter'])


@router.get('/search-tweets', response_model=Tweets)
def search_tweets_api(query: str, since: Optional[str] = None, until: Optional[str] = None, limit: int = 10):
    """ツイート検索機能(スクレイピング)"""
    tweets = search_tweets(
        query,
        since=since,
        until=until,
        limit=limit
    )
    return {'tweets': tweets}


@router.get('/user-profile/user_id/{user_id}', response_model=UserProfile)
def get_user_profile_by_id_api(user_id: str):
    """ユーザーIDによる、ユーザープロフィール情報取得"""
    return get_user_profile(user_id=user_id)


@router.get('/user-profile/user_name/{user_name}', response_model=UserProfile)
def get_user_profile_by_name_api(user_name: str):
    """ユーザー名による、ユーザープロフィール情報取得"""
    return get_user_profile(user_name=user_name)


@router.get('/name-to-id/{user_name}', response_model=UserID)
def name_to_id_api(user_name: str):
    """ユーザー名をユーザーIDに変換する(キャッシュ付き)"""
    return {'user_id': name_to_id(user_name)}


@router.get('/id-to-name/{user_id}', response_model=UserName)
def id_to_name_api(user_id: str):
    """ユーザーIDをユーザー名に変換する(キャッシュ付き)"""
    return {'user_name': id_to_name(user_id)}


@router.get('/user-timeline', response_model=Tweets)
def user_timeline_api(
        user_id: str,
        since: str = Query(None, regex='[1-2]\d\d\d-\d\d-\d\d'),
        until: str = Query(None, regex='[1-2]\d\d\d-\d\d-\d\d')
):
    """
    特定のユーザーのツイートを取得する、
    一度に取得できる上限があるため、該当ユーザーの全てのツイートを取得した場合は、日付を変更しながら少しずつ取得すること。
    アクセスレートに注意。
    """
    return {'tweets': user_timeline(user_id, since, until)}
