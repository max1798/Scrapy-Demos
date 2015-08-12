# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.exceptions import DropItem

class RequiredFieldsPipeline(object):

    required_fields = ['title', 'url', 'author']

    def process_item(self, item, spider):
        for field in self.required_fields:
            if not item.get(field):
                raise DropItem("Field '%s' missing" % (field))
        return item


class FileStorePipeline(object):

    def __init__(self, filename):
        base_dir = os.path.dirname(__file__)
        self.file = open(base_dir + filename, 'a')

    @classmethod
    def from_settings(cls, settings):
        filename = settings['FILE_NAME']
        return cls(filename)


    def process_item(self, item, spider):
        self.file.write('%s,%s,%s \n' % (item['title'].encode('utf-8').strip(), item['author'].encode('utf-8').strip(), item['url'].encode('utf-8').strip()))


