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
    root = r'F:/Spider/解析HTML内容——Beautiful Soup'
    name = 'python123.html'
    path = os.path.join(root, name)
    # print(path)
    # getHTMLText(url, path, headers)  # 获取网页源代码
    with open(path, 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())  # 对html添加缩进和换行，格式化输出
    print(soup.title)
    print(soup.a)  # 第一个a标签，a代表链接标签，a也可以代表其他标签
    # 输出为：<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
    print(soup.a.name)  # 获取标签的名称
    print(soup.a.parent.name)  # 获取父标签的名称
    print(soup.a.attrs)
    print(soup.a.attrs['href'])  # 获取标签的属性值
    print(soup.a['href'])  # 获取标签href的属性值
    for link in soup.find_all('a'):
        print(link.get('href'))
    print(soup.find_all(['a','b']))
