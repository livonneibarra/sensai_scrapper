# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
import argparse
from pricefetcher.utils import get_product_names, get_retailers_for_product
import time


class LocalPriceScrapper(object):
    def __init__(self):
        self.products = get_product_names()
        self.retailers = {p:get_retailers_for_product(p) for p in self.products}
        pass

    def deploySpider(self, spider_name):
        ## Methods to call spiders, fetch results and save them in csv/json/standard format
        pass

    def parse_unique_spiders(self):
        pass

    def fetch_all(self):
        ## Parse unique spiders to run from retailers
        spider_names = self.parse_unique_spiders(self.retailers)
        return (self.deploySpider(name) for name in spider_names)



def main(args):
    ## Ideal would be to have an asynchronous implementation of the crawlers.
    ## Better would be to deploy the Spiders on scrapinghub.com
    pass



def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wait_time', default=1800,
                        help='Wait time between parsing')
    ## Further arguments for script control.

    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())