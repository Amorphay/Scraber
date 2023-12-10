import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

timestamp = time.time()
dt_object = datetime.fromtimestamp(timestamp)
formatted_date = dt_object.strftime("%Y-%m-%d %H:%M:%S")
head = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}
response = requests.get('https://www.hdu.edu.cn/news/main.htm', headers=head)
if response.ok:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    ase = soup.find_all("li")
    print(f"爬取时间 {formatted_date}")
    for i in ase:
        print(i.text.strip())

else:
    print("请求失败")
response.close()
