# course-crawler
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)


## Overview
Program which crawls the University of Essex website for all courses in every subject. It is an attempt to extract as much information about a course as possible.

## Requirements
All requirements are using the latest version available at the time.

- [Scrapy] (1.7.3)
- [Python] (3.7.4)


## Installation
Clone the project repo and run the crawler from within the subfolder.

```console
# Clone project repo
git clone https://github.com/MrManning/course-crawler.git course-crawler

# Navigate inside project
cd course-crawler/crawler

# Run the crawler
scrapy crawl courses
```


The scraped courses will be located inside `course-crawler/crawler/tmp/courses.json`


## TODO
- [X] Fix bug which stops crawler running infinitely
- [X] Retrieve all courses under degree type including courses hidden behind API call
- [X] Make second depth a recursive method for courses hidden behind the API call
- [ ] Add repo license
- [ ] Reach a depth of 3 to retrieve more course information
- [ ] Extract courses from each degree type (Undergraduate, Postgraduate, Research)
- [ ] Update README.md to add project badges
- [ ] Add unit tests
- [ ] Implement caching to avoid potentially being blocked and increase performance time

## Potential TODO
- [ ] Main loop to start the crawler
- [ ] Ability to set output file

[Scrapy]: https://github.com/scrapy/scrapy
[Python]: https://www.python.org/
