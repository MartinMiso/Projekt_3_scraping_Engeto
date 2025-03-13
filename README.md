# Projekt_3_Engeto
repository for study project

README - Skript pro získání volebních výsledků

Popis
Tento Python skript stahuje a zpracovává volební výsledky z webu volby.cz. Výsledky se ukládají do CSV souboru, kde jsou dostupné informace o počtu voličů, odevzdaných obálkách a hlasech pro jednotlivé strany.

Požadavky
* Python 3.x
* Knihovny: requests, BeautifulSoup4, csv
Nainstalujte chybějící knihovny pomocí:
pip install requests beautifulsoup4

Použití
Spusťte skript s parametry:
python main.py "NAZEV_MESTA" "NAZEV_SOUBORU.csv"

Příklad použití:
python main.py "Olomouc" "vysledky_olomouc.csv"
Tento příkaz stáhne a uloží volební výsledky pro město Olomouc do souboru vysledky_olomouc.csv.

Vstupní data
Skript pracuje s daty ze stránek volby.cz, konkrétně z této URL:
https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

Parametry skriptu
1. Název města – musí přesně odpovídat názvu města uvedeného na stránkách volby.cz – tabulka níže
2. Název výstupního souboru – CSV soubor, do kterého budou výsledky uloženy.
Pokud zadáte název města nesprávně, skript zobrazí chybu a ukončí se.

Přehled obcí podle krajů 
Seznam obcí podle krajů z volebního webu

Hlavní město Praha
Praha

Středočeský kraj
Benešov
Beroun
Kladno
Kolín
Kutná Hora
Mělník
Mladá Boleslav
Nymburk
Praha-východ
Praha-západ
Příbram
Rakovník

Jihočeský kraj
České Budějovice
Český Krumlov
Jindřichův Hradec
Písek
Prachatice
Strakonice
Tábor
Plzeňský kraj
Domažlice
Klatovy
Plzeň-město
Plzeň-jih
Plzeň-sever
Rokycany
Tachov

Karlovarský kraj
Cheb
Karlovy Vary
Sokolov
Ústecký kraj
Děčín
Chomutov
Litoměřice
Louny
Most
Teplice
Ústí nad Labem

Liberecký kraj
Česká Lípa
Jablonec nad Nisou
Liberec
Semily

Královéhradecký kraj
Hradec Králové
Jičín
Náchod
Rychnov nad Kněžnou
Trutnov

Pardubický kraj
Chrudim
Pardubice
Svitavy
Ústí nad Orlicí

Kraj Vysočina
Havlíčkův Brod
Jihlava
Pelhřimov
Třebíč
Žďár nad Sázavou
Jihomoravský kraj
Blansko
Brno-město
Brno-venkov
Břeclav
Hodonín
Vyškov
Znojmo

Olomoucký kraj
Jeseník
Olomouc
Prostějov
Přerov
Šumperk

Zlínský kraj
Kroměříž
Uherské Hradiště
Vsetín
Zlín

Moravskoslezský kraj
Bruntál
Frýdek-Místek
Karviná
Nový Jičín
Opava
Ostrava-město

Funkce

* nacti_hlavni_stranku(url)
o Načte HTML obsah hlavní stránky.
* najdi_odkaz_na_mesto(soup, mesto)
o Najde odkaz na stránku daného města.
* ziskej_vysledne_adresy(soup_city)
o Získá seznam URL adres jednotlivých obcí.
* ziskej_kod_a_nazev_obce(soup_odkazy, adresa)
o Získá kód a název obce.
* ziskej_udaje_z_tabulky(table_tags)
o Extrahuje údaje o voličích, obálkách a hlasech.
* ziskej_hlasy_pro_strany(table_tags, nazvy_stran)
o Získá hlasy pro jednotlivé strany.
* uloz_vysledky_do_csv(vysledky_list, nazvy_stran, nazev_souboru)
o Uloží výsledky do CSV souboru.

Výstupní formát CSV
CSV soubor obsahuje:
* Kód obce
* Název obce
* Počet voličů v seznamu
* Odevzdané obálky
* Platné hlasy
* Počet hlasů pro každou politickou stranu
Každý řádek v CSV odpovídá jedné obci.

Poznámky
* Skript je vytvořen pro volební výsledky na stránkách https://www.volby.cz/pls/ps2017nss/
* Odkazy a struktura HTML mohou být změněny, což může vyžadovat úpravy kódu.
* Výstupní CSV soubor používá středník (;) jako oddělovač hodnot.


