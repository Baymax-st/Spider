import requests
import re
import os
from bs4 import BeautifulSoup
import bs4


def getHtmlText(url, headers=None, path=None):
    '''
    :param url: ��Ҫ��ȡ����ҳ��ַ
    :param headers: ����ͷ
    :param path: �ļ�����·��
    :return: ��ҳhtml�ı�����ַ���
    '''

    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('��ȡ�ɹ�')
        if path is not None:
            root, filename = os.path.split(path)
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                with open(path, 'w', encoding=r.encoding) as f:
                    f.write(f'encodingΪ{r.encoding}\n')
                    f.write(r.text)
                print('�ļ�д��ɹ�')
            else:
                print('�ļ��Ѵ���')
        return r.text
    except Exception as e:
        print(f'��ȡʧ��\n{e}')


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
    # ��ȡ�����Ƹ��Ͻ��������й�Ʊ����
    root = r'F:/Spider/���ס���������ʽ'
    filename = '�����Ƹ���ƱhtmlԴ����.txt'
    path = os.path.join(root, filename)
    headers = 'Mozilla/5.0'
    url = r'https://quote.eastmoney.com/center/gridlist.html#bj_a_board'
    stockHtml = getHtmlText(url, path=path, headers=headers)
    # ������ҳ��Ϣ���õ���Ʊ���Ƽ����룬���ֵ���ʽ����
    stockList = parsePage(stockHtml)
    # ������ϸ��Ϣ���ӣ��Ա��ڰٶȵĹ���ͨ�в��ҹ�Ʊ�۸����Ϣ
    infoLinks = mergeLink(stockList)
    for name, link in infoLinks.items():
        html = getHtmlText(link, headers=headers)
    outputFile = '��Ʊ��Ϣ.txt'
    outputPath = os.path.join(root, outputFile)


main()




