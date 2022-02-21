from typing import List
from pydantic import BaseModel
from .tweet import Tweet


class Tweets(BaseModel):
    tweets: List[Tweet]
