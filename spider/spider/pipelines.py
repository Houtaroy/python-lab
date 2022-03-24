# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderPipeline:
    def process_item(self, item, spider):
        return item


class GithubLinkPipeline:

    def open_spider(self, spider):
        print("开启爬虫")

    def close_spider(self, spider):
        print("结束爬虫")

    def process_item(self, item, spider):
        print(f'爬取url: %s' % item['url'])
        print(item['links'])
        return item
