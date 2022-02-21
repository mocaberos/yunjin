import requests


def test_search_tweets_api_1() -> None:
    raw_res = requests.get(
        'http://localhost:1190/yunjin/api/v1/twitter/search-tweets',
        params={
            'query': 'vtuber',
            'limit': 10
        }
    )
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert len(response['tweets']) > 0


def test_search_tweets_api_2() -> None:
    raw_res = requests.get(
        'http://localhost:1190/yunjin/api/v1/twitter/search-tweets',
        params={
            'query': 'めんだこちゃん',
            'limit': 10
        }
    )
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert len(response['tweets']) > 0


def test_search_tweets_api_3() -> None:
    raw_res = requests.get(
        'http://localhost:1190/yunjin/api/v1/twitter/search-tweets',
        params={
            'query': 'めんだこちゃん',
            'since': '2020-01-01',
            'limit': 10
        }
    )
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert len(response['tweets']) > 0


def test_get_user_profile_by_id_api() -> None:
    raw_res = requests.get('http://0.0.0.0:1190/yunjin/api/v1/twitter/user-profile/user_id/1040201001767034882')
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert response['user_name'] == 'Mendako_Vtuber'


def test_get_user_profile_by_name_api() -> None:
    raw_res = requests.get('http://0.0.0.0:1190/yunjin/api/v1/twitter/user-profile/user_name/Mendako_Vtuber')
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert response['id'] == '1040201001767034882'


def test_name_to_id_api() -> None:
    raw_res = requests.get('http://0.0.0.0:1190/yunjin/api/v1/twitter/name-to-id/Mendako_Vtuber')
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert response['user_id'] == '1040201001767034882'


def test_id_to_name_api() -> None:
    raw_res = requests.get('http://0.0.0.0:1190/yunjin/api/v1/twitter/id-to-name/1040201001767034882')
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert response['user_name'] == 'Mendako_Vtuber'


def test_user_timeline_api() -> None:
    raw_res = requests.get(
        'http://localhost:1190/yunjin/api/v1/twitter/user-timeline',
        params={
            'user_id': '1040201001767034882',
            'since': '2022-01-01',
            'until': '2022-01-10'
        }
    )
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert len(response['tweets']) > 0
