import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div.quote'):
            yield {
                'text': quote.xpath('//span.text/text()').get(),
                'author': quote.xpath('//small.author/text()').get(),
                'tags': quote.xpath('//div.tags a.tag/text()').getall(),
            }