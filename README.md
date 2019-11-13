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
    "courses": {
        "Undergraduate": [{
            "name": "Drama",
            "degree_type": "BA",
            "link": "/courses/ug00097/1/ba-drama",
            "study_mode": "Full-time",
            "location": "Colchester Campus",
            "options": ["Year Abroad", "Placement Year"]
        }, {
            "name": "Drama (Including Foundation Year)",
            "degree_type": "BA",
            "link": "/courses/ug00097/2/ba-drama",
            "study_mode": "Full-time",
            "location": "Colchester Campus",
            "options": []
        }, {
            "name": "Drama and Literature",
            "degree_type": "BA",
            "link": "/courses/ug00098/1/ba-drama-and-literature",
            "study_mode": "Full-time",
            "location": "Colchester Campus",
            "options": ["Year Abroad", "Placement Year"]
        }]
    }
},
```

## Requirements

All requirements are using the latest version available at the time.

-   [Scrapy](https://github.com/scrapy/scrapy) (1.7.3)
-   [Python](https://www.python.org/) (3.7.4)

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

## Problems
As mentioned in [#TODO](#TODO) the crawler is able to retrieve all the courses for Undergraduates and Masters but the results are split into multiple objects. It should be possible to fix this by updating the pipeline to check if each item already exists.

## TODO

-   [x] Fix bug which stops crawler running infinitely
-   [x] Retrieve all courses under degree type including courses hidden behind API call
-   [x] Make second depth a recursive method for courses hidden behind the API call
-   [x] Move CustomFeedStorage method to separate file
-   [x] Add sample item to README.md
-   [X] Reach a depth of 2
-   [ ] Reach a depth of 3 to retrieve more course information
-   [ ] Extract courses from each degree type (Undergraduate, Postgraduate, Research)
    - [ ] Get all courses
    - [ ] Combine duplicate results into one item
-   [ ] Add unit tests
-   [X] Implement caching to avoid potentially being blocked and increase performance time

## Potential TODO

-   [x] Update repository folder structure
-   [x] Update README.md to include more badges
-   [x] Add repository license
-   [ ] Main loop to start the crawler (Running from command line might be fine alone)
-   [ ] Ability to set output file (If running in command line output file can be set otherwise the default can be used)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for more information.
