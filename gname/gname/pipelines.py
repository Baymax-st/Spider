# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GnamePipeline:
    def process_item(self, item, spider):  #�������ݵ�ר�÷���
        # print(item)
        print(spider.name)

        return item


class ggPipeline:
    def process_item(self, item, spider):  #�������ݵ�ר�÷���
        print(spider.name)
        return item
