import requests

endpoint = 'http://py4e-data.dr-chuck.net/comments_392598.json'

try:
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=50,
        pool_maxsize=50)
    session.mount('http://', adapter)
    response = session.get(endpoint)
    response.raise_for_status()
    numbers = response.json()['comments']
    sums = 0
    for number in numbers:
        sums += int(number['count'])
    print(sums)

except Exception as ex:
    raise ex