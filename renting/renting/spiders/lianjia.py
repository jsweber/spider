# -*- coding: utf-8 -*-
import scrapy
from renting.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['http://sh.lianjia.com/']

    def parse(self, response):
        pass
