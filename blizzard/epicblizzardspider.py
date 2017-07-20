# -*- coding: utf-8 -*-
import scrapy


class BlizzardspiderSpider(scrapy.Spider):
    name = 'blizzardspider'
    allowed_domains = ['blizzard.com']
    start_urls = ['https://careers.blizzard.com/en-us/openings']

    def parse(self, response):
 		for joblisting in response.css('a.Table-item'):
 			item = {
				'title': joblisting.css('Div.is-wrapped::text')[0].extract(),
				'game': joblisting.css('Div.is-wrapped::text')[1].extract(),
				'location': joblisting.css('Div.is-wrapped::text')[2].extract(),
				'position': joblisting.css('Div.is-wrapped::text')[3].extract(),
			}
			yield item

