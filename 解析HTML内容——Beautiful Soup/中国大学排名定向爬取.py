import os
import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd


def getHTMLText(url, path, headers=None):
    try:
        root, filename = os.path.split(path)
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            with open(path, 'w', encoding=r.encoding) as html:
                html.write(r.text)
            print('html提取成功')
        else:
            print('文件已存在')
    except Exception as e:
        print(f'爬取发生错误\n{e}')


def printUnivList(university_info):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:10}'
    for item in university_info:
        if len(item) == 0:
            continue
        print(tplt.format(item[0], item[1], item[2], chr(12288)))


def saveData(path, university_info):
    root, filename = os.path.split(path)
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(filename):
        df = pd.DataFrame(university_info, columns=university_info[0])
        df.drop(index=0, inplace=True)
        df.to_excel(path, index=False, header=True)
        print('文件已保存')
    else:
        print('文件已存在')


if __name__ == '__main__':
    url = 'https://www.eol.cn/e_html/gk/dxpm/index.shtml'
    headers = {'User-Agent': 'Mozilla/5.0'}
    root = r'F:\Spider\解析HTML内容——Beautiful Soup'
    filename = '中国大学排名.html'
    path = os.path.join(root, filename)
    getHTMLText(url, path, headers)  # 获取并解析网页源代码
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())  # 对html添加缩进和换行，格式化输出
    # 获取排名大学和名称及对应分数
    div = soup.find('div', class_='university-list')
    # print(div.prettify())
    university_info = []
    for item in div.find_all('tr'):
        if isinstance(item, bs4.element.Tag):
            tds = item.find_all('td')
            if len(tds) == 0:
                continue
            rank = tds[0].string
            name = tds[1].string
            score = tds[2].string.replace('\n', ' ')
            university_info.append([rank, name, score])
    printUnivList(university_info)
    resultFile = '中国大学排名.xlsx'
    resultPath = os.path.join(root, resultFile)
    saveData(resultPath, university_info)
