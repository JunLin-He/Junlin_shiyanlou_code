# -*- coding: utf-8 -*-
import scrapy
from shiyanlou_course.items import ShiyanlouCourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']
    # spider just a page
    # start_urls = ['https://www.shiyanlou.com/courses/?fee=free']
    # -------------------
    # Changed to spider multiple page
    @property
    def start_urls(self):
        """
        return a iterable object, it could be a list/tuple/generator.
        """
        url_temp = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=free&tag=all&page={}'
        return (url_temp.format(i) for i in range(1, 6))    # Page 1-5

    def parse(self, response):
        courses = response.xpath('//div[@class="col-md-3 col-sm-6  course"]')
        for course in courses:
            item = ShiyanlouCourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            item['description'] = course.xpath('.//div[@class="course-desc"]/text()').extract_first()
            item['image'] = course.xpath('.//div[@class="course-img"]/img/@src').extract_first()

            yield item
        
