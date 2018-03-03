# coding=utf-8
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from sinanews.items import textItem
from scrapy.contrib.spiders import CrawlSpider, Rule
import re
from bs4 import BeautifulSoup
from datetime import datetime
from scrapy.loader import ItemLoader
class SinanewsSpider(Spider):
    name = "sinanews"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = ["http://news.sina.com.cn/china/"]
    def parse(self, response):
        links = LinkExtractor(allow=()).extract_links(response)
        for link in links:#如果包含则继续爬取
            if "//news.sina.com.cn" in link.url:
                yield Request(url=link.url, callback=self.parse_page)
    def parse_page(self, response):
        for link in LinkExtractor(allow=()).extract_links(response):
            if "//news.sina.com.cn" in link.url:
                yield Request(url=link.url, callback=self.parse_content)
                yield Request(url=link.url, callback=self.parse_page)
    def parse_content(self, response):
        sel = Selector(response)
        url = response.url
        pattern = re.compile("(\w+)")
        write_name = pattern.findall(url)[-2]

        text1 = sel.xpath('//a[@class="source"]/text()').extract()
        text2 = sel.xpath('//h1[@class="main-title"]/text()').extract()
        text3 = sel.xpath('//p[@class="show_author"]/text()').extract()
        text4 = sel.xpath('//span[@class="date"]/text()').extract()
        text5 = sel.xpath("//p/text()").extract()
        text6 = sel.xpath('//div[@class="keywords"]/text()'). extract()
        texts = text1 + text2 + text3 + text4 + text5 + text6
        write_text = open("texts1/" + write_name + ".txt", "w", encoding='utf-8')
        for i in texts:
            write_text.write(i + '\n')
        write_text.close()
        items = []
        return items


