from typing import *
from pydantic import BaseModel


class Tweet(BaseModel):
    id: int
    user_id: int
    tweet_created_at: str
    datestamp: str
    timestamp: str
    timezone: str
    username: str
    name: str
    place: str
    content: str
    language: str
    mentions: List[dict]
    urls: List[str]
    photos: List[str]
    replies_count: int
    retweets_count: int
    likes_count: int
    hashtags: List[str]
    cashtags: List[str]
    link: str
    retweet: bool
    quote_url: str
    video: int
    thumbnail: str
    near: str
    geo: str
    source: str
    user_rt_id: str
    user_rt: str
    retweet_id: str
    reply_to: List[dict]
    retweet_date: str
