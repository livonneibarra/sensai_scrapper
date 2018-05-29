# -*- coding: utf-8 -*-
from base_spider import BaseSpider


class BestbuySpider(BaseSpider):
    name = "bestbuy.com"

    def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        # TODO: Template changed. Check
        item['title'] = response.css("div#sku-title > h1 *::text").extract_first(default=0)
        item['price'] = float(
            response.css('div.price-block ::attr(data-customer-price)').extract_first(default=0)
        )
        yield item
