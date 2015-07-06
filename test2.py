from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule
import scrapy
from urllib2 import urlopen

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize
import re

paginas = []


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class MySpider(CrawlSpider):
    name = "ucr"
    allowed_domains = ["ucr.ac.cr"]
    start_urls = ["http://ucr.ac.cr/"]

    rules = (Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=()),
                  callback="parse_items", follow=True),
             )

    def parse_items(self, response):
        print response.url + 'lol'
        paginas.append(response.url)


MySpider.custom_settings = dict(DEPTH_LIMIT=1, RETRY_ENABLED=False)

process = CrawlerProcess()
process.crawl(MySpider)
process.start()  # the script will block here until all crawling jobs are finished
print paginas