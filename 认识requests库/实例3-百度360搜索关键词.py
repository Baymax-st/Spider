import requests


def getHTMLText(url, params=None, headers=None):
    try:
        r = requests.get(url, timeout=30, params=params, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return len(r.text)
    except Exception as e:
        return e


if __name__ == '__main__':
    kv = {'wd': 'python'}
    url = 'http://www.baidu.com/s'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    result = getHTMLText(url, kv, headers)
    print(result)
