import requests

#Change the value of the "session" key to your own key
COOKIES = {
    '_ga': 'GA1.2.1887550309.1732287497',
    '_gid': 'GA1.2.756549688.1732455219',
    '_ga_MHSNPJKWC7': 'GS1.2.1732458150.3.1.1732459421.0.0.0',
    'session': '53616c7465645f5fb82426dd9637e3176d39889b657ad53cc5f10b09e403ac8c85ae8c986570dbd0d6517b21592d984245bc3fe0436b9f6165b776589558d8af'
}

def get_input(year: str, day: str):
    URL = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(URL, cookies=COOKIES)
    return response.content.decode("utf-8")