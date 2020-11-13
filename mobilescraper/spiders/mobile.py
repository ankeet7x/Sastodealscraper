import scrapy
import pandas as pd

class MobileSpider(scrapy.Spider):
	name = "mobile"
	start_urls = [
		'https://www.sastodeal.com/electronic/mobile/samsung.html'
	]

	def parse(self, response):
		for mobile in response.css('div.product-item-info'):
			yield{
				'itemName' : mobile.css('a.product-item-link::text').get().lstrip().rstrip(),
				'itemPrice': mobile.css('span.price::text').get(),
			}