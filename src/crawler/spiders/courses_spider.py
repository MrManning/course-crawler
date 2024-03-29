# -*- coding: utf-8 -*-
import scrapy
import crawler.items as items
import crawler.helper_functions as helper

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CoursesSpider(CrawlSpider):
    """

    Attributes:
        name: A string representing what the spider is called.
        allowed_domains: A list of URLs the spider is allowed to crawl.
        start_urls: The initial URL the spider starts crawling from.
        count: The amount of subjects crawled.
        rules: Determines which URLs the spider can/cannot crawl.
    """

    name = 'courses'
    allowed_domains = ['essex.ac.uk']
    start_urls = ['https://essex.ac.uk/']
    count = 0

    rules = (
        Rule(LinkExtractor(allow=r'/subjects'), callback='parse_subject', follow=True),
    )

    def parse_subject(self, response):
        """Gets a subject from the University of Essex

        Args:
            response: Represents a HTTP response (a page).

        Raises:
            ValueError: An error occurs if the xpath expression is invalid
            NameError: An error occurs if variable is called without being defined
        """

        for subject in response.xpath('//div[starts-with(@class, "grid__item")]'):
            self.count = self.count + 1
            subject_item = items.SubjectItems()
            subject_item['count'] = self.count
            subject_item['subject'] = subject.css('div.subject__title::text').get()
            subject_item['link'] = subject.css('a::attr(href)').get()
            subject_item['courses'] = {'Undergraduate': [], 'Masters': []}

            next_url = response.urljoin(subject_item['link'])
            yield scrapy.Request(next_url, callback=self.parse_course, meta={'subject_item': subject_item})

    def parse_course(self, response):
        """Gets a course from the University of Essex

        Args:
            response: Represents a HTTP response (a page).

        Returns:

        Raises:
            ValueError: An error occurs if the xpath expression is invalid
            NameError: An error occurs if variable is called without being defined
        """

        subject_item = response.meta['subject_item']
        degree_types = [response.xpath('//div[@id="related-courses-UG"]'), response.xpath('//div[@id="related-courses-PGT"]'),]

        for index, degree in enumerate(degree_types, 1):
            for course in degree.xpath('.//div[@class="grid__item"]'):
                course_title = course.css('h3::text').get().strip().split(" ", 1)

                course_item = items.CourseItems()
                course_item['name'] = course_title[1]
                course_item['degree_type'] = course_title[0]
                course_item['link'] = course.css('a::attr(href)').get()
                course_item['study_mode'] = course.css('div.info-box__item:first-child p::text').get()
                course_item['location'] = course.css('div.info-box__item:nth-child(2) p::text').get()

                course_item['options'] = []
                for opt in course.xpath('.//div[@class="info-box__item"][3]/p/text()'):
                    course_item['options'].append(opt.get())

                subject_item['courses'][helper.get_degree_type(index)].append(course_item)


            load_more_link = degree.xpath('.//div[@id="load-more"]//a[contains(@href, "GetRelatedCourses")]/@href').get()
            if load_more_link is not None:
                next_url = response.urljoin(load_more_link)
                yield scrapy.Request(next_url, callback=self.parse_course, meta={'subject_item': subject_item})
            else:
                if len(degree_types) == index and load_more_link is None:
                    yield subject_item

        return
