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

class BipUmAleksandrOwKujawski(CrawlSpider):
    name = 'bip_um_aleksandrOw_kujawski'
    allowed_domains = ['www.bip.aleksandrowkujawski.pl']
    start_urls = ['http://www.bip.aleksandrowkujawski.pl']
    geo = "52.875048,18.696252"
    settings = get_project_settings()
    logLinks = settings.get('LOG_LINKS')
    logScripts = settings.get('LOG_SCRIPTS')
    logIscripts = settings.get('LOG_ISCRIPTS')
    logMeta = settings.get('LOG_META')
    logEmpty = settings.get('LOG_EMPTY')

    rules = (
        Rule(SgmlLinkExtractor(allow=('http://www.bip.aleksandrowkujawski.pl')), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(deny=(r'.*\.xml$')), follow=False),
    )

    def parse_item(self, response):

        """ Process only text content """
        textHeaders = ['text/plain','text/html']
        textFlag = False

        for i in textHeaders:
             if i in response.headers['Content-Type']:
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
             Content = None

             """ Put soup find query to extract content """
             Content = soup.find('div', {'id':'PageContent'}) 

             if Content:
                 item = MyOhMyItem()
                 item['url'] = response.url
                 item['title'] = soup.title.string
                 item['geo'] = self.geo
                 """ get publish date. If multiple available leave empty """
                 publishDate = soup.find_all('span',{'class':'metryczka_obiektu_sekcja_opublikowal_data'})
                 if(publishDate and len(publishDate) == 1):
                     item.set_pdate(publishDate[0].get_text())
                 item['content'] = Content.get_text()
                 item.write()
                 return item
             else:
                 if self.logEmpty == 1:
                     log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[INFO]=Required fields not found")
