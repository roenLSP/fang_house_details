# -*- coding: utf-8 -*-
import redis
import scrapy

from fang.items import FangItem


class SzfySpider(scrapy.Spider):

    name = 'szfy'
    allowed_domains = ['http://esf.sz.fang.com/']
    start_urls = ['http://esf.sz.fang.com/']
    url = 'http://esf.sz.fang.com'

    def parse(self, response):

        try:
            hrefs = response.xpath('//dl[@class="clearfix"]/dd/h4[@class="clearfix"]/a/@href').extract()
            for href in hrefs:
                detail_html = self.url + href
                yield scrapy.Request(detail_html,callback=self.parse_detail,dont_filter=True)

            next_href = response.xpath('//*[@id="list_D10_15"]/p/a[text()="下一页"]/@href').extract_first()
            next_url = self.url+next_href
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)
        except RecursionError:
            yield self.parse

    def parse_detail(self, response):
        item = FangItem()
        total_prices = response.xpath('//div[@class="tab-cont-right"]/div[@class="tr-line clearfix zf_new_title"]/div[@class="trl-item_top"]/div[@class="trl-item price_esf  sty1"]/i/text()').extract()
        if total_prices:
            total_price =total_prices[0].strip()
        else:
            total_price = None
        house_types = response.xpath('//div[@class="tab-cont-right"]/div[@class="tr-line clearfix"]/div[@class="trl-item1 w146"]/div[@class="tt"]/text()').extract()
        if house_types:
            house_type = house_types[0].strip()
        else:
            house_type =None
        sizes = response.xpath('//div[@class="tab-cont-right"]/div[@class="tr-line clearfix"]/div[@class="trl-item1 w182"]/div[@class="tt"]/text()').extract()
        if sizes:
            size = sizes[0].strip()
        else:
            size = None

        chaoxiangs = response.xpath('/html/body/div[5]/div[1]/div[4]/div[3]/div[1]/div[1]/text()').extract()
        if chaoxiangs:
            chaoxiang = chaoxiangs[0].strip()
        else:
            chaoxiang = None
        building_types = response.xpath('/html/body/div[5]/div[1]/div[4]/div[3]/div[2]/div[1]/text()').extract()
        if building_types:
            building_type = building_types[0].strip()
        else:
            building_type = None
        names = response.xpath('//*[@id="agantesfxq_C03_05"]/text()').extract()
        if names:
            name = names[0].strip()
        else:
            name = None
        beizhus = response.xpath('/html/body/div[5]/div[1]/div[4]/div[4]/div[1]/div[2]/span/text()').extract()
        if beizhus:
            beizhu = beizhus[0].strip()
        else:
            beizhu = None
        locals = response.xpath('//*[@id="agantesfxq_C03_07"]/text()').extract()
        if locals:
            local = locals[0].strip()
        else:
            local =None
        schools = response.xpath('//*[@id="agantesfxq_C03_09"]/text()').extract()
        if schools:
            school = schools[0].strip()
        else:
            school = None
        building_times =response.xpath('//html/body/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/span[2]/text()').extract()
        if building_times:
            building_time = building_times[0].strip()
        else:
            building_time = None
        prices =response.xpath('/html/body/div[5]/div[1]/div[4]/div[2]/div[3]/div[1]/text()').extract()[0].strip()
        if prices:
            price =prices.strip()
        else:
            price = None


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



