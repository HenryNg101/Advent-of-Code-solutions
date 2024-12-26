import requests
import json

def load_cookies(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        cookies = json.load(file)
    return cookies

def get_input(year: str, day: str):
    COOKIES = load_cookies('cookies.json')
    URL = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(URL, cookies=COOKIES)
    return response.content.decode("utf-8")