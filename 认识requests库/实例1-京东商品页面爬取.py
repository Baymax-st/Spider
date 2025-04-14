import requests  #导入requests库
from lxml import etree  #导入etree模块
# 1.发送请求
url = 'https://item.jd.com/10104633893603.html'  #京东商品页面

class getHTMLText:
    def __init__(self, url):
        self.url = url

    def getHTMLText(self):
        try:
            r = requests.get(self.url, timeout=30)  #发送请求
            r.raise_for_status()  #检查请求是否成功
            r.encoding = r.apparent_encoding  #设置编码
            return r.text  #返回页面内容
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            exit()


if __name__ == "__main__":
    url = 'https://item.jd.com/10104633893603.html'  #京东商品页面
    HTMLText = getHTMLText(url)  #创建对象
    html = HTMLText.getHTMLText()  #获取页面内容
    print(html)  #打印页面内容
