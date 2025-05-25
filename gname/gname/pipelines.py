# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GnamePipeline:
    def process_item(self, item, spider):  #处理数据的专用方法
        # print(item)
        print(spider.name)

        return item


class ggPipeline:
    def process_item(self, item, spider):  #处理数据的专用方法
        print(spider.name)
        return item
