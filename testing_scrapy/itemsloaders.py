from itemloaders.processors import TakeFirst, MapCompose,Identity
from scrapy.loader import ItemLoader

class QuoteItemLoader(ItemLoader):

    def convert_to_titlecase(title):
        return title.title()
    def convert_str_to_list(tags_str):
        #input:'abilities,choices'
        #output: ['abilities','choices']
        return tags_str.split(',')
    def convert_each_tag_titlecase(tag):        
        return tag.title() 


    default_output_processor = TakeFirst()
    #title_in = MapCompose(lambda x: x.title())
    title_in = MapCompose(convert_to_titlecase)
    #tags_in = MapCompose(lambda x: [tag.title() for tag in x] )
    tags_in = Identity()

    tags_in = MapCompose(convert_each_tag_titlecase)
    tags_out = Identity()