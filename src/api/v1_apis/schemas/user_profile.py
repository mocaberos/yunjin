from typing import List
from pydantic import BaseModel


class UserProfile(BaseModel):
    id: str
    name: str
    user_name: str
    bio: str
    location: str
    url: str
    join_date: str
    join_time: str
    tweets: int
    following: int
    followers: int
    likes: int
    media_count: int
    is_private: bool
    is_verified: bool
    avatar: str
    background_image: str
