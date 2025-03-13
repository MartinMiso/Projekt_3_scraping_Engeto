README - Skript pro z�sk�n� volebn�ch v�sledk�

Popis
Tento Python skript stahuje a zpracov�v� volebn� v�sledky z webu volby.cz. V�sledky se ukl�daj� do CSV souboru, kde jsou dostupn� informace o po�tu voli��, odevzdan�ch ob�lk�ch a hlasech pro jednotliv� strany.

Po�adavky
* Python 3.x
* Knihovny: requests, BeautifulSoup4, csv
Nainstalujte chyb�j�c� knihovny pomoc�:
pip install requests beautifulsoup4

Pou�it�
Spus�te skript s parametry:
python main.py "NAZEV_MESTA" "NAZEV_SOUBORU.csv"

P��klad pou�it�:
python main.py "Olomouc" "vysledky_olomouc.csv"
Tento p��kaz st�hne a ulo�� volebn� v�sledky pro m�sto Olomouc do souboru vysledky_olomouc.csv.

Vstupn� data
Skript pracuje s daty ze str�nek volby.cz, konkr�tn� z t�to URL:
https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

Parametry skriptu
1. N�zev m�sta � mus� p�esn� odpov�dat n�zvu m�sta uveden�ho na str�nk�ch volby.cz � tabulka n�e
2. N�zev v�stupn�ho souboru � CSV soubor, do kter�ho budou v�sledky ulo�eny.
Pokud zad�te n�zev m�sta nespr�vn�, skript zobraz� chybu a ukon�� se.

P�ehled obc� podle kraj� 
V�sledky hlasov�n� za �zemn� celky � ��st Hlavn� m�sto PrahaKr�lov�hradeck� kraj��V�sledky hlasov�n� za �zemn� celky � ��st Kr�lov�hradeck� kraj�zemn� �rove���k�dn�zev�zemn� �rove�CZ0100Prahak�dn�zevSt�edo�esk� krajCZ0521Hradec Kr�lov�V�sledky hlasov�n� za �zemn� celky � ��st St�edo�esk� krajCZ0522Ji��n��CZ0523N�chod�zemn� �rove�CZ0524Rychnov nad Kn�nouk�dn�zevCZ0525TrutnovCZ0201Bene�ovPardubick� krajCZ0202BerounV�sledky hlasov�n� za �zemn� celky � ��st Pardubick� krajCZ0203Kladno��CZ0204Kol�n�zemn� �rove�CZ0205Kutn� Horak�dn�zevCZ0206M�ln�kCZ0531ChrudimCZ0207Mlad� BoleslavCZ0532PardubiceCZ0208NymburkCZ0533SvitavyCZ0209Praha-v�chodCZ0534�st� nad Orlic�CZ020APraha-z�padKraj Vyso�inaCZ020BP��bramV�sledky hlasov�n� za �zemn� celky � ��st Kraj Vyso�inaCZ020CRakovn�k��XZahrani���zemn� �rove�Jiho�esk� krajk�dn�zevV�sledky hlasov�n� za �zemn� celky � ��st Jiho�esk� krajCZ0631Havl��k�v Brod��CZ0632Jihlava�zemn� �rove�CZ0633Pelh�imovk�dn�zevCZ0634T�eb��CZ0311�esk� Bud�joviceCZ0635���r nad S�zavouCZ0312�esk� KrumlovJihomoravsk� krajCZ0313Jind�ich�v HradecV�sledky hlasov�n� za �zemn� celky � ��st Jihomoravsk� krajCZ0314P�sek��CZ0315Prachatice�zemn� �rove�CZ0316Strakonicek�dn�zevCZ0317T�borCZ0641BlanskoPlze�sk� krajCZ0642Brno-m�stoV�sledky hlasov�n� za �zemn� celky � ��st Plze�sk� krajCZ0643Brno-venkov��CZ0644B�eclav�zemn� �rove�CZ0645Hodon�nk�dn�zevCZ0646Vy�kovCZ0321Doma�liceCZ0647ZnojmoCZ0322KlatovyOlomouck� krajCZ0323Plze�-m�stoV�sledky hlasov�n� za �zemn� celky � ��st Olomouck� krajCZ0324Plze�-jih��CZ0325Plze�-sever�zemn� �rove�CZ0326Rokycanyk�dn�zevCZ0327TachovCZ0711Jesen�kKarlovarsk� krajCZ0712OlomoucV�sledky hlasov�n� za �zemn� celky � ��st Karlovarsk� krajCZ0713Prost�jov��CZ0714P�erov�zemn� �rove�CZ0715�umperkk�dn�zevZl�nsk� krajCZ0411ChebV�sledky hlasov�n� za �zemn� celky � ��st Zl�nsk� krajCZ0412Karlovy Vary��CZ0413Sokolov�zemn� �rove��steck� krajk�dn�zevV�sledky hlasov�n� za �zemn� celky � ��st �steck� krajCZ0721Krom�����CZ0722Uhersk� Hradi�t��zemn� �rove�CZ0723Vset�nk�dn�zevCZ0724Zl�nCZ0421D���nMoravskoslezsk� krajCZ0422ChomutovV�sledky hlasov�n� za �zemn� celky � ��st Moravskoslezsk� krajCZ0423Litom��ice��CZ0424Louny�zemn� �rove�CZ0425Mostk�dn�zevCZ0426TepliceCZ0801Brunt�lCZ0427�st� nad LabemCZ0802Fr�dek-M�stekLibereck� krajCZ0803Karvin�V�sledky hlasov�n� za �zemn� celky � ��st Libereck� krajCZ0804Nov� Ji��n��CZ0805Opava�zemn� �rove�CZ0806Ostrava-m�stok�dn�zevCZ0511�esk� L�paCZ0512Jablonec nad NisouCZ0513LiberecCZ0514Semily

Funkce

* nacti_hlavni_stranku(url)
o Na�te HTML obsah hlavn� str�nky.
* najdi_odkaz_na_mesto(soup, mesto)
o Najde odkaz na str�nku dan�ho m�sta.
* ziskej_vysledne_adresy(soup_city)
o Z�sk� seznam URL adres jednotliv�ch obc�.
* ziskej_kod_a_nazev_obce(soup_odkazy, adresa)
o Z�sk� k�d a n�zev obce.
* ziskej_udaje_z_tabulky(table_tags)
o Extrahuje �daje o voli��ch, ob�lk�ch a hlasech.
* ziskej_hlasy_pro_strany(table_tags, nazvy_stran)
o Z�sk� hlasy pro jednotliv� strany.
* uloz_vysledky_do_csv(vysledky_list, nazvy_stran, nazev_souboru)
o Ulo�� v�sledky do CSV souboru.

V�stupn� form�t CSV
CSV soubor obsahuje:
* K�d obce
* N�zev obce
* Po�et voli�� v seznamu
* Odevzdan� ob�lky
* Platn� hlasy
* Po�et hlas� pro ka�dou politickou stranu
Ka�d� ��dek v CSV odpov�d� jedn� obci.

Pozn�mky
* Skript je vytvo�en pro volebn� v�sledky na str�nk�ch https://www.volby.cz/pls/ps2017nss/
* Odkazy a struktura HTML mohou b�t zm�n�ny, co� m��e vy�adovat �pravy k�du.
* V�stupn� CSV soubor pou��v� st�edn�k (;) jako odd�lova� hodnot.

