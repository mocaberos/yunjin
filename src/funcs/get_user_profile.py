from typing import *

import twint

from .formatter import __format_user_profile


def get_user_profile(user_name: Optional[str] = None, user_id: Optional[str] = None) -> Optional[dict]:
    """
    ユーザーのプロフィール情報を取得する、見つからない場合はNoneを返す。
    user_name と user_id どちらか片方のみ指定すること
    :param user_name: ユーザー名
    :param user_id:   ユーザーID
    :return: プロフィール情報
    """
    # スクレイピング
    users = []
    config = twint.Config()
    if user_name is not None:
        config.Username = user_name
    else:
        config.User_id = user_id
    config.Hide_output = True
    config.Store_object = True
    config.Store_object_users_list = users

    try:
        twint.run.Lookup(config)
    except (ValueError, KeyError):  # ユーザーが見つからない場合
        return None

    # レスポンス整形
    if len(users) == 0:
        return None
    return __format_user_profile(users[0])
