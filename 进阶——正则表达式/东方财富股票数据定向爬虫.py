import requests
import re
import os
from bs4 import BeautifulSoup
import bs4


def getHtmlText(url, path=None):
    '''
    :param url: 需要爬取的网页地址
    :param headers: 请求头
    :param path: 文件保存路径
    :return: 网页html文本或空字符串
    '''

    try:
        r = requests.get(url, timeout=30, headers={'headers':'Mozilla/5.0'})
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


def getStockCode(url, path=None):
    htmlText = getHtmlText(url, path)  # 得到东方财富网的html文本
    html = BeautifulSoup(htmlText, 'lxml')  # 解析文本
    tbody = html.find('tbody')  # 检查html结构发现所有股票信息包含在tbody标签中
    stockList = {}  # 股票名称和代码的字典
    for item in tbody.find_all('tr'):
        if isinstance(item, bs4.element.Tag):
            tds = item.find_all('td')
            if len(tds)==0:
                continue
            name = tds[2].string.strip()
            link = tds[2].get('href')
            code = re.search(r'\d{6}',link)
            stockList[name] = code
    return stockList


def getStockInfo(stockList):
    allStockInfo = []
    for name, code in stockList.items():
        stockInfoList = {}
        url = f'https://gushitong.baidu.com/stock/ab-{code}'
        stockInfoHtml = getHtmlText(url)
        if stockInfoHtml is None:
            print(f'获取{name}:{code}的股票信息失败')
            continue
        else:
            soup = BeautifulSoup(stockInfoHtml, 'lxml')
            # 解析股票信息
            stockInfoBox = soup.find('div', class_='pankou-fold-box')
            stockInfo = stockInfoBox.find_all('div', class_='pankou-item')
            if len(stockInfo) == 0:
                print(f'获取{name}:{code}的股票信息失败')
                continue
            else:
                for item in stockInfo:
                    if isinstance(item, bs4.element.Tag):
                        divs = item.find_all('div')
                        # 提取股票信息
                        factor = divs[0].string.strip()
                        number = divs[1].string.strip()
                        stockInfoList[factor] = number
                allStockInfo.append(stockInfoList)
    return allStockInfo


def main():
    # 爬取东方财富上交所的所有股票代码
    root = r'F:/Spider/进阶——正则表达式'
    filename = '东方财富股票html源代码.txt'
    path = os.path.join(root, filename)
    url = r'https://quote.eastmoney.com/center/gridlist.html#bj_a_board'
    # 解析网页信息，得到股票名称及代码，以字典形式返回
    stockList = getStockCode(url, path)  # 得到股票名称和代码的字典
    allStockInfo = getStockInfo(stockList)  # 生成详细信息链接，以便在百度的股市通中查找股票价格等信息
    # outputFile = '股票信息.txt'
    # outputPath = os.path.join(root, outputFile)
    print(allStockInfo)

main()




