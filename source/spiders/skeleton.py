from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy import log
from scrapy.utils.project import get_project_settings
from MyOhMy.items import MyOhMyItem
from bs4 import BeautifulSoup
import sys
import re
import ast

class Bip(CrawlSpider):
    name = '' """ Crawler name - same as filename """
    allowed_domains = [] """ List of domains to scrap """
    start_urls = [] """ Starting url """
    geo = ""  """ Geographical coordinates """
    settings = get_project_settings()
    logLinks = settings.get('LOG_LINKS')
    logScripts = settings.get('LOG_SCRIPTS')
    logIscripts = settings.get('LOG_ISCRIPTS')
    logMeta = settings.get('LOG_META')
    logEmpty = settings.get('LOG_EMPTY')

    rules = (
        """ Fill allow with allowed url list """
        Rule(SgmlLinkExtractor(allow=('')), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(deny=(r'.*\.xml$')), follow=False),
    )

    def parse_item(self, response):

        """ Process only text content """
        textHeaders = ['text/plain','text/html']
        textFlag = False

        for i in textHeaders:
             if i in response.headers['content-Type']:
                  textFlag = True
                  break 

        if textFlag:
             sel = Selector(response)
             soup = BeautifulSoup(response.body)
             soup.prettify(formatter="minimal")

             if(self.logIscripts == 1):
                 """ Inline scripts statistics """
                 rexScript = re.compile('<script.*>')
                 rexEmpties = re.compile('^\s*$')
                 scripts = sel.xpath('//script[not(@src)]')
                 for script in scripts:
                     s = rexScript.match(script.extract())
                     text = script.xpath('text()').extract()
                     for c in text:
                         if(s.group()):
                             log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[ISCRIPT]=" + s.group() + "," + str(len(c)), level=log.INFO)
                         else:
                             log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[ISCRIPT]=" + str(len(c)), level=log.INFO)

             if(self.logScripts == 1):
                 """ External Scripts """
                 escripts = sel.xpath('//script[@src]')
                 for escript in escripts:
                	 log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[SCRIPT]=" + escript.extract())
    
             if(self.logMeta == 1):
                 """ Meta """
                 meta = sel.xpath('//meta')
                 for m in meta:
                     log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[META]=" + m.extract(), level=log.INFO)
    
             if(self.logLinks == 1):
                 """ Links """
                 links = sel.xpath('//a')
                 for l in links:
                     log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[LINK]=" + l.extract(), level=log.INFO)

             """ Propagate item with data if required fields are present """
             content = None

             """ Put soup find query to extract content """
             content = soup.find() 

             if content:
                 item = MyOhMyItem()
                 item['url'] = response.url
                 item['title'] = soup.title.string

                 """ Find publish date """
                 publishDate = soup.find()
                 item.set_pdate(publishDate)
                 item['geo'] = self.geo
                 item['content'] = content.get_text()
                 item['crawler'] = name
                 item.write()
                 return item
             else:
                 if self.logEmpty == 1:
                     log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[INFO]=Required fields not found")
