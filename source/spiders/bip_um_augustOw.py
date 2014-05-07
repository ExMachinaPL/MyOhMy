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

class BipUmAugustOw(CrawlSpider):
    name = 'bip_um_augustOw' 
    allowed_domains = ['um-augustow.pbip.pl']
    start_urls = ['http://um-augustow.pbip.pl']
    geo = "53.840226,22.98952"
    settings = get_project_settings()
    logLinks = settings.get('LOG_LINKS')
    logScripts = settings.get('LOG_SCRIPTS')
    logIscripts = settings.get('LOG_ISCRIPTS')
    logMeta = settings.get('LOG_META')
    logEmpty = settings.get('LOG_EMPTY')

    rules = (
        Rule(SgmlLinkExtractor(allow=('http://um-augustow.pbip.pl')), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(deny=(r'.*\.xml$','printInf\.php','showFile\.php')), follow=False),
    )

    def parse_item(self, response):

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
             """ Data are present on pages which url contains param event=informacja  """
             goodUrl = re.search('event=informacja', response.url)
             if goodUrl:
                 content = None
    
                 """ Put soup find query to extract content """
                 c1 = soup.find('div', {'class':'inf_div_gora'})
                 c2 = soup.find('div', {'class':'inf_div_srodek'})
                 if c1 and c2:
                     content = c1.get_text() + "\n" + c2.get_text()
    
                 if content:
                     item = MyOhMyItem()
                     item['url'] = response.url
                     item['title'] = soup.title.string
    
                     """ Find publish date """
                     date = soup.find('table',{'class':'stopka_informacjis ltable'})
                     publishDate = re.search('Data publikacji:\n(\d{4}-\d{2}-\d{2})', date.get_text())
                     if publishDate:
                         item.set_pdate(publishDate.group(1))
                     item['geo'] = self.geo
                     item['content'] = content
                     item['crawler'] = self.name
                     item.write()
                     return item
                 else:
                     if self.logEmpty == 1:
                         log.msg("[GEO]=" + self.geo + "[URL]=" + response.url + "[INFO]=Required fields not found")
