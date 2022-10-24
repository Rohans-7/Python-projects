import requests

def get_joke():
    url='https://some-random-api.ml/joke'
    r=requests.get(url)
    data=r.json()
    return data['joke']

print(get_joke())