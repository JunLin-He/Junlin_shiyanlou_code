# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        """
        The parameter of the after is from the website, it means different page.
        """
        url_temp = [
            'https://github.com/shiyanlou?tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
        ]
        return url_temp

    def parse(self, response):
        #repositories = response.xpath('//ul[@class="col-12 d-flex width-full py-4 border-bottom public source"]')
        """
        for repository in repositories:
            item = ShiyanlouItem()
            item['repo_name'] = repository.xpath('//div[@class="d-inline-block mb-1"]/h3/a/text()').extract_first()
            item['update_time'] = repository.xpath('//relative-time/@datetime').extract_first()
        """
        #repo_names = repositories[0].xpath('//div[@class="d-inline-block mb-1"]/h3/a/text()').re('(.+)')
        #update_times = repositories[0].xpath('//relative-time/@datetime').extract()
        #for i in range(len(repo_names)):
        #    item = ShiyanlouItem()
        #    item['repo_name'] = repo_names[i]
        #    item['update_time'] = update_times[i]
        #   yield item
        repos = response.xpath('//li[@itemprop="owns"]')
        for repo in repos:
            item = ShiyanlouItem()
            item['repo_name'] = repo.xpath("./div/div/h3/a/text()").extract_first().strip()
            item['update_time'] = repo.xpath("./div/div/relative-time/@datetime").extract_first()

            yield item
        