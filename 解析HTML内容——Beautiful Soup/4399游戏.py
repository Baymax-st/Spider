import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        # 使用requests库获取网页内容
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = response.apparent_encoding  # 设置编码
        return response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def parse_html(html):
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(html, 'lxml')
    # 找到游戏列表
    ul = soup.find('ul', class_='tm_list')
    # 提取游戏名称
    games = ul.find_all('a')
    for game in games:
        print(game.text.strip())


if __name__ == "__main__":
    url = "https://www.4399.com"
    html_content = get_html(url)
    if html_content:
        print(html_content)
        parse_html(html_content)