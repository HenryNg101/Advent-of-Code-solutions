import requests

#Change the value of the "session" key to your own key
COOKIES = {
    'session': '53616c7465645f5f67e747e4ec15f285204a54730944591d46e3567ae7d7fe60bcd4f2a155884944f904f56e184bfed319e1b109b2f5f896876591e936b9c62d'
}

def get_input(year: str, day: str):
    URL = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(URL, cookies=COOKIES)
    return response.content.decode("utf-8")