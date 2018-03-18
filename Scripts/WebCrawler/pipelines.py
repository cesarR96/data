# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class WebcrawlerPipeline(object):
    uris = {}
    def open_spider(self, spider):
        self.file = open('Salidas/items.json', 'w')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.uris)).save()
        self.file.close()

    def process_item(self, item, spider):
        self.uris[item['url']] = {'ranking': 0, 'enlaces': item['enlaces'], 'ruta': item['ruta']}
        msg = 'la pagina  con url:' + item['url']+ 'tiene ' + str(len(item['enlaces'])) + 'enlaces'
        print(msg)
        return item
