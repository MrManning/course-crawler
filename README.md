# course-crawler
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


## Overview
This is a Scrapy project which crawls the [University of Essex](https://www.essex.ac.uk) for all courses in every subject. It is an attempt to extract as much information about a course as possible.


## Example data
The project retrieves all courses from all subjects, below is an example of an extracted item in the JSON format pretty printed.

```json
{
        "count": 16,
        "subject": "Drama",
        "link": "/subjects/drama",
        "courses": [{
            "name": "Drama",
            "degree_type": "BA",
            "link": "/courses/ug00097/1/ba-drama"
        }, {
            "name": "Drama (Including Foundation Year)",
            "degree_type": "BA",
            "link": "/courses/ug00097/2/ba-drama"
        }, {
            "name": "Drama and Literature",
            "degree_type": "BA",
            "link": "/courses/ug00098/1/ba-drama-and-literature"
        }, {
            "name": "Drama and Literature (Including Foundation Year)",
            "degree_type": "BA",
            "link": "/courses/ug00098/2/ba-drama-and-literature"
        }]
},
```


## Requirements
All requirements are using the latest version available at the time.

- [Scrapy](https://github.com/scrapy/scrapy) (1.7.3)
- [Python](https://www.python.org/) (3.7.4)


## Installation
Clone the project repo and run the crawler from within the subfolder.

```bash
# Clone project repo
$ git clone https://github.com/MrManning/course-crawler.git course-crawler

# Navigate inside project
$ cd course-crawler/src

# Run the crawler
$ scrapy crawl courses
```

The scraped courses will be located inside `course-crawler/build/courses.json`


## TODO
- [X] Fix bug which stops crawler running infinitely
- [X] Retrieve all courses under degree type including courses hidden behind API call
- [X] Make second depth a recursive method for courses hidden behind the API call
- [X] Move CustomFeedStorage method to separate file
- [X] Add sample item to README.md
- [ ] Reach a depth of 3 to retrieve more course information
- [ ] Extract courses from each degree type (Undergraduate, Postgraduate, Research)
- [ ] Add unit tests
- [ ] Implement caching to avoid potentially being blocked and increase performance time


## Potential TODO
- [X] Update repository folder structure
- [X] Update README.md to include more badges
- [X] Add repository license
- [ ] Main loop to start the crawler
- [ ] Ability to set output file


## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for more information.
