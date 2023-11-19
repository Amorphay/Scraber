import requests
from bs4 import BeautifulSoup
import re
head = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}


response = requests.get('https://nyaa.si/', headers=head)
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    ase = soup.find_all("a")
    with open("Anime name.txt", "w", encoding='utf-8') as f:
        for a in ase:
            result = a.text.strip()
            if result and len(result) > 12:
                f.write(result + "\n")
else:
    print("请求失败")
response.close()
