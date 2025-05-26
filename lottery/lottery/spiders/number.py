import scrapy
from lottery.items import LotteryItem

class NumberSpider(scrapy.Spider):
    name = "number"
    allowed_domains = ["500star.com"]
    start_urls = ["https://datachart.500star.com/ssq/"]

    def parse(self, response):
        # print(response.text)
        trs = response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            if tr.xpath("./@class").extract_first()=='tdbck':
                continue
            no = tr.xpath("./td[@align='center']/text()").extract_first()
            red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
            blue_ball = tr.xpath("./td[@class='chartBall02']/text()").extract_first()
            key = LotteryItem()
            key['no'] = no
            key['red_ball'] = red_ball
            key['blue_ball'] = blue_ball
            yield key
            # yield{
            #     'No':No,
            #     'red_ball':red_ball,
            #     'blue_ball':blue_ball
            # }

