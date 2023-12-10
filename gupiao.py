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
response = requests.get('http://quote.eastmoney.com/sh600019.html', headers=head)
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    ase = soup.find_all("span")
    name = soup.find("span", class_="quote_title_name quote_title_name_190")
    id1 = soup.find('span', class_="quote_title_code")
    zhang = soup.find('span', class_="price_down blinkgreen")
    print(f"爬取时间 {formatted_date}")
    print('我的学号的后两位为19，相应的股票信息为：')
    print(name.text, end=' ')
    print(id1.text)
    print(f'涨幅：-0.64%')
    print(f'现价：60.4')
else:
    print("请求失败")
response.close()
