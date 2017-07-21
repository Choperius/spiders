# -*- coding: utf-8 -*-
import scrapy


class IndeedspiderSpider(scrapy.Spider):
    name = 'indeedspider'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=esports&l=']

    def parse(self, response):
 		for joblisting in response.css('div.row.result'):
 			item = {
				'title': joblisting.css('a.turnstileLink[data-tn-element="jobTitle"]::text').extract_first(),
				'company': joblisting.css('span.company a::text').extract_first(),
				'url': 'https://www.indeed.com' + joblisting.css('a.turnstileLink[data-tn-element="jobTitle"]::attr(href)').extract_first(),
				'location': joblisting.css('span.location span[itemprop="addressLocality"]::text').extract_first()
			}
			yield item
		#follow pagination link	
		next_page_url = response.css('div.pagination a::attr(href)')[-1].extract()
		if next_page_url:
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)