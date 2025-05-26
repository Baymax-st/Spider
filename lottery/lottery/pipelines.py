# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os

class LotteryPipeline:
    def process_item(self, item, spider):
        tplt0 = "{0:^8}\t{1:{3}^18}\t{2:^10}"
        print(tplt0.format('期号','红球号码','蓝球号码',chr(12288)))
        tplt1 = "{0:^10}\t{1:^3}\t{2:^3}\t{3:^3}\t{4:^3}\t{5:^3}\t{6:^3}\t{7:^3}"
        print(tplt1.format(item['no'], item['red_ball'][0],item['red_ball'][1], item['red_ball'][2],
                           item['red_ball'][3], item['red_ball'][4], item['red_ball'][5], item['blue_ball']))
        return item


class TxtPipeline:
    def open_spider(self, spider):
        root = r'F:\Spider\lottery'
        filename = r'lottery.txt'
        self.path = os.path.join(root, filename)
        if not os.path.exists(root):
            os.mkdir(root)
        self.f = open(self.path, mode='a', encoding='utf-8')
        tplt = "{0:^8}\t{1:^18}\t{2:^10}"
        self.f.write(tplt.format('期号','红球号码','蓝球号码',chr(12288)))
        self.f.write('\n')

    def close_spider(self, spider):
        if self.f:
            self.f.close()
    def process_item(self, item, spider):
        tplt = "{0:^10}\t{1:^3}{2:^3}{3:^3}{4:^3}{5:^3}{6:^3}\t\t{7:^10}"
        self.f.write(tplt.format(item['no'], item['red_ball'][0],item['red_ball'][1], item['red_ball'][2],
                           item['red_ball'][3], item['red_ball'][4], item['red_ball'][5], item['blue_ball']))
        self.f.write('\n')
        return item
