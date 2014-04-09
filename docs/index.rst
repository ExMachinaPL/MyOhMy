.. MyOhMy documentation master file, created by
   sphinx-quickstart on Fri Apr  4 10:31:17 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


MyOhMy - Dokumentacja
=====================

MyOhMy jest projektem mającym na celu zbieranie treści publikowanych w BIP'ach i zapisywanie ich w formacie czytelnym dla maszyn.
Projekt wykorzystuje framework Scrapy: http://scrapy.org .


Instalacja
==========
Aby rozpocząć korzystanie z projektu należy zainstalować projekt Scrapy: http://scrapy.org i zainicjalizować nowy projekt.


Konfiguracja projektu
=====================
Po zainstalowaniu oraz zainicjowaniu nowego projektu należy skopiować pliki crawlerów do katalogu spiders.

Otwórz plik settings.py projektu i dopisz następujące parametry:
 
WRITE_DIR = ścieżka do katalogu w którym mają być zapisywane zebrane pliki

WRITE_ZIP = 0 lub 1 jeśli pliki mają zostać spakowane

LOG_FILE = ścieżka do logu crawlera

LOG_LEVEL = INFO

Dodatkowe parametry przyjmują wartości: 0 (wyłączone) i 1 (włączone). W szczególnych przypadkach 2.

- LOG_ISCRIPTS - Logowanie statystyk skryptów osadzonych w stronie
- LOG_LINKS - Logowanie znalezionych linków. Ustawienie 2 - sam link
- LOG_META - Logowanie znaczników <meta>
- LOG_SCRIPTS - Logowanie informacji o zewnętrznych skryptach


Konwencje
=========
Nazewnictwo crawlerów
---------------------
Wszystkie crawlery są nazywane wg nastepującej konwencji:

typ-jednostki_nazwa-miasta[_nazwa-jednostki].py

Gdzie typy jednostki są reprezentowane przez następujące skróty:

- **um** - urząd miasta
- **ug** - urząd gminy
- **umg** - urząd miasta i gminy

Nazwy miast pisane są małymi literami bez polskich znaków.

Nazwa jednostki jest elementem opcjonalnym. Pojawia się gdy jednostka urzędu posiada własny BIP.

Przykładowo crawler urzędu miasta Bielsko-Biała będzie miał nazwę:
um_bielsko-biala.py

Pliki wynikowe
--------------
Pliki wynikowe sa umieszczane w katalogach o następującej strukturze:
-nazwa_crawlera
 -domena_z_której_pochodzą_dane
  -data publikacji (jesli istnieje)

Nazwy plików są sumą md5 adresu z którego dane pochodzą.


Struktura plików wynikowych
==============
Treść stron
-----------
URL=adres url z którego pochodzą dane

TITLE=wartość tagu <title> dokumentu html

PUBLISH_DATE=data publikacji w formacie yyyy-mm-dd  (np. 2014-03-24)

GEO=długość i szeroośc geograficzna 

CONTENT=zasadnicza tekstowa treść publikacji. Z treści zostają usunięte wszelkie formatowania i linki zewnętrzne.::


Crawler log
-----------

Wpisy w logu mają następujący schemat: data(yyyy-mm-dd) godzina (hh:m:ss+strefa czasowa) [scrapy] INFO: DANE

DANE dla poszczególnych przypadków maja następujący schemat:

- Inline scripts:

[URL]=url strony [ISCRIPT] tag otwierający skrypt, liczba znaków (\w) w osadzonym skrypcie



- Linki - odpowiednio dla wartości 1 i 2:

[URL]=url strony [LINK]=zawartość tagu <a>

Zawartość tagu <a>



- Znaczniki Meta

[URL]=url strony [META]=zawartość tagu <meta>



- Skrypty zewnętrzne:

[URL]=url strony [SCRIPT]= zawartość tagu <script>


Dokumenty żródłowe
==================

Lista adresów BIP: http://bip.gov.pl 

Lista crawlerów i status implementacji
======================================

.. table:: Lista spiderów

============================================= ====== ===========
                  Miasto                       Jest   od wersji
