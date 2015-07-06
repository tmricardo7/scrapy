from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.conf import settings
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


import scrapy
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["ucr.ac.cr"]
    start_urls = [
        "http://mediacionvirtual.ucr.ac.cr/19/"
    ]
    rules = (
        Rule(LxmlLinkExtractor(),
    )

    def parse(self, response):
        x = response.xpath('//div')
        for p in x.xpath('//@href'):
            print p.extract()

process = CrawlerProcess()
process.crawl(DmozSpider)
process.start() # the script will block here until all crawling jobs are finished