import requests
import os
from bs4 import BeautifulSoup


def getHTMLText(url, path, headers=None):
    try:
        root, filename = os.path.split(path)
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            with open(path, 'w') as html:
                html.write(r.text)
            print('html提取成功')
        else:
            print('文件已存在')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = 'http://python123.io/ws/demo.html'
    headers = {'User-Agent': 'Mozilla/5.0'}
    root = r'F:\Spider\解析HTML内容——Beautiful Soup'
    name = 'python123.html'
    path = os.path.join(root,name)
    # print(path)
    getHTMLText(url, path, headers)
    with open(path, 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())