import requests
from typing import List

try:
    with open("urls.txt", "r") as file:
        url_list: List[str] = [s.strip() for s in file.readlines()]
except:
    url_list = []

for url in url_list:
    response = requests.get(url)
    print(f"{response.status_code},{url}")
