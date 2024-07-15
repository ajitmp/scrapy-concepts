# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class FilterLifeQuotePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        ## check is title present
        if adapter.get('title'):
            #converting to title case
            if 'Life' in adapter['title'].split():
                return item
            else:
                raise DropItem(f"Missing 'life' in title of {item}")        

        else:
            # drop item if no title
            raise DropItem(f"Missing title in {item}")

class FilterLoveTagQuotePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        ## check is title present
        if adapter.get('tags'):
            #converting to title case
            if 'Love' in adapter['tags']:
                return item
            else:
                raise DropItem(f"Missing 'Love' in tags of {item}")        

        else:
            # drop item if no title
            raise DropItem(f"Missing love tag  in {item}")        
        

class DuplicatesPipeline:

    def __init__(self):
        self.titles_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['title'] in self.titles_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.titles_seen.add(adapter['title'])
            return item