
from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class QuoteItemLoader(ItemLoader):

    default_output_processor = TakeFirst()
    title_in = MapCompose(lambda x: x.title())
    #tags_in = MapCompose(lambda x: [tag.title() for tag in x] )