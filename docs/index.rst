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
Urząd Miasta Szczecinek
Urząd Miasta Szklarska Poręba
Urząd Miasta Śrem
Urząd Miasta Świdnik
Urząd Miasta Świdwin
Urząd Miasta Świebodzin
Urząd Miasta Świeradów-Zdrój
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
============================================= ====== ===========


.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`search`
* :ref:`genindex`
* :ref:`modindex`

