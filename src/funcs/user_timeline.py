from typing import *

import twint
from .formatter import __format_tweet


def user_timeline(user_id: str, since: str, until: str) -> List[dict]:
    """
    特定のユーザーが特定の期間内にツイートした内容を取得する。
    一度に取得できる上限があるため、該当ユーザーの全てのツイートを取得したい場合は、日付を変更しながら少しずつ取得すること
    :param user_id: ユーザーID
    :param since: 開始時間、例: `2020-01-01`
    :param until: 終了時間、例: `2020-01-31`
    :return: ツイートリスト
    """
    tweets = []
    config = twint.Config()
    config.User_id = user_id
    config.Hide_output = True
    config.Store_object = True
    config.Since = since
    config.Until = until
    config.Store_object_tweets_list = tweets
    twint.run.Search(config)
    return list(filter(lambda x: x is not None, [__format_tweet(tweet, user_id=user_id) for tweet in tweets]))
