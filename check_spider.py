import requests
from typing import List

try:
    with open("urls.txt", "r") as file:
        url_list: List[str] = [s.strip() for s in file.readlines()]
except:
    url_list = []

i = 1
result_list: List[str] = []
for url in url_list:
    response = requests.get(url)
    print(f"{response.status_code},{url}")
    result_list.append(str(response.status_code) + "," + url)
    filename = str(i) + ".txt"
    with open(filename, "w", encoding = "utf_8") as file:
        file.write(response.text)
    i = i + 1

with open("result.txt", "w", encoding = "utf_8") as file:
    for result in result_list:
        file.write("%s\n" % result)
