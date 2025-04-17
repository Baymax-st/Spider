import requests


def getIPaddress(url, params=None):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return r.text[2000:3000]
    except Exception as e:
        return e


if __name__ == "__main__":
    ip_pool = ['141.11.42.208', '127.0.0.1']
    for ip in ip_pool:
        url = f"https://www.ipshudi.com/{ip}.htm"
        address = getIPaddress(url)
        print(address)
