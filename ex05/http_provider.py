import requests as api


def get(url):
    response = api.get(url)
    if response.status_code == 200:
        datas = response.json()["response"]["body"]["items"]["item"]
        return datas
