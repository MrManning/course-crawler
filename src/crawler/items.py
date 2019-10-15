# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubjectItems(scrapy.Item):
    count = scrapy.Field()
    subject = scrapy.Field()
    link = scrapy.Field()
    courses = scrapy.Field()


class CourseItems(scrapy.Item):
    name = scrapy.Field()
    degree_type = scrapy.Field()
    link = scrapy.Field()
    study_mode = scrapy.Field()
    location = scrapy.Field()
    options = scrapy.Field()
    duration = scrapy.Field()
