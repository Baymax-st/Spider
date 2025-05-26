# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class PicturePipeline:
    def open_spider(self, spider):
        root = r'F:\Spider\picture'
        filename = 'picture_db.txt'
        if not os.path.exists(root):
            os.mkdir(root)
        self.path = os.path.join(root, filename)
        if os.path.exists(self.path):
            os.remove(self.path)
        self.f = open(self.path, 'a', encoding='utf-8')
        tplt = '{0:{3}^64}\t{1:{3}^30}\t{2:{3}^40}'
        self.f.write(tplt.format('图片名称', '图片地址', '本地路径', chr(12288)))
        self.f.write('\n')

    def close_spider(self, spider):
        if self.f:
            self.f.close()
    def process_item(self, item, spider):
        image_name = item['name']
        tplt = '{0:{3}^64}\t{1:{3}<60}\t{2:{3}>40}'
        self.f.write(tplt.format(image_name, item['address'], item['local_path'], chr(12288)))
        self.f.write('\n')
        return item


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # self.name = item['name']
        return scrapy.Request(item['address'])

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.url.split('/')[-1]
        return f'img/{image_name}'

    def item_completed(self, results, item, info):
        # name = item['name']
        # print(f'{name}下载成功')
        ok, finfo = results[0]
        if not ok:
            raise ValueError(f"Image download failed for {item['name']}")
        item['local_path'] = finfo['path']
        return item
