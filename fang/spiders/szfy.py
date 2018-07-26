# -*- coding: utf-8 -*-
import scrapy

from fang.items import FangItem


class SzfySpider(scrapy.Spider):
    name = 'szfy'
    allowed_domains = ['http://esf.sz.fang.com/']
    start_urls = ['http://esf.sz.fang.com/']
    url = 'http://esf.sz.fang.com'
    def parse(self, response):
        hrefs = response.xpath('//dl[@class="clearfix"]/dd/h4[@class="clearfix"]/a/@href').extract()
        for href in hrefs:
            detail_html = self.url + href
            yield scrapy.Request(detail_html,callback=self.parse_detail,dont_filter=True)

        next_href = response.xpath('//*[@id="list_D10_15"]/p/a[text()="下一页"]/@href').extract_first()
        next_url = self.url+next_href
        yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)

    def parse_detail(self, response):
        item = FangItem()

        total_price = response.xpath('//div[@class="tab-cont-right"]/div[@class="tr-line clearfix zf_new_title"]/div[@class="trl-item_top"]/div[@class="trl-item price_esf  sty1"]/i/text()').extract()[0].strip()
        house_type = response.xpath('//div[@class="tab-cont-right"]/div[@class="tr-line clearfix"]/div[@class="trl-item1 w146"]/div[@class="tt"]/text()').extract()[0].strip()
        size = response.xpath('//div[@class="tab-cont-right"]/div[@class="tr-line clearfix"]/div[@class="trl-item1 w182"]/div[@class="tt"]/text()').extract()[0].strip()

        chaoxiang = response.xpath('/html/body/div[5]/div[1]/div[4]/div[3]/div[1]/div[1]/text()').extract()[0].strip()
        building_type = response.xpath('/html/body/div[5]/div[1]/div[4]/div[3]/div[2]/div[1]/text()').extract()[0].strip()
        name = response.xpath('//*[@id="agantesfxq_C03_05"]/text()').extract()[0].strip()
        beizhu = response.xpath('/html/body/div[5]/div[1]/div[4]/div[4]/div[1]/div[2]/span/text()').extract()[0].strip()
        local = response.xpath('//*[@id="agantesfxq_C03_07"]/text()').extract()[0].strip()
        school = response.xpath('//*[@id="agantesfxq_C03_09"]/text()').extract()[0].strip()
        building_time =response.xpath('//html/body/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/span[2]/text()').extract()[0].strip()
        price =response.xpath('/html/body/div[5]/div[1]/div[4]/div[2]/div[3]/div[1]/text()').extract()[0].strip()
        item['total_price'] = total_price
        item['house_type'] = house_type
        item['size'] = size
        item['chaoxiang'] = chaoxiang
        item['building_type'] = building_type
        item['name'] = name
        item['beizhu'] = beizhu
        item['local'] = local
        item['school'] = school
        item['building_time'] = building_time
        item['price'] = price
        yield item

