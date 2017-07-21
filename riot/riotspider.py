# -*- coding: utf-8 -*-
import scrapy


class RiotspiderSpider(scrapy.Spider):
    name = 'riotspider'
    allowed_domains = ['riotgames.com']
    start_urls = ['http://riotgames.com/']

    def parse(self, response):
        pass
