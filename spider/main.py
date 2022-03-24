# Time  ：2022-3-24 15:02
# Author：Houtaroy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 方便调试
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('github')
    process.start()
