# -*- coding: utf-8 -*-

# Scrapy settings for yhd2 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yhd2'

SPIDER_MODULES = ['yhd2.spiders']
NEWSPIDER_MODULE = 'yhd2.spiders'
SPIDER_MIDDLEWARES = {}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
Referer = 'http://www.yhd.com/'
RETRY_TIMES = 30
# Retry many times since proxies often fail

# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
DOWNLOAD_DELAY = 0.2 # 5,000 ms of delay
CONCURRENT_REQUESTS = 80
LOG_LEVEL = 'INFO'
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

DOWNLOADER_MIDDLEWARES = {
                    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
                  #  'myspider.comm.rotate_useragent.RotateUserAgentMiddleware' : 100,

                    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 200,
                   # 'myspider.comm.random_proxy.RandomProxyMiddleware': 300,

                  #  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 400,
                }

ITEM_PIPELINES = {
    'yhd2.pipelines.DuplicatesPipeline': 300,
}
