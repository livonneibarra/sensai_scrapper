# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class PricefetcherItem(Item):
    # Definition of our Pricefectcher Item
    url = Field()
    title = Field()
    price = Field
    pass
