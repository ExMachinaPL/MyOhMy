.. _topics-conf:

=====================
Konfiguracja projektu
=====================

Po zainstalowaniu oraz zainicjowaniu nowego projektu należy skopiować pliki crawlerów do katalogu spiders.

Otwórz plik settings.py projektu i dopisz następujące parametry:
 
WRITE_DIR = ścieżka do katalogu w którym mają być zapisywane zebrane pliki

WRITE_ZIP = 0 lub 1 jeśli pliki mają zostać spakowane

LOG_FILE = ścieżka do logu crawlera

LOG_LEVEL = INFO

Dodatkowe parametry
-------------------

Dodatkowe parametry przyjmują wartości: 0 (wyłączone) i 1 (włączone).

- LOG_ISCRIPTS - Logowanie statystyk skryptów osadzonych w stronie
- LOG_LINKS - Logowanie znalezionych linków.
- LOG_META - Logowanie znaczników <meta>
- LOG_SCRIPTS - Logowanie informacji o zewnętrznych skryptach


Struktura plików wynikowych
===========================

Treść stron
-----------

URL=adres url z którego pochodzą dane

TITLE=wartość tagu <title> dokumentu html

PUBLISH_DATE=data publikacji w formacie yyyy-mm-dd  (np. 2014-03-24)

GEO=długość i szeroośc geograficzna 

CONTENT=zasadnicza tekstowa treść publikacji. Z treści zostają usunięte wszelkie formatowania i linki zewnętrzne.

Lokalizacja plików wynikowych
-----------------------------

Pliki wynikowe są umieszczane w katalogach o następującej strukturze::
 -nazwa_crawlera
  -domena_z_której_pochodzą_dane
   -rok publikacji
    -miesiąc publikacji
     -dzień publikacji
   -0000 (jeśli nie ma daty publikacji)
    -pierwsze 2 znaki z nazwy pliku 

Nazwy plików są sumą md5 adresu url z którego dane pochodzą.

Crawler log
-----------

Wpisy w logu mają następujący schemat: data(yyyy-mm-dd) godzina (hh:m:ss+strefa czasowa) [scrapy] INFO: DANE

DANE dla poszczególnych przypadków maja następujący schemat:

Inline scripts::
 [URL]=url strony [ISCRIPT] tag otwierający skrypt, liczba znaków (\w) w osadzonym skrypcie

Linki::
 [URL]=url strony [LINK]=zawartość tagu <a>

Znaczniki Meta::
 [URL]=url strony [META]=zawartość tagu <meta>

Skrypty zewnętrzne::
 [URL]=url strony [SCRIPT]= zawartość tagu <script>
