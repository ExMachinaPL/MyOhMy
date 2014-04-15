# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from datetime import datetime
from scrapy import log
from scrapy.utils.project import get_project_settings
from dateutil import parser
from urlparse import urlparse
import hashlib
import re
import os
import string
import zipfile

class MyOhMyItem(Item):

    """ Common format for dates is YYYY-MM-DD """
    url = Field()
    title = Field()
    publish_date = Field()
    content = Field()
    geo = Field()
    settings = get_project_settings()
    wdir = settings.get('WRITE_DIR')
    zipdir = settings.get('WRITE_ZIP')
    gdir = settings.get('GIT_DIR')
    datedir = Field()

    def set_pdate(self,pdate):
        """ Method that converts taken argument to common date format """
        if pdate:
            pdt =  parser.parse(pdate)
            self['publish_date'] = str(pdt.year) + "-" + str(pdt.month) + "-" + str(pdt.day)
            self['datedir'] = str(pdt.year) + "/" + str(pdt.month) + "/" + str(pdt.day) + "/"

    def write(self):
        """ Method that writes item data to directory specified by WRITE_DIR in project config.
            File placement is done by creating subdirectory named by originating domain
            then subdirectories for year, month, day if apply.
            Filename is a MD5 from url
            If publish date is not available file is written in domain subdirectory named by first 2 chars of filename"""
        f = hashlib.new('ripemd160')
        f.update(self.get('url'))
        domain = urlparse(self.get('url'))
        if self.get('datedir'):
            path = self.wdir + "/" + domain.netloc + "/" + str(self.get('datedir'))
        else:
            datadir = f.hexdigest()[:2]
            path = self.wdir + "/" + domain.netloc + "/" + datadir +"/"
        if not os.path.isdir(path):
            os.makedirs(path)
        fpath = path + f.hexdigest()
        data = 'URL='+self.get('url')+"\n"+'TITLE='+self.get('title').encode("UTF-8")+"\n"+'PUBLISH_DATE='+str(self.get('publish_date'))+"\n"+'GEO='+self.get('geo')+"\n"+'CONTENT='+self.get('content').encode("UTF-8")
        try:
            if self.zipdir == 1:
                zf = zipfile.ZipFile(fpath+'.zip', 
                mode='w',
                compression=zipfile.ZIP_DEFLATED, 
                )
                try:
                    zf.writestr(f.hexdigest(), data)
                finally:
                    zf.close()
            else:
                output = open(fpath, "w")
                try:
                    output.write(data)
                finally:
                    output.close()
        except IOError:
            log.msg("I/O error({0}): {1}".format(e.errno, e.strerror))

