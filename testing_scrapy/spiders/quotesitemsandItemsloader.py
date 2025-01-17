import scrapy
from testing_scrapy.items import QuoteItem
from testing_scrapy.itemsloaders import QuoteItemLoader


class QuotesitemsanditemsloaderSpider(scrapy.Spider):
    name = "quotesitemsandItemsloader"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    custom_settings = {
        'ITEM_PIPELINES': {
            'testing_scrapy.pipelines.FilterLoveTagQuotePipeline': 100,            
        },
        'FEEDS' : {
    'data/%(name)s/%(name)s_%(time)s.json': {
        'format': 'json',        
        }}
    }

    def parse(self, response):
        quotes = response.css("div.quote")         
        for quote in quotes:
            quotes_item = QuoteItemLoader(item=QuoteItem(),selector=quote)
            quotes_item.add_css('title',"span.text::text")            
            quotes_item.add_css('author',"small.author::text")           
            #quotes_item.add_css('tags',"div.tags meta.keywords::attr('content')")  
            quotes_item.add_css('tags',"div.tags a.tag::text")         
            yield quotes_item.load_item() 

        next_page = response.css('.next a::attr("href")').extract_first()
        if next_page:
           yield scrapy.Request(response.urljoin(next_page)) 