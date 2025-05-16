import requests
import re
import os
from bs4 import BeautifulSoup
import bs4


def getHtmlText(url, headers=None, path=None):
    '''
    :param url: 需要爬取的网页地址
    :param headers: 请求头
    :param path: 文件保存路径
    :return: 网页html文本或空字符串
    '''

    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('爬取成功')
        if path is not None:
            root, filename = os.path.split(path)
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                with open(path, 'w', encoding=r.encoding) as f:
                    f.write(f'encoding为{r.encoding}\n')
                    f.write(r.text)
                print('文件写入成功')
            else:
                print('文件已存在')
        return r.text
    except Exception as e:
        print(f'爬取失败\n{e}')


def parsePage(html):
    html = BeautifulSoup(html, 'lxml')
    tbody = html.find('tbody')
    stockList = {}
    for item in tbody.find_all('tr'):
        if isinstance(item, bs4.element.Tag):
            tds = item.find_all('td')
            if len(tds)==0:
                continue
            name = tds[1].string.strip()
            link = tds[1].get('href')
            code = re.search(r'\d{6}',link)
            stockList[name] = code
    return stockList


def mergeLink(stockList):
    stockLinks = {}
    for name, code in stockList.items():
        url = f'https://gushitong.baidu.com/stock/ab-{code}'
        stockLinks[name] = url
    return stockLinks

def printStockInfo(infoList):
    tpls = f''
    name
    print(tpls.format({},{}))
    pass

def main():
    # 爬取东方财富上交所的所有股票代码
    root = r'F:/Spider/进阶——正则表达式'
    filename = '东方财富股票html源代码.txt'
    path = os.path.join(root, filename)
    headers = 'Mozilla/5.0'
    url = r'https://quote.eastmoney.com/center/gridlist.html#bj_a_board'
    stockHtml = getHtmlText(url, path=path, headers=headers)
    # 解析网页信息，得到股票名称及代码，以字典形式返回
    stockList = parsePage(stockHtml)
    # 生成详细信息链接，以便在百度的股市通中查找股票价格等信息
    infoLinks = mergeLink(stockList)
    for name, link in infoLinks.items():
        html = getHtmlText(link, headers=headers)
    outputFile = '股票信息.txt'
    outputPath = os.path.join(root, outputFile)


main()




