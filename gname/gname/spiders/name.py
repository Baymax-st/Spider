import scrapy
import chardet

class NameSpider(scrapy.Spider):
    name = "name"
    allowed_domains = ["4399.com"]  # 限定爬虫的域名,如果不设置,则可以爬取任意域名
    # start_urls = ["https://www.4399.com/flash/new.htm"]  # 该列表中的URL会被Scrapy请求,由用户自己设置
    start_urls = [f"https://www.4399.com/flash/new_{i}.htm" for i in range(1,11)]  # 该列表中的URL会被Scrapy请求,由用户自己设置

    def parse(self, response):  # 该方法用来解析response对象
        # print(response.text)
        # 解析网页内容
        ## response.css()方法用于提取网页中的数据
        ## response.xpath()方法也可以用于提取网页中的数据
        ## response.json()方法用于提取网页中的JSON数据

        # 该方法返回一个SelectorList对象,可以使用XPath或CSS选择器来提取数据
        # 这里使用CSS选择器来提取网页中的所有链接
        li_list = response.xpath("//ul[@class='n-game cf']/li")  # 提取所有链接的文本
        for li in li_list:
            name = li.xpath("./a/b/text()").extract_first()
            category = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em/text()").extract_first()
            yield {
                "name" : name,
                "category" : category,
                "date" : date
            }





