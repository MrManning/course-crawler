import os
from scrapy.extensions.feedexport import FileFeedStorage


class CustomFeedStorage(FileFeedStorage):

    def open(self, spider):
        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        return open(self.path, 'wb')
