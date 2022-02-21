from typing import *
import twint

from .formatter import __format_tweet


def search_tweets(
        query: str,
        since: Optional[str] = None,
        until: Optional[str] = None,
        limit: int = 1024
) -> List[Dict]:
    """
    指定のキーワードでツイートの検索を行う。
    :param query: 検索キーワード
    :param since: 検索開始日付 例: `2020-01-01`
    :param until: 検索終了日付 例: `2020-01-31`
    :param limit: 取得数制限 (厳密に制限される訳ではない)
    :return: 検索で見つけたツイート情報。
    """
    tweets = []
    config = twint.Config()
    config.Hide_output = True
    config.Store_object = True
    config.Since = since
    config.Until = until
    config.Store_object_tweets_list = tweets
    config.Search = query
    config.Limit = limit
    twint.run.Search(config)
    return [__format_tweet(tweet) for tweet in tweets]
