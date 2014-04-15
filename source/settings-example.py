# Scrapy settings for MyOhMy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'MyOhMy'

SPIDER_MODULES = ['MyOhMy.spiders']
NEWSPIDER_MODULE = 'MyOhMy.spiders'

VERBOSE = 0
LOG_FILE = '/var/log/scrapy/MyOhMyLog.log'
LOG_LEVEL = 'INFO'

# Log found links? 
LOG_LINKS = 2
# Log found external scripts?
LOG_SCRIPTS = 0
# Log inline scripts stats?
LOG_ISCRIPTS = 0
# Log meta data?
LOG_META = 0
# Log pages not containing content?
LOG_EMPTY = 0

DEPTH_LIMIT = 0
ERROR_LOG = '/var/log/scrapy/MyOhMy.err'

# Where crawled data is going to be stored
WRITE_DIR = '/mom/Publikacje'
# ZIP crawled data? 1 for yes
WRITE_ZIP = 1


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MyOhMy (+http://www.yourdomain.com)'