============================================= ====== ===========
Urząd Gminy Abramów
Urząd Gminy Adamów
Urząd Gminy Adamówka
Urząd Gminy Aleksandrów
Urząd Gminy Aleksandrów Kujawski
Urząd Gminy Andrespol
Urząd Gminy Andrzejowo
Urząd Gminy Augustów
Urząd Gminy Babiak
Urząd Gminy Baboszewo
Urząd Gminy Baćkowice
Urząd Gminy Bakałarzewo
Urząd Gminy Baligród
Urząd Gminy Bałtów
Urząd Gminy Banie
Urząd Gminy Banie Mazurskie
Urząd Gminy Baranowo
Urząd Gminy Baranów
Urząd Gminy Bargłów Kościelny
Urząd Gminy Bartoszyce
Urząd Gminy Baruchowo
Urząd Gminy Batorz
Urząd Gminy Bądkowo
Urząd Gminy Bedlno
Urząd Gminy Bejsce
Urząd Gminy Belsk Duży
Urząd Gminy Bełchatów
Urząd Gminy Bełżec
Urząd Gminy Besko
Urząd Gminy Bestwina
Urząd Gminy Będzino
Urząd Gminy Biała
Urząd Gminy Biała Podlaska
Urząd Gminy Białe Błota
Urząd Gminy Białobrzegi
Urząd Gminy Białogard
Urząd Gminy Białopole
Urząd Gminy Białowieża
Urząd Gminy Bielany Żyłaki
Urząd Gminy Bielawy
Urząd Gminy Bielice
Urząd Gminy Bieliny
Urząd Gminy Bielsk
Urząd Gminy Bielsk Podlaski
Urząd Gminy Bierawa
Urząd Gminy Bierzwnik
Urząd Gminy Biesiekierz
Urząd Gminy Biłgoraj
Urząd Gminy Biskupiec
Urząd Gminy Biszcza
Urząd Gminy Bledzew
Urząd Gminy Blizanów
Urząd Gminy Bliżyn
Urząd Gminy Błędów
Urząd Gminy Bobrowice
Urząd Gminy Bobrowniki
Urząd Gminy Bobrowo
Urząd Gminy Boćki
Urząd Gminy Bodzanów
Urząd Gminy Bodzechów
Urząd Gminy Bogdaniec
Urząd Gminy Bogoria
Urząd Gminy Bojadła
Urząd Gminy Bojanów
Urząd Gminy Bojszowy
Urząd Gminy Bolesław
Urząd Gminy Bolesławiec
Urząd Gminy Bolimów
Urząd Gminy Boniewo
Urząd Gminy Borki
Urząd Gminy Borkowice
Urząd Gminy Boronów
Urząd Gminy Borowa
Urząd Gminy Borowie
Urząd Gminy Borów
Urząd Gminy Borzechów
Urząd Gminy Borzęcin
Urząd Gminy Borzytuchom
Urząd Gminy Bralin
Urząd Gminy Branice
Urząd Gminy Braniewo
Urząd Gminy Brańsk
Urząd Gminy Brańszczyk
Urząd Gminy Brąszewice
Urząd Gminy Brenna
Urząd Gminy Brochów
Urząd Gminy Brodnica
Urząd Gminy Brojce
Urząd Gminy Brok
Urząd Gminy Brójce
Urząd Gminy Brudzeń Duży
Urząd Gminy Brwinów
Urząd Gminy Brzeszcze
Urząd Gminy Brzeziny
Urząd Gminy Brzeźnica
Urząd Gminy Brzeźnio
Urząd Gminy Brzeżno
Urząd Gminy Brzozie
Urząd Gminy Brzuze
Urząd Gminy Brzyska
Urząd Gminy Buczkowice
Urząd Gminy Budry
Urząd Gminy Budzyń
Urząd Gminy Bukowiec
Urząd Gminy Bukowsko
Urząd Gminy Bulkowo
Urząd Gminy Burzenin
Urząd Gminy Cedry Wielkie
Urząd Gminy Cegłów
Urząd Gminy Cekcyn
Urząd Gminy Ceków Kolonia
Urząd Gminy Celestynów
Urząd Gminy Ceranów
Urząd Gminy Cewice
Urząd Gminy Chełm
Urząd Gminy Chełm Śląski
Urząd Gminy Chełmiec
Urząd Gminy Chełmno
Urząd Gminy Chełmża
Urząd Gminy Chlewiska
Urząd Gminy Chłopice
Urząd Gminy Chmielnik
Urząd Gminy Chmielno
Urząd Gminy Choceń
Urząd Gminy Chocz
Urząd Gminy Choczewo
Urząd Gminy Chodel
Urząd Gminy Chodów
Urząd Gminy Chodzież
Urząd Gminy Chojnice
Urząd Gminy Chojnów
Urząd Gminy Chorkówka
Urząd Gminy Chotcza
Urząd Gminy Chrostkowo
Urząd Gminy Chrzanów
Urząd Gminy Chrząstowice
Urząd Gminy Chrzypsko Wielkie
Urząd Gminy Chynów
Urząd Gminy Ciasna
Urząd Gminy Ciechanów
Urząd Gminy Ciechocin
Urząd Gminy Ciepielów
Urząd Gminy Ciepłowody
Urząd Gminy Cieszków
Urząd Gminy Ciężkowice
Urząd Gminy Cisek
Urząd Gminy Cisna
Urząd Gminy Cmolas
Urząd Gminy Czajków
Urząd Gminy Czarna
Urząd Gminy Czarna Dąbrówka
Urząd Gminy Czarnocin
Urząd Gminy Czarnożyły
Urząd Gminy Czastary
Urząd Gminy Czemierniki
Urząd Gminy Czempiń
Urząd Gminy Czeremcha
Urząd Gminy Czermin
Urząd Gminy Czernica
Urząd Gminy Czernice Borowe
Urząd Gminy Czernichów
Urząd Gminy Czerniejewo
Urząd Gminy Czernikowo
Urząd Gminy Czerwin
Urząd Gminy Czerwińsk
Urząd Gminy Czerwonak
Urząd Gminy Czerwonka
Urząd Gminy Człuchów
Urząd Gminy Czorsztyn
Urząd Gminy Czosnów
Urząd Gminy Czudec
Urząd Gminy Czyże
Urząd Gminy Czyżew-Osada
Urząd Gminy Daleszyce
Urząd Gminy Damasławek
Urząd Gminy Damnica
Urząd Gminy Darłowo
Urząd Gminy Dąbie
Urząd Gminy Dąbrowa
Urząd Gminy Dąbrowa Biskupia
Urząd Gminy Dąbrowa Chełmińska
Urząd Gminy Dąbrowa Tarnowska 
Urząd Gminy Dąbrowa Zielona
Urząd Gminy Dąbrowice
Urząd Gminy Dąbrówka
Urząd Gminy Dąbrówno 
Urząd Gminy Debowa Kłoda
Urząd Gminy Deszczno
Urząd Gminy Dębica
Urząd Gminy Dębnica Kaszubska
Urząd Gminy Dębowa Łąka
Urząd Gminy Dębowiec
Urząd Gminy Długosiodło
Urząd Gminy Dmosin
Urząd Gminy Dobra
Urząd Gminy Dobre
Urząd Gminy Dobromierz
Urząd Gminy Dobroń
Urząd Gminy Dobroszyce
Urząd Gminy Dobryszyce
Urząd Gminy Dobrzyca
Urząd Gminy Dobrzyniewo Duże
Urząd Gminy Dolice
Urząd Gminy Dołhobyczów
Urząd Gminy Domaniewice
Urząd Gminy Domaradz
Urząd Gminy Domaszowice
Urząd Gminy Dominowo
Urząd Gminy Dopiewo
Urząd Gminy Dorohusk
Urząd Gminy Doruchów
Urząd Gminy Dragacz
Urząd Gminy Drelów
Urząd Gminy Drzycim
Urząd Gminy Dubeninki
Urząd Gminy Dubicze Cerkiewne
Urząd Gminy Dubiecko
Urząd Gminy Dubienka
Urząd Gminy Duszniki Wielkopolskie
Urząd Gminy Dwikozy
Urząd Gminy Dydnia
Urząd Gminy Dygowo
Urząd Gminy Dynów
Urząd Gminy Dywity
Urząd Gminy Dziadkowice
Urząd Gminy Dziadowa Kłoda
Urząd Gminy Działdowo
Urząd Gminy Dziemiany
Urząd Gminy Dzierzążnia
Urząd Gminy Dzierzgowo
Urząd Gminy Dzierzkowice
Urząd Gminy Dzierżoniów
Urząd Gminy Dzikowiec
Urząd Gminy Dzwola
Urząd Gminy Dźwierzuty
Urząd Gminy Elbląg
Urząd Gminy Ełk
Urząd Gminy Fabianki
Urząd Gminy Fajsławice
Urząd Gminy Fałków
Urząd Gminy Filipów
Urząd Gminy Firlej
Urząd Gminy Fredropol
Urząd Gminy Frysztak
Urząd Gminy Galewice
Urząd Gminy Garbatka Letnisko
Urząd Gminy Garbów
Urząd Gminy Gardeja
Urząd Gminy Gaszowice
Urząd Gminy Gawłuszowice
Urząd Gminy Gaworzyce
Urząd Gminy Gąsawa
Urząd Gminy Gdów
Urząd Gminy Giby
Urząd Gminy Gidle
Urząd Gminy Gierałtowice
Urząd Gminy Gietrzwałd
Urząd Gminy Gilowice
Urząd Gminy Gizałki
Urząd Gminy Giżycko
Urząd Gminy Głogów
Urząd Gminy Głowno
Urząd Gminy Głuchów
Urząd Gminy Gniewoszów
Urząd Gminy Gniezno
Urząd Gminy Gnojnik
Urząd Gminy Gnojno
Urząd Gminy Goczałkowice-Zdrój
Urząd Gminy Godkowo
Urząd Gminy Godów
Urząd Gminy Godziesze Małe
Urząd Gminy Godziszów
Urząd Gminy Goleszów
Urząd Gminy Golub-Dobrzyń
Urząd Gminy Gołuchów
Urząd Gminy Gołymin-Ośrodek
Urząd Gminy Gomunice
Urząd Gminy Goraj
Urząd Gminy Gorlice
Urząd Gminy Gorzkowice
Urząd Gminy Gorzyce
Urząd Gminy Gostycyn
Urząd Gminy Gostynin
Urząd Gminy Goszczyn
Urząd Gminy Gościeradów
Urząd Gminy Gościno
Urząd Gminy Gowarczów
Urząd Gminy Goworowo
Urząd Gminy Gozdowo
Urząd Gminy Górno
Urząd Gminy Górowo Iławeckie
Urząd Gminy Górzno
Urząd Gminy Górzyca
Urząd Gminy Gózd
Urząd Gminy Grabowo
Urząd Gminy Grabów
urząd Gminy Grajewo
Urząd Gminy Granowo
Urząd Gminy Grążawy
Urząd Gminy Grębków
Urząd Gminy Grębocice
Urząd Gminy Grębów
Urząd Gminy Grodziczno
Urząd Gminy Grodziec
Urząd Gminy Grodzisk
Urząd Gminy Grodzisko Dolne
Urząd Gminy Gromadka
Urząd Gminy Gromnik
Urząd Gminy Gronowo Elbląskie
Urząd Gminy Gródek
Urząd Gminy Gródek nad Dunajcem
Urząd Gminy Grudusk
Urząd Gminy Grunwald
Urząd Gminy Gruta
Urząd Gminy Grybów
Urząd Gminy Grzmiąca
Urząd Gminy Gzy
Urząd Gminy Haczów
Urząd Gminy Hajnówka
Urząd Gminy Hańsk
Urząd Gminy Harasiuki
Urząd Gminy Hażlach
Urząd Gminy Herby
Urząd Gminy Horodło
Urząd Gminy Horyniec Zdroj
Urząd Gminy Hrubieszów
Urząd Gminy Hyżne
Urząd Gminy i Miasta Baranów Sandomierski
Urząd Gminy i Miasta Barwice
Urząd Gminy i Miasta Bisztynek
Urząd Gminy i Miasta Błaszki
Urząd Gminy i Miasta Chęciny
Urząd Gminy i Miasta Chmielnik
Urząd Gminy i Miasta Chocianów
Urząd Gminy i Miasta Czaplinek
Urząd Gminy i Miasta Czerwionka-Leszczyny
Urząd Gminy i Miasta Ćmielów
Urząd Gminy i Miasta Dobczyce
Urząd Gminy i Miasta Dobrodzień
Urząd Gminy i Miasta Dolsk
Urząd Gminy i Miasta Drobin
Urząd Gminy i Miasta Drzewica
Urząd Gminy i Miasta Działoszyn
Urząd Gminy i Miasta Frombork
Urząd Gminy i Miasta Gąbin
Urząd Gminy i Miasta Glinojeck
Urząd Gminy i Miasta Goleniów
Urząd Gminy i Miasta Grodzisk Wielkopolski
Urząd Gminy i Miasta Grójec
Urząd Gminy i Miasta Gryfino
Urząd Gminy i Miasta Gryfów Śląski
Urząd Gminy i Miasta Ińsko
Urząd Gminy i Miasta Izbica Kujawska
Urząd Gminy i Miasta Jelcz-Laskowice
Urząd Gminy i Miasta Jutrosin
Urząd Gminy i Miasta Kleczew
Urząd Gminy i Miasta Kłecko
Urząd Gminy i Miasta Koziegłowy
Urząd Gminy i Miasta Koźmin Wielkopolski
Urząd Gminy i Miasta Krzepice
Urząd Gminy i Miasta Krzywiń
Urząd Gminy i Miasta Lądek Zdrój
Urząd Gminy i Miasta Lubniewice
Urząd Gminy i Miasta Lubomierz
Urząd Gminy i Miasta Lwówek Śląski
Urząd Gminy i Miasta Łasin
Urząd Gminy i Miasta Małogoszcz
Urząd Gminy i Miasta Margonin
Urząd Gminy i Miasta Miechów
Urząd Gminy i Miasta Międzybórz
Urząd Gminy i Miasta Międzylesie
Urząd Gminy i Miasta Mikołajki
Urząd Gminy i Miasta Miłakowo
Urząd Gminy i Miasta Mirosławiec
Urząd Gminy i Miasta Młynary
Urząd Gminy i Miasta Mogielnica
Urząd Gminy i Miasta Mordy
Urząd Gminy i Miasta Myślibórz
Urząd Gminy i Miasta Nekla
Urząd Gminy i Miasta Niemcza
Urząd Gminy i Miasta Nisko
Urząd Gminy i Miasta Nowe Skalmierzyce
Urząd Gminy i Miasta Odolanów
Urząd Gminy i Miasta Ostrzeszów
Urząd Gminy i Miasta Pajęczno
Urząd Gminy i Miasta Pasym
Urząd Gminy i Miasta Pelplin
Urząd Gminy i Miasta Pełczyce
Urząd Gminy i Miasta Piaseczno
Urząd Gminy i Miasta Pieńsk
Urząd Gminy i Miasta Pisz
Urząd Gminy i Miasta Piwniczna-Zdrój
Urząd Gminy i Miasta Połaniec
Urząd Gminy i Miasta Połczyn-Zdrój
Urząd Gminy i Miasta Prabuty
Urząd Gminy i Miasta Prochowice
Urząd Gminy i Miasta Proszowice
Urząd Gminy i Miasta Prusice
Urząd Gminy i Miasta Przysucha
Urząd Gminy i Miasta Pyzdry
Urząd Gminy i Miasta Raszków
Urząd Gminy i Miasta Rudnik nad Sanem
Urząd Gminy i Miasta Rychwał
Urząd Gminy i Miasta Rydzyna
Urząd Gminy i Miasta Serock
Urząd Gminy i Miasta Sędziszów
Urząd Gminy i Miasta Sędziszów Małopolski
Urząd Gminy i Miasta Sępopol
Urząd Gminy i Miasta Sianów
Urząd Gminy i Miasta Skalbmierz
Urząd Gminy i Miasta Skała
Urząd Gminy i Miasta Skaryszew
Urząd Gminy i Miasta Skępe
Urząd Gminy i Miasta Skoki
Urząd Gminy i Miasta Sokołów Małopolski
Urząd Gminy i Miasta Staszów
Urząd Gminy i Miasta Stawiszyn
Urząd Gminy i Miasta Strzyżów
Urząd Gminy i Miasta Swarzędz
Urząd Gminy i Miasta Syców
Urząd Gminy i Miasta Szamocin
Urząd Gminy i Miasta Sztum
Urząd Gminy i Miasta Świątniki Górne
Urząd Gminy i Miasta Tłuszcz
Urząd Gminy i Miasta Trzemeszno
Urząd Gminy i Miasta Tuczno
Urząd Gminy i Miasta Tuliszków
Urząd Gminy i Miasta Ulanów
Urząd Gminy i Miasta w Korszach
Urząd Gminy i Miasta w Lubrańcu
Urząd Gminy i Miasta w Szlichtyngowej
Urząd Gminy i Miasta w Warcie
Urząd Gminy i Miasta Wąchock
Urząd Gminy i Miasta Węgliniec
Urząd Gminy i Miasta Wiązów
Urząd Gminy i Miasta Wieliczka
Urząd Gminy i Miasta Witkowo
Urząd Gminy i Miasta Witnica
Urząd Gminy i Miasta Wleń
Urząd Gminy i Miasta Wronki
Urząd Gminy i Miasta Wyszogród
Urząd Gminy i Miasta Zagórów
Urząd Gminy i Miasta Zduny
Urząd Gminy i Miasta Żerków
Urząd Gminy i Miasta Żuromin
Urząd Gminy Iława
Urząd Gminy Iłowo-Osada
Urząd Gminy Iłów
Urząd Gminy Imielno
Urząd Gminy Inowłódz
Urząd Gminy Inowrocław
Urząd Gminy Irządze
Urząd Gminy Iwaniska
Urząd Gminy Iwierzyce
Urząd Gminy Iwonicz-Zdrój
Urząd Gminy Izabelin
Urząd Gminy Izbicko
Urząd Gminy Jabłonka
Urząd Gminy Jabłonna
Urząd Gminy Jabłonna Lacka
Urząd Gminy Jadów
Urząd Gminy Jaktorów
Urząd Gminy Jakubów
Urząd Gminy Janowice Wielkie
Urząd Gminy Janowiec
Urząd Gminy Janowiec Kościelny
Urząd Gminy Janowo
Urząd Gminy Jaraczewo
Urząd Gminy Jarosław
Urząd Gminy Jasienica
Urząd Gminy Jasienica Rosielna
Urząd Gminy Jasieniec
Urząd Gminy Jasionówka
Urząd Gminy Jasło
Urząd Gminy Jastków
Urząd Gminy Jastrząb
Urząd Gminy Jastrzębia
Urząd Gminy Jaświły
Urząd Gminy Jawor
Urząd Gminy Jaworze
Urząd Gminy Jaworzyna Śląska
Urząd Gminy Jedlicze
Urząd Gminy Jedlińsk
Urząd Gminy Jedlnia Letnisko
Urząd Gminy Jednorożec
Urząd Gminy Jedwabno
Urząd Gminy Jeleniewo
Urząd Gminy Jemielnica
Urząd Gminy Jemielno
Urząd Gminy Jerzmanowa
Urząd Gminy Jerzmanowice - Przeginia
Urząd Gminy Jeziora Wielkie 36
Urząd Gminy Jeziorzany
Urząd Gminy Jeżowe
Urząd Gminy Jeżów
Urząd Gminy Jodłowa
Urząd Gminy Jodłownik
Urząd Gminy Jonkowo
Urząd Gminy Jordanów
Urząd Gminy Jordanów Śląski
Urząd Gminy Józefów nad Wisłą
Urząd Gminy Juchnowiec Kościelny
Urząd Gminy Kadzidło
Urząd Gminy Kalinowo
Urząd Gminy Kaliska
Urząd Gminy Kamienica
Urząd Gminy Kamienica Polska
Urząd Gminy Kamieniec
Urząd Gminy Kamieniec Ząbkowicki
Urząd Gminy Kamienna Góra
Urząd Gminy Kamiennik
Urząd Gminy Kamień
Urząd Gminy Kamionka
Urząd Gminy Kamionka Wielka
Urząd Gminy Kampinos
Urząd Gminy Karczmiska
Urząd Gminy Karnice
Urząd Gminy Karniewo
Urząd Gminy Karsin
Urząd Gminy Kartuzy
Urząd Gminy Kawęczyn
Urząd Gminy Kazanów
Urząd Gminy Kazimierz Biskupi
Urząd Gminy Kaźmierz
Urząd Gminy Kąkolewnica 
Urząd Gminy Kęsowo
Urząd Gminy Kętrzyn
Urząd Gminy Kęty
Urząd Gminy Kiełczygłów
Urząd Gminy Kiernozia
Urząd Gminy Kije
Urząd Gminy Kikół
Urząd Gminy Kiszkowo
Urząd Gminy Kiwity
Urząd Gminy Kleszczewo
Urząd Gminy Klimontów
Urząd Gminy Klonowa
Urząd Gminy Klucze
Urząd Gminy Kluczewsko
Urząd Gminy Klukowo 
Urząd Gminy Klwów
Urząd Gminy Kłaj
Urząd Gminy Kłobuck
Urząd Gminy Kłoczew
Urząd Gminy Kłodzko
Urząd Gminy Kłomnice
Urząd Gminy Kobierzyce
Urząd Gminy Kobiór
Urząd Gminy Kobyla Góra
Urząd Gminy Kobylin-Borzymy
Urząd Gminy Kobylnica
Urząd Gminy Kochanowice
Urząd Gminy Kocierzew Południowy
Urząd Gminy Kocmyrzów-Luborzyca
Urząd Gminy Koczała
Urząd Gminy Kodrąb
Urząd Gminy Kolbudy
Urząd Gminy Kolno
Urząd Gminy Kołaczkowo
Urząd Gminy Kołaczyce
Urząd Gminy Kołaki Kościelne
Urząd Gminy Kołbaskowo
Urząd Gminy Kołczygłowy 
Urząd Gminy Koło
Urząd Gminy Kołobrzeg
Urząd Gminy Komańcza
Urząd Gminy Komarówka Podlaska
Urząd Gminy Komarów-Osada
Urząd Gminy Komorniki
Urząd Gminy Komprachcice
Urząd Gminy Koneck
Urząd Gminy Konopiska
Urząd Gminy Konopnica
Urząd Gminy Konstantynów
Urząd Gminy Końskowola
Urząd Gminy Korczew
Urząd Gminy Korczyna
Urząd Gminy Kornowac
Urząd Gminy Korycin
Urząd Gminy Korytnica
Urząd Gminy Korzenna
Urząd Gminy Kosakowo
Urząd Gminy Kostomłoty
Urząd Gminy Koszalin
Urząd Gminy Koszęcin
Urząd Gminy Kościan
Urząd Gminy Kościelec
Urząd Gminy Kościelisko
Urząd Gminy Kościerzyna
Urząd Gminy Kotla
Urząd Gminy Kotlin
Urząd Gminy Kotuń
Urząd Gminy Kowal
Urząd Gminy Kowala
Urząd Gminy Kowale Oleckie
Urząd Gminy Kowiesy
Urząd Gminy Kozielice
Urząd Gminy Kozłowo
Urząd Gminy Kozy
Urząd Gminy Koźminek
Urząd Gminy Kramsk
Urząd Gminy Krasne
Urząd Gminy Krasnopol
Urząd Gminy Krasnosielc
Urząd Gminy Krasnystaw
Urząd Gminy Krasocin
Urząd Gminy Kraszewice
Urząd Gminy Kraśniczyn
Urząd Gminy Kraśnik
Urząd Gminy Krempna
Urząd Gminy Kroczyce
Urząd Gminy Krokowa
Urząd Gminy Krościenko nad Dunajcem
Urząd Gminy Krościenko Wyżne
Urząd Gminy Krośnice 
Urząd Gminy Krotoszyce
Urząd Gminy Kruklanki
Urząd Gminy Krupski Młyn
Urząd Gminy Kruszyna
Urząd Gminy Krynice
Urząd Gminy Krynki
Urząd Gminy Krypno
Urząd Gminy Krzczonów
Urząd Gminy Krzemieniewo
Urząd Gminy Krzeszów
Urząd Gminy Krzeszyce
Urząd Gminy Krzęcin
Urząd Gminy Krzykosy
Urząd Gminy Krzymów
Urząd Gminy Krzynowłoga Mała
Urząd Gminy Krzywcza
Urząd Gminy Krzywda
Urząd Gminy Krzywiń
Urząd Gminy Krzyżanowice
Urząd Gminy Krzyżanów
Urząd Gminy Ksawerów
Urząd Gminy Książ Wielki
Urząd Gminy Książki
Urząd Gminy Księżpol
Urząd Gminy Kuczbork - Osada
Urząd Gminy Kunice
Urząd Gminy Kurów
Urząd Gminy Kuryłówka
Urząd Gminy Kurzętnik
Urząd Gminy Kuślin
Urząd Gminy Kutno
Urząd Gminy Kuźnica
Urząd Gminy Kwidzyn
Urząd Gminy Kwilcz
Urząd Gminy Lanckorona
Urząd Gminy Laskowa
Urząd Gminy Lasowice Wielkie
Urząd Gminy Latowicz
Urząd Gminy Lądek
Urząd Gminy Legnickie Pole
Urząd Gminy Lelis
Urząd Gminy Lelkowo
Urząd Gminy Leoncin
Urząd Gminy Leszno
Urząd Gminy Lesznowola
Urząd Gminy Leśniowice
Urząd Gminy Lewin Kłodzki
Urząd Gminy Leżajsk
Urząd Gminy Lichnowy
Urząd Gminy Lidzbark Warmiński
Urząd Gminy Limanowa
Urząd Gminy Linia
Urząd Gminy Liniewo
Urząd Gminy Lipce Reymontowskie
Urząd Gminy Lipie
Urząd Gminy Lipinki
Urząd Gminy Lipinki Łużyckie
Urząd Gminy Lipka
Urząd Gminy Lipnica
Urząd Gminy Lipnik
Urząd Gminy Lipno
Urząd Gminy Lipowa
Urząd Gminy Lipowiec Kościelny
Urząd Gminy Lipusz
Urząd Gminy Lisewo
Urząd Gminy Lisia Góra
Urząd Gminy Lisków
Urząd Gminy Liszki
Urząd Gminy Liw z/s Węgrowie
Urząd Gminy Lniano
Urząd Gminy Lubaczów
Urząd Gminy Lubań
Urząd Gminy Lubartów
Urząd Gminy Lubasz
Urząd Gminy Lubawa
Urząd Gminy Lubenia
Urząd Gminy Lubichowo
Urząd Gminy Lubicz
Urząd Gminy Lubień
Urząd Gminy Lubiewo
Urząd Gminy Lubin
Urząd Gminy Lubiszyn
Urząd Gminy Lubochnia
Urząd Gminy Lubomia
Urząd Gminy Lubomino
Urząd Gminy Lubowidz
Urząd Gminy Lubrza
Urząd Gminy Lubsza
Urząd Gminy Lubycza Królewska
Urząd Gminy Ludwin
Urząd Gminy Lutomiersk
Urząd Gminy Lutowiska
Urząd Gminy Lututów
Urząd Gminy Luzino
Urząd Gminy Lyski
Urząd Gminy Łabowa
Urząd Gminy Łabunie
Urząd Gminy Ładzice
Urząd Gminy Łagiewniki
Urząd Gminy Łagów
Urząd Gminy Łambinowice
Urząd Gminy Łanięta
Urząd Gminy Łańcut
Urząd Gminy Łapanów
Urząd Gminy Łapsze Niżne
Urząd Gminy Łaskarzew
Urząd Gminy Łaszczów
Urząd Gminy Łaziska
Urząd Gminy Łąck
Urząd Gminy Łącko
Urząd Gminy Łączna
Urząd Gminy Łęczyce
Urząd Gminy Łęka Opatowska
Urząd Gminy Łękawica
Urząd Gminy Łęki Szlacheckie
Urząd Gminy Łodygowice
Urząd Gminy Łomazy
Urząd Gminy Łomża
Urząd Gminy Łoniów
Urząd Gminy Łubianka
Urząd Gminy Łubniany
Urząd Gminy Łubnice
Urząd Gminy Łubowo
Urząd Gminy Łukowa
Urząd Gminy Łukowica
Urząd Gminy Łuków
Urząd Gminy Łukta
Urząd Gminy Łużna 634
Urząd Gminy Łyse
Urząd Gminy Łysomice
Urząd Gminy Łyszkowice
Urząd Gminy Maciejowice
Urząd Gminy Magnuszew
Urząd Gminy Majdan Królewski
Urząd Gminy Maków
Urząd Gminy Malanów
Urząd Gminy Malbork
Urząd Gminy Malczyce
Urząd Gminy Malechowo
Urząd Gminy Mała Wieś
Urząd Gminy Małdyty
Urząd Gminy Małkinia Górna
Urząd Gminy Mały Płock
Urząd Gminy Manowo
Urząd Gminy Marciszów
Urząd Gminy Marianowo
Urząd Gminy Marklowice
Urząd Gminy Markusy
Urząd Gminy Markuszów
Urząd Gminy Masłów
Urząd Gminy Medyka
Urząd Gminy Męcinka
Urząd Gminy Miasteczko Krajeńskie
Urząd Gminy Miastkowo
Urząd Gminy Miastków Kościelny
Urząd Gminy Miączyn
Urząd Gminy Michałowice
Urząd Gminy Michałowo
Urząd Gminy Michałów
Urząd Gminy Michów
Urząd Gminy Miedziana Góra
Urząd Gminy Miedzichowo
Urząd Gminy Miedzna
Urząd Gminy Miedźna
Urząd Gminy Miedźno
Urząd Gminy Miejsce Piastowe
Urząd Gminy Mielec
Urząd Gminy Mieleszyn
Urząd Gminy Mielnik
Urząd Gminy Mielno
Urząd Gminy Mierzęcice
Urząd Gminy Mieścisko
Urząd Gminy Mietków
Urząd Gminy Międzyrzec Podlaski
Urząd Gminy Miękinia
Urząd Gminy Mikołajki Pomorskie
Urząd Gminy Milejczyce
Urząd Gminy Milejów
Urząd Gminy Milówka
Urząd Gminy Miłki
Urząd Gminy Miłkowice
Urząd Gminy Miłoradz
Urząd Gminy Miłosław
Urząd Gminy Mińsk Mazowiecki
Urząd Gminy Mircze
Urząd Gminy Mirów Stary
Urząd Gminy Mirzec
Urząd Gminy Młodzieszyn
Urząd Gminy Młynarze
Urząd Gminy Mniów
Urząd Gminy Mniszków
Urząd Gminy Mochowo
Urząd Gminy Modliborzyce
Urząd Gminy Mogilany
Urząd Gminy Mokobody
Urząd Gminy Morawica
Urząd Gminy Morzeszczyn
Urząd Gminy Moskorzew
Urząd Gminy Moszczenica
Urząd Gminy Mrągowo 
Urząd Gminy Mrozy
Urząd Gminy Mszana
Urząd Gminy Mściwojów
Urząd Gminy Mucharz
Urząd Gminy Murów
Urząd Gminy Mycielin z/s w Słuszkowie
Urząd Gminy Nadarzyn
Urząd Gminy Nagłowice
Urząd Gminy Narew
Urząd Gminy Narewka
Urząd Gminy Naruszewo
Urząd Gminy Nędza
Urząd Gminy Nieborów
Urząd Gminy Niebylec
Urząd Gminy Niechanowo
Urząd Gminy Niechłów
Urząd Gminy Niedrzwica Duża
Urząd Gminy Niedźwiada
Urząd Gminy Niegosławice
Urząd Gminy Niegowa
Urząd Gminy Niemce
Urząd Gminy Nieporęt
Urząd Gminy Niwiska
Urząd Gminy Nowa Karczma
Urząd Gminy Nowa Ruda
Urząd Gminy Nowa Sól
Urząd Gminy Nowa Sucha
Urząd Gminy Nowa Wieś Lęborska
Urząd Gminy Nowa Wieś Wielka
Urząd Gminy Nowe
Urząd Gminy Nowe Brzesko
Urząd Gminy Nowe Miast n. Wartą
Urząd Gminy Nowe Miasto
Urząd Gminy Nowe Miasto Lubawskie z/s w Mszanowie
Urząd Gminy Nowe Ostrowy
Urząd Gminy Nowe Piekuty
Urząd Gminy Nowe Warpno
Urząd Gminy Nowodwór
Urząd Gminy Nowogródek Pomorski
Urząd Gminy Nowosolna
Urząd Gminy Nowy Duninów
Urząd Gminy Nowy Dwór
Urząd Gminy Nowy Korczyn
Urząd Gminy Nowy Targ
Urząd Gminy Nowy Żmigród
Urząd Gminy Nozdrzec
Urząd Gminy Nurzec Stacja
Urząd Gminy Obrowo
Urząd Gminy Obrzycko
Urząd Gminy Ochotnica Dolna
Urząd Gminy Odolanów
Urząd Gminy Odrzywół
Urząd Gminy Ojrzeń
Urząd Gminy Oksa
Urząd Gminy Olesno
Urząd Gminy Oleśnica
Urząd Gminy Olszanica
Urząd Gminy Olszanka
Urząd Gminy Olszanka
Urząd Gminy Olszewo-Borki
Urząd Gminy Olszówka
Urząd Gminy Olsztyn
Urząd Gminy Opatowiec
Urząd Gminy Opatów
Urząd Gminy Opinogóra Górna
Urząd Gminy Oporów
Urząd Gminy Orchowo
Urząd Gminy Orla
Urząd Gminy Ornontowice
Urząd Gminy Orońsko
Urząd Gminy Osie
Urząd Gminy Osieck
Urząd Gminy Osiecznica
Urząd Gminy Osiek
Urząd Gminy Osiek Jasielski
Urząd Gminy Osiek Mały
Urząd Gminy Osielsko
Urząd Gminy Osięciny
Urząd Gminy Osina
Urząd Gminy Ostaszewo
Urząd Gminy Ostrowice
Urząd Gminy Ostrowite
Urząd Gminy Ostróda
Urząd Gminy Ostrów
Urząd Gminy Ostrów Mazowiecka
Urząd Gminy Ostrów Wielkopolski
Urząd Gminy Ostrówek
Urząd Gminy Ośno Lubuskie
Urząd Gminy Oświęcim
Urząd Gminy Otyń
Urząd Gminy Ozorków
Urząd Gminy Ożarowice
Urząd Gminy Pabianice
Urząd Gminy Pacanów
Urząd Gminy Padwa Narodowa
Urząd Gminy Pakosław
Urząd Gminy Pałecznica
Urząd Gminy Panki
Urząd Gminy Papowo Biskupie
Urząd Gminy Parchowo
Urząd Gminy Parysów
Urząd Gminy Parzęczew
Urząd Gminy Paszowice
Urząd Gminy Pawłowice
Urząd Gminy Pawłowiczki
Urząd Gminy Pawłów
Urząd Gminy Perlejewo
Urząd Gminy Perzów
Urząd Gminy Pęcław
Urząd Gminy Pęczniew
Urząd Gminy Pępowo
Urząd Gminy Piaski
Urząd Gminy Piątek
Urząd Gminy Piątnica
Urząd Gminy Piecki
Urząd Gminy Piekoszów
Urząd Gminy Pielgrzymka
Urząd Gminy Pierzchnica
Urząd Gminy Pietrowice Wielkie
Urząd Gminy Pilchowice
Urząd Gminy Piła
Urząd Gminy Piszczac
Urząd Gminy Pleśna
Urząd Gminy Płaska
urząd Gminy Płoniawy-bramura
Urząd Gminy Płoskinia
Urząd Gminy Płośnica
Urząd Gminy Płużnica
Urząd Gminy Pniewy 
Urząd Gminy Poczesna
Urząd Gminy Podedwórze
Urząd Gminy Podegrodzie
Urząd Gminy Podgórzyn
Urząd Gminy Pokój
Urząd Gminy Pokrzywnica
Urząd Gminy Police
Urząd Gminy Policzna
Urząd Gminy Polkowice
Urząd Gminy Polska Cerkiew
Urząd Gminy Połajewo
Urząd Gminy Pomiechówek
Urząd Gminy Popielów
Urząd Gminy Porąbka
Urząd Gminy Poronin
Urząd Gminy Postomino
Urząd Gminy Poświętne
Urząd Gminy Potęgowo
Urząd Gminy Potok Górny
Urząd Gminy Potok Wielki
Urząd Gminy Potworów
Urząd Gminy Powidz
Urząd Gminy Pozezdrze
Urząd Gminy Prażmów
Urząd Gminy Promna
Urząd Gminy Prostki
Urząd Gminy Prószków
Urząd Gminy Pruchnik
Urząd Gminy Pruszcz
Urząd Gminy Pruszcz Gdański
Urząd Gminy Przasnysz
Urząd Gminy Przechlewo
Urząd Gminy Przeciszów
Urząd Gminy Przecław
Urząd Gminy Przelewice
Urząd Gminy Przemęt
Urząd Gminy Przemyśl
Urząd Gminy Przerośl
Urząd Gminy Przesmyki
Urząd Gminy Przeworno
Urząd Gminy Przeworsk
Urząd Gminy Przewóz
Urząd Gminy Przodkowo
Urząd Gminy Przybiernów
Urząd Gminy Przygodzice
Urząd Gminy Przykona
Urząd Gminy Przyłęk
Urząd Gminy Przyrów
Urząd Gminy Przystajń
Urząd Gminy Przytoczna
Urząd Gminy Przytuły
Urząd Gminy Przytyk
Urząd Gminy Przywidz
Urząd Gminy Psary
Urząd Gminy Pszczółki
Urząd Gminy Puck
Urząd Gminy Puławy
Urząd Gminy Puńsk
Urząd Gminy Purda
Urząd Gminy Puszcza Mariańska
Urząd Gminy Pysznica
Urząd Gminy Raba Wyżna
Urząd Gminy Raciąż
Urząd Gminy Raciążek
Urząd Gminy Raczki
Urząd Gminy Radecznica
Urząd Gminy Radgoszcz
Urząd Gminy Radków
Urząd Gminy Radłów
Urząd Gminy Radomin
Urząd Gminy Radomsko
Urząd Gminy Radomyśl n. Sanem
Urząd Gminy Radomyśl nad Sanem
Urząd Gminy Radoszyce
Urząd Gminy Radwanice
Urząd Gminy Radymno
Urząd Gminy Radymno 
Urząd Gminy Radzanowo
Urząd Gminy Radzanów
Urząd Gminy Radziejowice
Urząd Gminy Radziejów
Urząd Gminy Radziłów
Urząd Gminy Radzyń Podlaski 
Urząd Gminy Rajcza
Urząd Gminy Raków
Urząd Gminy Rakszawa
Urząd Gminy Raniżów
Urząd Gminy Raszyn
Urząd Gminy Rawa Mazowiecka
Urząd Gminy Rąbino
Urząd Gminy Regimin
Urząd Gminy Regnów
Urząd Gminy Rejowiec
Urząd Gminy Rejowiec Fabryczny
Urząd Gminy Repki
Urząd Gminy Reszel
Urząd Gminy Rewal
Urząd Gminy Ręczno
Urząd Gminy Rędziny
Urząd Gminy Rogowo
Urząd Gminy Rogowo k/Rypina
Urząd Gminy Rogów
Urząd Gminy Rogóźno
Urząd Gminy Rojewo
Urząd Gminy Rokietnica
Urząd Gminy Rokitno
Urząd Gminy Ropa
Urząd Gminy Rościszewo
Urząd Gminy Rozdrażew
Urząd Gminy Rozogi
Urząd Gminy Rozprza
Urząd Gminy Ruda Maleniecka
Urząd Gminy Ruda-Huta
Urząd Gminy Rudka
Urząd Gminy Rudna
Urząd Gminy Rudnik
Urząd Gminy Rudniki
Urząd Gminy Rudziniec
Urząd Gminy Ruja
Urząd Gminy Rusiec
Urząd Gminy Rusinów
Urząd Gminy Rutka-Tartak
Urząd Gminy Rutki
Urząd Gminy Rybno
Urząd Gminy Ryczywół
Urząd Gminy Ryglice
Urząd Gminy Ryjewo
Urząd Gminy Rymanów
Urząd Gminy Rymań
Urząd Gminy Rypin
Urząd Gminy Rytwiany
Urząd Gminy Rząśnia
Urząd Gminy Rząśnik
Urząd Gminy Rzeczenica
Urząd Gminy Rzeczniów
Urząd Gminy Rzeczyca
Urząd Gminy Rzekuń
Urząd Gminy Rzepiennik Strzyżewski
Urząd Gminy Rzgów
Urząd Gminy Sabnie
Urząd Gminy Sadki
Urząd Gminy Sadlinki
Urząd Gminy Sadowne
Urząd Gminy Samborzec
Urząd Gminy Sanniki
Urząd Gminy Santok
Urząd Gminy Sarnaki
Urząd Gminy Sawin
Urząd Gminy Secemin
Urząd Gminy Sejny
Urząd Gminy Serniki
Urząd Gminy Serokomla
Urząd Gminy Sędziejowice
Urząd Gminy Sękowa
Urząd Gminy Sicienko
Urząd Gminy Sidra
Urząd Gminy Sieciechów
Urząd Gminy Siedlce
Urząd Gminy Siedlec
Urząd Gminy Siedlisko
Urząd Gminy Siedliszcze
Urząd Gminy Siekierczyn
Urząd Gminy Siemiatycze
Urząd Gminy Siemiątkowo Koziebrodzkie
Urząd Gminy Siemyśl
Urząd Gminy Siennica
Urząd Gminy Siennica Różana
Urząd Gminy Sienno
Urząd Gminy Sieradz
Urząd Gminy Sierakowice
Urząd Gminy Sieroszewice
Urząd Gminy Sierpc
Urząd Gminy Sitkówka-Nowiny
Urząd Gminy Skarbimierz
Urząd Gminy Skarszewy
Urząd Gminy Skarżysko Kościelne
Urząd Gminy Skąpe
Urząd Gminy Skierbieszów
Urząd Gminy Skierniewice
Urząd Gminy Skołyszyn
Urząd Gminy Skomlin
Urząd Gminy Skoroszyce
Urząd Gminy Skórcz
Urząd Gminy Skórzec
Urząd Gminy Skrwilno
Urząd Gminy Skrzyszów
Urząd Gminy Skulsk
Urząd Gminy Sławno
Urząd Gminy Sławoborze
Urząd Gminy Słońsk
Urząd Gminy Słubice
Urząd Gminy Słupca
Urząd Gminy Słupia
Urząd Gminy Słupno
Urząd Gminy Słupsk
Urząd Gminy Smętowo Graniczne
Urząd Gminy Sobienie Jeziory
Urząd Gminy Sobków
Urząd Gminy Sobolew
Urząd Gminy Sochaczew
Urząd Gminy Sochocin
Urząd Gminy Sokolniki
Urząd Gminy Sokoły
Urząd Gminy Solec nad Wisłą
Urząd Gminy Solec Zdrój
Urząd Gminy Solina
Urząd Gminy Somianka
Urząd Gminy Somonino
Urząd Gminy Sońsk
Urząd Gminy Sorkwity
Urząd Gminy Sosnowica
Urząd Gminy Sosnówka
Urząd Gminy Sośnie
Urząd Gminy Sośno
Urząd Gminy Spiczyn
Urząd Gminy Spytkowice
Urząd Gminy Srokowo
Urząd Gminy Stanin
Urząd Gminy Stanisławów
Urząd Gminy Stara Biała
Urząd Gminy Stara Dąbrowa
Urząd Gminy Stara Kamienica
Urząd Gminy Stara Kornica
Urząd Gminy Starcza
Urząd Gminy Stare Babice
Urząd Gminy Stare Bogaczowice
Urząd Gminy Stare Juchy
Urząd Gminy Stare Kurowo
Urząd Gminy Stare Miasto
Urząd Gminy Stare Pole
Urząd Gminy Stargard Szczeciński
Urząd Gminy Staroźreby
Urząd Gminy Stary Brus
Urząd Gminy Stary Dzierzgoń
Urząd Gminy Stary Dzików
Urząd Gminy Stary Lubotyń
Urząd Gminy Stary Targ
Urząd Gminy Stary Zamość
Urząd Gminy Stawiguda
Urząd Gminy Stepnica
Urząd Gminy Sterdyń
Urząd Gminy Stęszew
Urząd Gminy Stężyca
Urząd Gminy Stoczek
Urząd Gminy Stoczek Łukowski
Urząd Gminy Stolno
Urząd Gminy Stopnica
Urząd Gminy Stoszowice
Urząd Gminy Strachówka
Urząd Gminy Strawczyn
Urząd Gminy Stromiec
Urząd Gminy Strzałkowo
Urząd Gminy Strzegowo
Urząd Gminy Strzelce
Urząd Gminy Strzelce Opolskie
Urząd Gminy Strzelce Wielkie
Urząd Gminy Strzeleczki
Urząd Gminy Strzyżewice
Urząd Gminy Studzienice
Urząd Gminy Stupsk
Urząd Gminy Subkowy
Urząd Gminy Suchożebry
Urząd Gminy Suchy Dąb
Urząd Gminy Suchy Las
Urząd Gminy Sulęczyno
Urząd Gminy Sulików
Urząd Gminy Sulmierzyce
Urząd Gminy Sułów
Urząd Gminy Susiec
Urząd Gminy Suszec
Urząd Gminy Suwałki
Urząd Gminy Sypniewo
Urząd Gminy Szastarka
Urząd Gminy Szczaniec
Urząd Gminy Szczawnica
Urząd Gminy Szczecinek
Urząd Gminy Szczerców
Urząd Gminy Szczurowa
Urząd Gminy Szczutowo
Urząd Gminy Szczytno
Urząd Gminy Szelków
Urząd Gminy Szemud
Urząd Gminy Szerzyny
Urząd Gminy Szreńsk
Urząd Gminy Sztabin
Urząd Gminy Sztutowo
Urząd Gminy Szudziałowo
Urząd Gminy Szulborze Wielkie
Urząd Gminy Szumowo
Urząd Gminy Szydłowo
Urząd Gminy Szydłów
Urząd Gminy Szypliszki
Urząd Gminy Ślemień
Urząd Gminy Śliwice
Urząd Gminy Śniadowo
Urząd Gminy Świątki
Urząd Gminy Świdnica
Urząd Gminy Świdwin
Urząd Gminy Świecie nad Osą
Urząd Gminy Świedziebnia
Urząd Gminy Świekatowo
Urząd Gminy Świercze
Urząd Gminy Świerczów
Urząd Gminy Świerklaniec
Urząd Gminy Świerklany
Urząd Gminy Świerzno
Urząd Gminy Świeszyno
Urząd Gminy Święciechowa
Urząd Gminy Święta Katarzyna
Urząd Gminy Świętajno
Urząd Gminy Świętojano
Urząd Gminy Świlcza
Urząd Gminy Świnice Warckie
Urząd Gminy Świnna
Urząd Gminy Tarnawatka
Urząd Gminy Tarnowo Podgórne
Urząd Gminy Tarnów
Urząd Gminy Tarnów Opolski
Urząd Gminy Tczew
Urząd Gminy Tczów
Urząd Gminy Telatyn
Urząd Gminy Teresin
Urząd Gminy Terespol
Urząd Gminy Tereszpol
Urząd Gminy Tłuchowo
Urząd Gminy Tokarnia
Urząd Gminy Tomaszów Lubelski
Urząd Gminy Tomice
Urząd Gminy Topólka
Urząd Gminy Trawniki
Urząd Gminy Trąbki Wielkie
Urząd Gminy Trojanów
Urząd Gminy Troszyn
Urząd Gminy Trzciana
Urząd Gminy Trzcianka
Urząd Gminy Trzcianne
Urząd Gminy Trzcinica
Urząd Gminy Trzebiechów
Urząd Gminy Trzebiel
Urząd Gminy Trzebieszów
Urząd Gminy Trzebownisko
Urząd Gminy Trzeszczany
Urząd Gminy Trzydnik Duży
Urząd Gminy Tuchola
Urząd Gminy Tuchomie
Urząd Gminy Tuczępy
Urząd Gminy Tułowice
Urząd Gminy Turawa
Urząd Gminy Turek
Urząd Gminy Turośl
Urząd Gminy Turośń Kościelna
Urząd Gminy Twardgóra
Urząd Gminy Tworóg
Urząd Gminy Tychowo
Urząd Gminy Tymbark
Urząd Gminy Tyrawa Wołoska
Urząd Gminy Uchanie
Urząd Gminy Ujsoły
Urząd Gminy Ulan-Majorat
Urząd Gminy Ulhówek
Urząd Gminy Ułęż
Urząd Gminy Unisław
Urząd Gminy Urszulin
Urząd Gminy Urzędów
Urząd Gminy Ustka
Urząd Gminy Ustronie Morskie
Urząd Gminy Uście Gorlickie
Urząd Gminy Uścimów
Urząd Gminy w Baranowie
Urząd Gminy w Barcianach
Urząd Gminy w Będkowie
Urząd Gminy w Birczy
Urząd Gminy w Błędowie
Urząd Gminy w Bobowej
Urząd Gminy w Brodach
Urząd Gminy w Buczku
Urząd Gminy w Bytnicy
Urząd Gminy w Bytoniu
Urząd Gminy w Chąśnie
Urząd Gminy w Chybiu
Urząd Gminy w Cielądzu
Urząd Gminy w Cycowie
Urząd Gminy w Czarnej
Urząd Gminy w Czarni
Urząd Gminy w Czarnkowie
Urząd Gminy w Czerminie
Urząd Gminy w Czerniewicach
Urząd Gminy w Dalikowie
Urząd Gminy w Daszynie
Urząd Gminy w Dąbrowie Chełmińskiej
Urząd Gminy w Dobrczu
Urząd Gminy w Dobrzeniu Wielkim
Urząd Gminy w Drużbicach
Urząd Gminy w Godzianowie
Urząd Gminy w Gorzycach
Urząd Gminy w Górze Św. Małgorzaty
Urząd Gminy w Grabicy
Urząd Gminy w Grudziądzu
Urząd Gminy w Grzegorzewie
Urząd Gminy w Huszlewie
Urząd Gminy w Istebnej
Urząd Gminy w Janowie
Urząd Gminy w Kijewie Królewskim
Urząd Gminy w Kleszczowie
Urząd Gminy w Kobylance
Urząd Gminy w Kołbieli 
Urząd Gminy w Kuleszach Kościelnych
Urząd Gminy w Lgocie Wielkiej
Urząd Gminy w Lipnie
Urząd Gminy w Lutocinie
Urząd Gminy w Łowiczu
Urząd Gminy w Małej Wsi
Urząd Gminy w Milejewie
Urząd Gminy w Mykanowie
Urząd Gminy w Nowej Brzeźnicy
Urząd Gminy w Nowym Kawęczynie
Urząd Gminy w Obrazowie
Urząd Gminy w Obrytem
Urząd Gminy w Osieku
Urząd Gminy w Osjakowie
Urząd Gminy w Ostrówku
Urząd Gminy w Pionkach
Urząd Gminy w Platerówce
Urząd Gminy w Płońsku
Urząd Gminy w Podedwórzu
Urząd Gminy w Pszczewie
Urząd Gminy w Reńskiej Wsi
Urząd Gminy w Roźwienicy
Urząd Gminy w Różanie
Urząd Gminy w Rzewniu
Urząd Gminy w Sadkowicach
Urząd Gminy w Słopnicach
Urząd Gminy w Słupi
Urząd Gminy w Smołdzinie
Urząd Gminy w Solcu nad Wisłą
Urząd Gminy w Szczawinie Kościelnym
Urząd Gminy w Tomaszowie Maz.
Urząd Gminy w Udaninie
Urząd Gminy w Ujeździe
Urząd Gminy w Warlubiu
Urząd Gminy w Waśniowie
Urząd Gminy w Wąpielsku
Urząd Gminy w Wiązownicy
Urząd Gminy w Wilczynie
Urząd Gminy w Zabrodziu
Urząd Gminy w Zawadach
Urząd Gminy Waganiec
Urząd Gminy Walce
Urząd Gminy Walim
Urząd Gminy Wapno
Urząd Gminy Warnice
Urząd Gminy Warta Bolesławiecka
Urząd Gminy Wartkowice
Urząd Gminy Wąbrzeźno
Urząd Gminy Wądroże Wielkie
Urząd Gminy Wągrowiec
Urząd Gminy Wąsewo
Urząd Gminy Wąsosz
Urząd Gminy Wąwolnica
Urząd Gminy Wejherowo
Urząd Gminy Werbkowice
Urząd Gminy Węgierska Górka
Urząd Gminy Wiązowna
Urząd Gminy Wicko
Urząd Gminy Widawa
Urząd Gminy Widuchowa
Urząd Gminy Wieczfnia Kościelna 
Urząd Gminy Wielgie
Urząd Gminy Wielgomłyny
Urząd Gminy Wieliczki
Urząd Gminy Wieliszew
Urząd Gminy Wielka Nieszawka
Urząd Gminy Wielka Wieś
Urząd Gminy Wielkie Oczy
Urząd Gminy Wielopol Skrzyński
Urząd Gminy Wielowieś
Urząd Gminy Wieprz
Urząd Gminy Wierzbica
Urząd Gminy Wierzbinek
Urząd Gminy Wierzbno
Urząd Gminy Wierzchlas
Urząd Gminy Wierzchosławice
Urząd Gminy Wierzchowo
Urząd Gminy Wijewo
Urząd Gminy Wilamowice
Urząd Gminy Wilczęta
Urząd Gminy Wilczyce
Urząd Gminy Wilga
Urząd Gminy Wilkołaz
Urząd Gminy Wilkowice
Urząd Gminy Wilków
Urząd Gminy Winnica
Urząd Gminy Wińsko
Urząd Gminy Wiskitki
Urząd Gminy Wisznice
Urząd Gminy Wiślica
Urząd Gminy Wiśniew
Urząd Gminy Wiśniewo
Urząd Gminy Wiśniowa
Urząd Gminy Witonia
Urząd Gminy Wizna
Urząd Gminy Wiżajny
Urząd Gminy Władysławów
Urząd Gminy Włocławek
Urząd Gminy Włodawa
Urząd Gminy Włodowice
Urząd Gminy Włoszakowice
Urząd Gminy Włoszczowa
Urząd Gminy Wodynie
Urząd Gminy Wodziefrady
Urząd Gminy Wodzierady
Urząd Gminy Wodzisław
Urząd Gminy Wohyń
Urząd Gminy Wojaszówka
Urząd Gminy Wojciechowice
Urząd Gminy Wojciechów
Urząd Gminy Wojcieszków
Urząd Gminy Wojnicz
Urząd Gminy Wojsławice
Urząd Gminy Wola Krzysztoporska
Urząd Gminy Wola Mysłowska
Urząd Gminy Wola Uhruska
Urząd Gminy Wolanów
Urząd Gminy Wolbórz
Urząd Gminy Wólka
Urząd Gminy Wręczyca Wielka
Urząd Gminy Wróblew
Urząd Gminy Wydminy
Urząd Gminy Wymiarki
Urząd Gminy Wyry
Urząd Gminy Wyryki
Urząd Gminy Wysokie
Urząd Gminy Wysokie Mazowieckie
Urząd Gminy Wyszki
Urząd Gminy Zabierzów
Urząd Gminy Zadzim
Urząd Gminy Zagnańsk
Urząd Gminy Zagrodno
Urząd Gminy Zakroczym
Urząd Gminy Zakrzew
Urząd Gminy Zakrzewo
Urząd Gminy Zakrzówek
Urząd Gminy Zalesie
Urząd Gminy Zaleszany
Urząd Gminy Załuski
Urząd Gminy Zambrów
Urząd Gminy Zamość
Urząd Gminy Zaniemyśl
Urząd Gminy Zapolice
Urząd Gminy Zaręby Kościelne
Urząd Gminy Zarszyn
Urząd Gminy Zarzecze
Urząd Gminy Zatory
Urząd Gminy Zawidz
Urząd Gminy Zawoja
Urząd Gminy Zawonia
Urząd Gminy Zbiczno
Urząd Gminy Zblewo
Urząd Gminy Zbójna
Urząd Gminy Zbójno
Urząd Gminy Zbrosławice
Urząd Gminy Zbuczyn
Urząd Gminy Zduny
Urząd Gminy Zduńska Wola
Urząd Gminy Zebrzydowice
Urząd Gminy Zębowice
Urząd Gminy Zgierz
Urząd Gminy Zgorzelec
Urząd Gminy Zielona Góra
Urząd Gminy Zławieś Wielka
Urząd Gminy Złota
Urząd Gminy Złotoryja
Urząd Gminy Złotów
Urząd Gminy Zwierzyn
Urząd Gminy Żabia Wola
Urząd Gminy Żabno
Urząd Gminy Żagań
Urząd Gminy Żarnowiec
Urząd Gminy Żarnów
Urząd Gminy Żary 
Urząd Gminy Żelechlinek
Urząd Gminy Żmudź
Urząd Gminy Żołynia
Urząd Gminy Żółkiewka
Urząd Gminy Żórawina
Urząd Gminy Żukowice
Urząd Gminy Żukowo
Urząd Gminy Żychlin
Urząd Gminy Żyraków
Urząd Gminy Żyrzyn
Urząd Gminy Żytno
Urząd Miasta Aleksandrów Kujawski
Urząd Miasta Augustów
Urząd Miasta Bartoszyce
Urząd Miasta Bełchatowa
Urząd Miasta Bełżyce
Urząd Miasta Biała Podlaska
Urząd Miasta Białogard
Urząd Miasta Bielawa
Urząd Miasta Bielsk Podlaski
Urząd Miasta Bielsko-Biała
Urząd Miasta Biłgoraj
Urząd Miasta Bochnia
Urząd Miasta Bolesławiec
Urząd Miasta Borek Wielkopolski
Urząd Miasta Braniewo
Urząd Miasta Brańsk
Urząd Miasta Brzeg
Urząd Miasta Brzeg Dolny
Urząd Miasta Brzeziny
Urząd Miasta Bukowno
Urząd Miasta Bydgoszcz
Urząd Miasta Chełm
Urząd Miasta Chełmno
Urząd Miasta Chełmża
Urząd Miasta Chojna
Urząd Miasta Chojnice
Urząd Miasta Chorzów
Urząd Miasta Ciechanów
Urząd Miasta Cieszyn
Urząd Miasta Czarna Woda
Urząd Miasta Czarnków
Urząd Miasta Czechowice-Dziedzice
Urząd Miasta Czeladź
Urząd Miasta Częstochowy
Urząd Miasta Człuchów
Urząd Miasta Dąbrowa Górnicza
Urząd Miasta Dębica
Urząd Miasta Dęblin
Urząd Miasta Duszniki Zdrój
Urząd Miasta Dynów
Urząd Miasta Działdowo
Urząd Miasta Dzierżoniów
Urząd Miasta Ełk
Urząd Miasta Frampol
Urząd Miasta Garwolin
Urząd Miasta Gdyni
Urząd Miasta Głogów
Urząd Miasta Gniezna
Urząd Miasta Golub-Dobrzyń
Urząd Miasta Gorzów Śląski
Urząd Miasta Gorzów Wielkopolski
Urząd Miasta Gostynin
Urząd Miasta Gostyń
Urząd Miasta Gozdnica
Urząd Miasta Górowo Iławeckie
Urząd Miasta Grajewo
Urząd Miasta Hajnówka
Urząd Miasta Helu
Urząd Miasta Hrubieszów
Urząd Miasta i Gimny Żelechów
Urząd Miasta i Gminy  Bodzentyn
Urząd Miasta i Gminy Annopol
Urząd Miasta i Gminy Bardo
Urząd Miasta i Gminy Biała Piska
Urząd Miasta i Gminy Biała Rawska
Urząd MIasta i Gminy Błonie
Urząd Miasta i Gminy Bogatynia 
Urząd Miasta i Gminy Brusy
Urząd Miasta i Gminy Buk
Urząd Miasta i Gminy Busko-Zdrój
Urząd Miasta i Gminy Bystrzyca Kłodzka
Urząd Miasta i Gminy Chodecz
Urząd Miasta i Gminy Chorzele
Urząd Miasta i Gminy Cieszanów
Urząd Miasta i Gminy Czarne
Urząd Miasta i Gminy Debrzno
Urząd Miasta i Gminy Dobrzyń nad Wisłą
Urząd Miasta i Gminy Działoszyce
Urząd Miasta i Gminy Góra Kalwaria
Urząd Miasta i Gminy Jabłonowo Pomorskie
Urząd Miasta i Gminy Kalisz Pomorski
Urząd Miasta i Gminy Kazimierza Wielka
Urząd Miasta i Gminy Kąty Wrocławskie
Urząd Miasta i Gminy Kępno
Urząd Miasta i Gminy Kluczbork
Urząd Miasta i Gminy Kłodawa
Urząd Miasta i Gminy Kolonowskie
Urząd Miasta i Gminy Konstancin-Jeziorna
Urząd Miasta i Gminy Koprzywnica
Urząd Miasta i Gminy Kosów Lacki
Urząd Miasta i Gminy Krapkowice
Urząd Miasta i Gminy Lubawka
Urząd Miasta i Gminy Łomianki
Urząd Miasta i Gminy Międzychód
Urząd Miasta i Gminy Mikstat
Urząd Miasta i Gminy Miłomłyn
Urząd Miasta i Gminy Mirsk
Urząd Miasta i Gminy Murowana Goślina
Urząd Miasta i Gminy Myszyniec
Urząd Miasta i Gminy Niepołomice
Urząd Miasta i Gminy Nowa Dęba
Urząd Miasta i Gminy Nowa Sarzyna
Urząd Miasta i Gminy Ogrodzieniec
Urząd Miasta i Gminy Oleszyce
Urząd Miasta i Gminy Opatów
Urząd Miasta i Gminy Ostroróg
Urząd Miasta i Gminy Ożarów Mazowiecki
Urząd Miasta i Gminy Pilica
Urząd Miasta i Gminy Piotrków Kujawski
Urząd Miasta i Gminy Pleszew
Urząd Miasta i Gminy Pobiedziska
Urząd Miasta i Gminy Praszka
Urząd Miasta i Gminy Przedecz
Urząd Miasta i Gminy Radzymin
Urząd Miasta i Gminy Ryn
Urząd Miasta i Gminy Sieniawa
Urząd Miasta i Gminy Siewierz
Urząd Miasta i Gminy Solec Kujawski
Urząd Miasta i Gminy Staszów
Urząd Miasta i Gminy Suchedniów
Urząd Miasta i Gminy Szamotuły
Urząd Miasta i Gminy Szczekociny
Urząd Miasta i Gminy Ścinawa
Urząd Miasta i Gminy Świątniki Górne
Urząd Miasta i Gminy Świerzawa
Urząd Miasta i Gminy Twardogóra
Urząd Miasta i Gminy w Białobrzegach
Urząd Miasta i Gminy w Daleszycach
Urząd Miasta i Gminy w Gniewie
Urząd Miasta i Gminy w Górze
Urząd Miasta i Gminy w Kańczudze
Urząd Miasta i Gminy w Koniecpolu
Urząd Miasta i Gminy w Końskich
Urząd Miasta i Gminy w Kunowie
Urząd Miasta i Gminy w Lipsku
Urząd Miasta i Gminy w Łosicach
Urząd Miasta i Gminy w Mroczy
Urząd Miasta i Gminy w Nakle nad Notecią
Urząd Miasta i Gminy w Okonku
Urząd Miasta i Gminy w Olkuszu
Urząd Miasta i Gminy w Osieku
Urząd Miasta i Gminy w Ożarowie
Urząd Miasta i Gminy w Radzyniu Chełmińskim
Urząd Miasta i Gminy w Wielichowie
Urząd Miasta i Gminy w Wolbromiu
Urząd Miasta i Gminy w Żarkach
Urząd Miasta i Gminy we Wrześni
Urząd Miasta i Gminy Wołów
Urząd Miasta i Gminy Wysoka
Urząd Miasta i Gminy Zawichost
Urząd Miasta i Gminy Złocieniec
Urząd Miasta i Gminy Żmigród
Urząd Miasta Iława
Urząd Miasta Imielin
Urząd Miasta Inowrocław
Urząd Miasta Janowiec Wielkopolski
Urząd Miasta Jarosławia
Urząd Miasta Jasień
Urząd Miasta Jasło
Urząd Miasta Jastarnia
Urząd Miasta Jastrzębie Zdrój
Urząd Miasta Jawor
Urząd Miasta Jaworzno
Urząd Miasta Jedlina-Zdrój
Urząd Miasta Jedwabne
Urząd Miasta Jelenia Góra
Urząd Miasta Józefowa
Urząd Miasta Kalety
Urząd Miasta Kałuszyn
Urząd Miasta Kamienna Góra
Urząd Miasta Kamień Krajeński
Urząd Miasta Kamieńsk
Urząd Miasta Katowice
Urząd Miasta Kazimierz Dolny
Urząd Miasta Kędzierzyn-Koźle
Urząd Miasta Kętrzyn
Urząd Miasta Kielce
Urząd Miasta Kłodzko
Urząd Miasta Knurów
Urząd Miasta Kobylin
Urząd Miasta Kobyłka
Urząd Miasta Kock
Urząd Miasta Kolno
Urząd Miasta Kołobrzeg
Urząd Miasta Konstantynów Łódzki
Urząd Miasta Korfantów
Urząd Miasta Kostrzyn nad Odrą
Urząd Miasta Kościerzyna
Urząd Miasta Kowal
Urząd Miasta Kowalewo Pomorskie
Urząd Miasta Kowary
Urząd Miasta Kożuchów
Urząd Miasta Krakowa
Urząd Miasta Krasnystaw
Urząd Miasta Kraśnik
Urząd Miasta Krosna
Urząd Miasta Krosno Odrzańskie
Urząd Miasta Kruszwica
Urząd Miasta Krynica Morska
Urząd Miasta Krynica-Zdrój
Urząd Miasta Krzanowice
Urząd Miasta Kudowa Zdrój
Urząd Miasta Kutno
Urząd Miasta Kuźnia Raciborska
Urząd Miasta Legionowo
Urząd Miasta Legnica
Urząd Miasta Leszno
Urząd Miasta Leśnica
Urząd Miasta Leżajsk
Urząd Miasta Leżajsk-Gmina Miasto Leżajsk
Urząd Miasta Lębork
Urząd Miasta Lędziny
Urząd Miasta Libiąż
Urząd Miasta Lidzbark Warmiński
Urząd Miasta Limanowa
Urząd Miasta Lipno
Urząd Miasta Lubaczów
Urząd Miasta Lubań
Urząd Miasta Lubartów
Urząd Miasta Lubawa
Urząd Miasta Lublin
Urząd Miasta Luboń
Urząd Miasta Łańcut
Urząd Miasta Łaskarzew
Urząd Miasta Łęczyca
Urząd Miasta Łodzi
Urząd Miasta Łuków
Urząd Miasta Malborka
Urząd Miasta Marki
Urząd Miasta Mielec
Urząd Miasta Mieroszów
Urząd Miasta Międzyrzec Podlaski
Urząd Miasta Mikołów
Urząd Miasta Milicz
Urząd Miasta Mińsk Mazowiecki
Urząd Miasta Mława
Urząd Miasta Mosina
Urząd Miasta Mrągowo
Urząd Miasta Mszana Dolna
Urząd Miasta Mysłowice
Urząd Miasta Myszkowa
Urząd Miasta Myszków
Urząd Miasta Nieszawa
Urząd Miasta Nowe Miasto Lubawskie
Urząd Miasta Nowy Sącz
Urząd Miasta Nowy Targ
Urząd Miasta Nysa
Urząd Miasta Oborniki Śląskie
Urząd Miasta Obrzycko
Urząd Miasta Oleśnicy
Urząd Miasta Olsztyna
Urząd Miasta Opalenica
Urząd Miasta Opoczno
Urząd Miasta Opole
Urząd Miasta Orzesze
Urząd Miasta Ostrołęki
Urząd Miasta Ostrowiec Świętokrzyski
Urząd Miasta Ostróda
Urząd Miasta Ostrów Lubelski
Urząd Miasta Ostrów Wielkopolski
Urząd Miasta Oświęcim
Urząd Miasta Otwock
Urząd Miasta Paczków
Urząd Miasta Piastów
Urząd Miasta Piechowice
Urząd Miasta Piekary Śląskie
Urząd Miasta Pieszyce
Urząd Miasta Piława Górna
Urząd Miasta Piły
Urząd Miasta Pionki
Urząd Miasta Piotrków Trybunalski
Urząd Miasta Płock
Urząd Miasta Pniewy
Urząd Miasta Poręba
Urząd Miasta Poznań
Urząd Miasta Pruszcz Gdański
Urząd Miasta Pruszków
Urząd Miasta Przasnysz
Urząd Miasta Przeworsk
Urząd Miasta Pszów
Urząd Miasta Puck
Urząd Miasta Puławy
Urząd Miasta Pyskowice
Urząd Miasta Rabka-Zdrój
Urząd Miasta Racibórz
Urząd Miasta Radlin
Urząd Miasta Radomska
Urząd Miasta Radymno
Urząd Miasta Radziejów
Urząd Miasta Radzionków
Urząd Miasta Radzyń Podlaski
Urząd Miasta Rajgród
Urząd Miasta Rawa Mazowiecka
Urząd Miasta Recz
Urząd Miasta Reda
Urząd Miasta Rejowiec Fabryczny
Urząd Miasta Ruda Śląska
Urząd Miasta Rumi
Urząd Miasta Rybnika
Urząd Miasta Rydułtowy
Urząd Miasta Rzeszów
Urząd Miasta Sandomierz
Urząd Miasta Sanok
Urząd Miasta Siedlce
Urząd Miasta Siemianowice Śląskie
Urząd Miasta Siemiatycze
Urząd Miasta Sieradz
Urząd Miasta Skarżysko_Kamienna
Urząd Miasta Skarżysko-Kamienna
Urząd Miasta Skierniewice
Urząd Miasta Skoczów
Urząd Miasta Skórcz
Urząd Miasta Sławków
Urząd Miasta Słomniki
Urząd Miasta Słubice
Urząd Miasta Sochaczew
Urząd Miasta Sokółka
Urząd Miasta Sopot
Urząd Miasta Sosnowiec
Urząd Miasta Stalowa Wola
Urząd Miasta Starachowice
Urząd Miasta Stargard Szczeciński
Urząd Miasta Starogard Gdański
Urząd Miasta Stąporków
Urząd Miasta Stoczek Łukowski
Urząd Miasta Stołecznego Warszawy
Urząd Miasta Strzelce Krajeńskie
Urząd Miasta Sulejówek
Urząd Miasta Sulmierzyce
Urząd Miasta Szczecin
Urząd Miasta Szczecinek
Urząd Miasta Szklarska Poręba
Urząd Miasta Śrem
Urząd Miasta Świdnik
Urząd Miasta Świdwin
Urząd Miasta Świebodzin
Urząd Miasta Świeradów-Zdrój
Urząd Miasta Świętochłowice
Urząd Miasta Świnoujście 
Urząd Miasta Tarnobrzeg
Urząd Miasta Tarnowa
Urząd Miasta Tarnowskie Góry
Urząd Miasta Tomaszów Lubelski
Urząd Miasta Tomaszów Mazowiecki
Urząd Miasta Toruń
Urząd Miasta Toszek
Urząd Miasta Trzebinia
Urząd Miasta Tuszyna
Urząd Miasta Tychy
Urząd Miasta Tyszowce
Urząd Miasta Tyszowice
Urząd Miasta Ujazd
Urząd Miasta Uniejów
Urząd Miasta Ustka
Urząd Miasta Ustroń
Urząd Miasta Ustrzyki Dolne
Urząd Miasta w Dziwnowie
Urząd Miasta w Krzyżu Wlkp
Urząd Miasta w Ostrowi Mazowieckiej
Urząd Miasta w Przemkowie
Urząd Miasta w Słupcy
Urząd Miasta w Żyrardowie
Urząd Miasta Wałbrzych
Urząd Miasta Wałcz
Urząd Miasta Wejherowo
Urząd Miasta Węgorzyno
Urząd Miasta Węgrów
Urząd Miasta Władysławowo
Urząd Miasta Włocławek
Urząd Miasta Wodzisław Śląski
Urząd Miasta Wojcieszów
Urząd Miasta Wojkowice
Urząd Miasta Wolin
Urząd Miasta Wolsztyn
Urząd Miasta Wyrzysk
Urząd Miasta Wysokie Mazowieckie
Urząd Miasta Zakopane
Urząd Miasta Zalewo
Urząd Miasta Zambrów
Urząd Miasta Zamość
Urząd Miasta Ząbki
Urząd Miasta Zduńska Wola
Urząd Miasta Zdzieszowice
Urząd Miasta Zgierz
Urząd Miasta Zgorzelec
Urząd Miasta Zielona Góra
Urząd Miasta Zielonka
Urząd Miasta Żagań
Urząd Miasta Żory
Urząd Miasta-Gminy Stryków
Urząd Miejski Gminy Rakoniewice
============================================= ====== ===========


.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`search`
* :ref:`genindex`
* :ref:`modindex`

