import scrapy
from testing_scrapy.items import QuoteItem


class QuotesitemsSpider(scrapy.Spider):
    name = "quotesitems"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css("div.quote")
        quotes_item = QuoteItem()
        for quote in quotes:
            quotes_item['title'] = quote.css("span.text::text").get()            
            quotes_item['author'] = quote.css("small.author::text").get()            
            quotes_item['tags'] = quote.css("div.tags a::text").getall()            
            yield quotes_item 

        next_page = response.css('.next a::attr("href")').extract_first()
        if next_page:
           yield scrapy.Request(response.urljoin(next_page)) 