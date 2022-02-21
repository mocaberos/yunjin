import requests


def test_health_api() -> None:
    raw_res = requests.get('http://localhost:1190/yunjin/api/v1/sys/health')
    response = raw_res.json()
    assert raw_res.status_code == 200
    assert response['message'] == 'Success!'
