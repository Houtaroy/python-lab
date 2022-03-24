import scrapy
from bs4 import BeautifulSoup
from ..items import GithubLinkListItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    # 自定义配置
    custom_settings = {
        'ITEM_PIPELINES': {
            # 流水线类: 排序索引
            'spider.pipelines.GithubLinkPipeline': 300
        }
    }
    allowed_domains = ['github.com']
    start_urls = []

    def start_requests(self):
        return [scrapy.Request("https://github.com/marketplace")]

    def parse(self, response):
        result = GithubLinkListItem()
        result['url'] = response.url
        soup = BeautifulSoup(response.body.decode('utf-8'), 'html.parser')
        result['links'] = [a['href'] for a in soup.find_all('a')]
        return result
