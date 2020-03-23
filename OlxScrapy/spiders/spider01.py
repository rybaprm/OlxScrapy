import scrapy

# Declared default variable - search link of the site olx.ua
START_URL = '''https://www.olx.ua/nedvizhimost/zaporozhe/?search%5B
filter_float_price%3Afrom%5D=10000&search%5B
filter_float_price%3Ato%5D=23000&search%5Bdistrict_id%5D
=51&currency=USD'''

# Declared xpath variable for search to the site olx.ua
# xpath_olx_ad - xpath for find elements consist data of ad
xpath_olx_ad = '//*[@id="offers_table"]/tbody/tr[@class="wrap"]'
# xpath_olx_ad_url - xpath for find url in some ad data
xpath_olx_ad_url = './/*/div/h3/a/@href'
# xpath_olx_ad_text - xpath for find text in some ad data
xpath_olx_ad_text = './/*/div/h3/a/strong/text()'
# xpath_olx_ad_date - xpath for find date in some ad data
xpath_olx_ad_date = './/*/div[@class ="space rel"]/p/small[2]/span/text()'
# xpath_olx_ad_price - xpath for find price in some ad data
xpath_olx_ad_price = './/*/div/p[@class="price"]/strong/text()'
# xpath_olx_next_page - xpath for find elements consist url of next page
xpath_olx_next_page = '//*/span[@class="fbold next abs large"]/a/@href'

class QuotesSpider(scrapy.Spider):
	name = 'olx_scrapy_spider'
	start_urls = [START_URL]
	def parse(self, response):
		for olx_ad in response.xpath(xpath_olx_ad):
			ad_url = olx_ad.xpath(
				xpath_olx_ad_url).get()  # find URL of ad
			ad_text = olx_ad.xpath(
				xpath_olx_ad_text).get()  # find text of ad
			ad_date = olx_ad.xpath(
				xpath_olx_ad_date).getall()[1].strip()  # find date of ad
			ad_price = olx_ad.xpath(
				xpath_olx_ad_price).get().strip('$').replace(' ', '')  # price
			# return dictionary that consist elements: link, text, date, price
			# of ad
			yield {
				'link': ad_url.split('#')[0],
				'text': ad_text.encode("cp1251", "ignore").decode("cp1251"),
				'date': ad_date,
				'price': ad_price
				}
		# find url of next page
		next_page = response.xpath(xpath_olx_next_page).get()
		if next_page:
			# next step of pagination
			yield scrapy.Request(response.urljoin(next_page))