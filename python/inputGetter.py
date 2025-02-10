import requests
import json
from pathlib import Path

def load_cookies(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading cookies: {e}")

def get_input(year: int, day: int):
    input_dir = Path('../inputs')
    input_file = input_dir / f'input_{year}_{day}.txt'  # Join the folder and filename to get the path
    
    if input_file.exists():
        return input_file.read_text()
    
    input_dir.mkdir(exist_ok=True)  # Make the folder if doesnt exist
    
    response = requests.get(
        f'https://adventofcode.com/{year}/day/{day}/input', 
        cookies = load_cookies('../cookies.json')
    )
    
    if not response.ok:
        raise RuntimeError(f"Failed to fetch input with {response.reason} error, and status code {response.status_code}")
    
    content = response.text.rstrip('\n')
    input_file.write_text(content)  # Write to the newly created file
    return content