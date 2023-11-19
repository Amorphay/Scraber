import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
head = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}

def is_direct_link(link):
    parsed_link = urlparse(link)
    return bool(parsed_link.netloc)

def download_image(url):
    response = requests.get(url)
    if response.ok:
        content_type = response.headers.get('content-type')
        if content_type and 'image' in content_type:
            filename = os.path.basename(url)
            #ext = os.path.splitext(url)[1]
            with open(f'{filename}', 'wb') as f:
                f.write(response.content)
                print(f'图片{url}保存成功')
    else:
        print(f'图片{url}下载失败，状态码：{response.status_code}')


response = requests.get('https://www.keromakura.net/', headers=head)
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    imgS = soup.find_all("img")
    i = 0
    for a in imgS:
        i += 1
        src = a.get('src')
        src = src.strip()
        if is_direct_link(src):
            download_image(src)
        else:
            src = 'https://www.keromakura.net/' + src
            download_image(src)

else:
    print("请求失败")
