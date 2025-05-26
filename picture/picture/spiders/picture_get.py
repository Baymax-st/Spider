import scrapy
from picture.items import PictureItem


class PictureGetSpider(scrapy.Spider):
    name = "picture_get"
    allowed_domains = ["tpzj.com"]
    start_urls = ["https://www.tpzj.com/mingxing/juzhao/"]

    def parse(self, response, **kwargs):
        img_list = response.css('ul.list_con_box_ul li a img')
        # a_list = response.xpath('//ul[@class="list_con_box_ul"]/li/a')
        # print(a_list)
        for img in img_list:
            # if a.xpath('./@target').get() == '_blank':
            #     continue
            address = img.css('img::attr(src)').extract_first()
            name = img.css('img::attr(alt)').extract_first()
            item = PictureItem()
            item['address'] = address
            item['name'] = f'{name}.jpg'
            # print(item)
            # # 根据scrapy运行原理，将address封装成Request交给引擎
            # scrapy.Request(url = address,
            #                method='get',
            #                callback=self.parse_image)
            # print(item)
            yield item

        # 获取下一页链接
        lis = response.css('div.pages ul li')
        for li in lis:
            if li.css('a::text').extract_first() == '下一页':
                next_page = li.css('a::attr(href)').extract_first()
                if next_page:
                    yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
                break

    # def parse_image(self, response, **kwargs):
    #     print(response.content)

