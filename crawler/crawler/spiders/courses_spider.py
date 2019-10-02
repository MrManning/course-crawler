# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
# from scrapy.crawler import CrawlerProcess
import crawler.items as items


class CoursesSpider(CrawlSpider):
    name = 'courses'
    allowed_domains = ['essex.ac.uk']
    start_urls = ['https://essex.ac.uk/']

    rules = (
        Rule(LinkExtractor(allow=r'subjects'), callback='parse_subject'),
    )

    # setting the location of the output csv file
    # custom_settings = {
    #     'FEED_URI': 'tmp/courses.json'
    # }

    def parse_subject(self, response):
        sel = Selector(response)
        for subject in sel.css('div[class^="grid__item"]'):
            subject_item = items.SubjectItems()
            subject_item['subject'] = subject.css('div.subject__title::text').get()
            subject_item['link'] = subject.css('a::attr(href)').get()
            yield subject_item
            # yield scrapy.Request(subject_item['link'], self.parse_course, meta={'subject_item': subject_item})

    def parse_course(self, response):
        subject_item = response.meta['subject_item']
        sel = Selector(response)
        all_courses = []

        for course in sel.css('div[class="grid__item"]'):
            course_title = course.css('h3::text').strip().split(" ", 1)

            course_item = items.CourseItems()
            course_item['name'] = course_title[1]
            course_item['degree_type'] = course_title[0]
            # course_item['link'] =
            # course_item['study_mode'] =
            # course_item['location'] =
            # course_item['options'] =
            # course_item['duration'] =
            all_courses.append(course_item)

        subject_item['courses'] = [dict(all_courses)]
        yield subject_item
