from functools import lru_cache
from typing import *

from .get_user_profile import get_user_profile


@lru_cache(maxsize=1024)
def name_to_id(user_name: str) -> Optional[str]:
    """
    ユーザー名をユーザーIDに変換する。見つからない場合はNoneを返す。
    :param user_name: ユーザー名
    :return: ユーザーID
    """
    info = get_user_profile(user_name=user_name)
    if info is None:
        return None
    else:
        return info['id']


@lru_cache(maxsize=1024)
def id_to_name(user_id: str) -> Optional[str]:
    """
    ユーザーIDをユーザー名に変換する。見つからない場合はNoneを返す。
    :param user_id: ユーザーID
    :return: ユーザー名
    """
    info = get_user_profile(user_id=user_id)
    if info is None:
        return None
    else:
        return info['user_name']
