from typing import *


def __format_user_profile(user) -> dict:
    """
    `twint` のオブジェクト(user)を辞書型データに変換する。
    :param user: `twint` の検索レスポンス
    :return: 変換済みデータ
    """
    return {
        'id': user.id,
        'name': user.name,
        'user_name': user.username,
        'bio': user.bio,
        'location': user.location,
        'url': user.url,
        'join_date': user.join_date,
        'join_time': user.join_time,
        'tweets': user.tweets,
        'following': user.following,
        'followers': user.followers,
        'likes': user.likes,
        'media_count': user.media_count,
        'is_private': user.is_private,
        'is_verified': user.is_verified,
        'avatar': user.avatar,
        'background_image': user.background_image
    }


def __format_tweet(tweet, user_id: Optional[str] = None) -> Optional[dict]:
    """
    `twint` のオブジェクト(tweet)を辞書型データに変換する。
    :param tweet:   `twint` の検索レスポンス
    :param user_id: ユーザーID、特定のユーザーのツイート以外を除外する場合に指定する。
    :return: 変換済みデータ
    """
    if user_id is not None and str(user_id) != str(tweet.user_id):
        return None
    return {
        'id': tweet.id,
        'user_id': tweet.user_id,
        'tweet_created_at': tweet.datetime,
        'datestamp': tweet.datestamp,
        'timestamp': tweet.timestamp,
        'timezone': tweet.timezone,
        'username': tweet.username,
        'name': tweet.name,
        'place': tweet.place,
        'content': tweet.tweet,
        'language': tweet.lang,
        'mentions': tweet.mentions,
        'urls': tweet.urls,
        'photos': tweet.photos,
        'replies_count': tweet.replies_count,
        'retweets_count': tweet.retweets_count,
        'likes_count': tweet.likes_count,
        'hashtags': tweet.hashtags,
        'cashtags': tweet.cashtags,
        'link': tweet.link,
        'retweet': tweet.retweet,
        'quote_url': tweet.quote_url,
        'video': tweet.video,
        'thumbnail': tweet.thumbnail,
        'near': tweet.near,
        'geo': tweet.geo,
        'source': tweet.source,
        'user_rt_id': tweet.user_rt_id,
        'user_rt': tweet.user_rt,
        'retweet_id': tweet.retweet_id,
        'reply_to': tweet.reply_to,
        'retweet_date': tweet.retweet_date
    }
