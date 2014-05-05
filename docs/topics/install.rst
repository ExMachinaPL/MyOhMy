.. _topics-install:

===================
Instalacja projektu
===================

Aby rozpocząć korzystanie z projektu należy zainstalować projekt Scrapy: http://scrapy.org i zainicjalizować nowy projekt.

Instalacja na Ubuntu
------------------------------

 sudo apt-get install python-pip python-dev build-essential python-scrapy python-cssselect
 sudo pip install Scrapy beautifulsoup4 zipdir
 export MOM="/path_to_project_dir"
 #Utwórz katalog jeśli nie istnieje
 mkdir -p $MOM
 cd $MOM
 scrapy startproject mom




