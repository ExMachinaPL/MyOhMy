.. _topics-spiders:

========
Pajączki
========

Pajączki (spiders) służą do zbierania danych ze stron BIP. Ze względu na to, 
że każdy z serwisów zazwyczaj posiada inną strukturę dokumentu, każdy z urzędów
ma dedykowanego pajączka.

.. _topics-spiders-naming:

Nazewnictwo pajączków
=====================

Wszystkie pajączki są nazywane wg nastepującej konwencji:

typ-jednostki_nazwa-miasta[_nazwa-jednostki].py

Gdzie typy jednostki są reprezentowane przez następujące skróty:

- **um** - urząd miasta
- **ug** - urząd gminy
- **umg** - urząd miasta i gminy

Nazwy miast pisane są małymi literami bez polskich znaków.

Nazwa jednostki jest elementem opcjonalnym. Pojawia się gdy jednostka urzędu posiada własny BIP.

Przykładowo crawler urzędu miasta Bielsko-Biała będzie miał nazwę:
um_bielsko-biala.py

