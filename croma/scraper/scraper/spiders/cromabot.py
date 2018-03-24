# -*- coding: utf-8 -*-
import scrapy


class CromabotSpider(scrapy.Spider):
    name = 'cromabot'
    allowed_domains = ['www.croma.com']
    start_urls = ['http://www.croma.com/']

    def parse(self, response):
    	images = response.css('img::attr(src)').extract()
    	for item in zip(images):
           scraped_info = {
               'image_urls' : ["https://www.croma.com" + item[0]],
           }

           yield scraped_info
