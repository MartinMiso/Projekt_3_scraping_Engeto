README - Skript pro získání volebních vısledkù

Popis
Tento Python skript stahuje a zpracovává volební vısledky z webu volby.cz. Vısledky se ukládají do CSV souboru, kde jsou dostupné informace o poètu volièù, odevzdanıch obálkách a hlasech pro jednotlivé strany.

Poadavky
* Python 3.x
* Knihovny: requests, BeautifulSoup4, csv
Nainstalujte chybìjící knihovny pomocí:
pip install requests beautifulsoup4

Pouití
Spuste skript s parametry:
python main.py "NAZEV_MESTA" "NAZEV_SOUBORU.csv"

Pøíklad pouití:
python main.py "Olomouc" "vysledky_olomouc.csv"
Tento pøíkaz stáhne a uloí volební vısledky pro mìsto Olomouc do souboru vysledky_olomouc.csv.

Vstupní data
Skript pracuje s daty ze stránek volby.cz, konkrétnì z této URL:
https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

Parametry skriptu
1. Název mìsta – musí pøesnì odpovídat názvu mìsta uvedeného na stránkách volby.cz – tabulka níe
2. Název vıstupního souboru – CSV soubor, do kterého budou vısledky uloeny.
Pokud zadáte název mìsta nesprávnì, skript zobrazí chybu a ukonèí se.

Pøehled obcí podle krajù 
Vısledky hlasování za územní celky – èást Hlavní mìsto PrahaKrálovéhradeckı kraj  Vısledky hlasování za územní celky – èást Královéhradeckı krajÚzemní úroveò  kódnázevÚzemní úroveòCZ0100PrahakódnázevStøedoèeskı krajCZ0521Hradec KrálovéVısledky hlasování za územní celky – èást Støedoèeskı krajCZ0522Jièín  CZ0523NáchodÚzemní úroveòCZ0524Rychnov nad KnìnoukódnázevCZ0525TrutnovCZ0201BenešovPardubickı krajCZ0202BerounVısledky hlasování za územní celky – èást Pardubickı krajCZ0203Kladno  CZ0204KolínÚzemní úroveòCZ0205Kutná HorakódnázevCZ0206MìlníkCZ0531ChrudimCZ0207Mladá BoleslavCZ0532PardubiceCZ0208NymburkCZ0533SvitavyCZ0209Praha-vıchodCZ0534Ústí nad OrlicíCZ020APraha-západKraj VysoèinaCZ020BPøíbramVısledky hlasování za územní celky – èást Kraj VysoèinaCZ020CRakovník  XZahranièíÚzemní úroveòJihoèeskı krajkódnázevVısledky hlasování za územní celky – èást Jihoèeskı krajCZ0631Havlíèkùv Brod  CZ0632JihlavaÚzemní úroveòCZ0633PelhøimovkódnázevCZ0634TøebíèCZ0311Èeské BudìjoviceCZ0635ïár nad SázavouCZ0312Èeskı KrumlovJihomoravskı krajCZ0313Jindøichùv HradecVısledky hlasování za územní celky – èást Jihomoravskı krajCZ0314Písek  CZ0315PrachaticeÚzemní úroveòCZ0316StrakonicekódnázevCZ0317TáborCZ0641BlanskoPlzeòskı krajCZ0642Brno-mìstoVısledky hlasování za územní celky – èást Plzeòskı krajCZ0643Brno-venkov  CZ0644BøeclavÚzemní úroveòCZ0645HodonínkódnázevCZ0646VyškovCZ0321DomaliceCZ0647ZnojmoCZ0322KlatovyOlomouckı krajCZ0323Plzeò-mìstoVısledky hlasování za územní celky – èást Olomouckı krajCZ0324Plzeò-jih  CZ0325Plzeò-severÚzemní úroveòCZ0326RokycanykódnázevCZ0327TachovCZ0711JeseníkKarlovarskı krajCZ0712OlomoucVısledky hlasování za územní celky – èást Karlovarskı krajCZ0713Prostìjov  CZ0714PøerovÚzemní úroveòCZ0715ŠumperkkódnázevZlínskı krajCZ0411ChebVısledky hlasování za územní celky – èást Zlínskı krajCZ0412Karlovy Vary  CZ0413SokolovÚzemní úroveòÚsteckı krajkódnázevVısledky hlasování za územní celky – èást Ústeckı krajCZ0721Kromìøí  CZ0722Uherské HradištìÚzemní úroveòCZ0723VsetínkódnázevCZ0724ZlínCZ0421DìèínMoravskoslezskı krajCZ0422ChomutovVısledky hlasování za územní celky – èást Moravskoslezskı krajCZ0423Litomìøice  CZ0424LounyÚzemní úroveòCZ0425MostkódnázevCZ0426TepliceCZ0801BruntálCZ0427Ústí nad LabemCZ0802Frıdek-MístekLibereckı krajCZ0803KarvináVısledky hlasování za územní celky – èást Libereckı krajCZ0804Novı Jièín  CZ0805OpavaÚzemní úroveòCZ0806Ostrava-mìstokódnázevCZ0511Èeská LípaCZ0512Jablonec nad NisouCZ0513LiberecCZ0514Semily

Funkce

* nacti_hlavni_stranku(url)
o Naète HTML obsah hlavní stránky.
* najdi_odkaz_na_mesto(soup, mesto)
o Najde odkaz na stránku daného mìsta.
* ziskej_vysledne_adresy(soup_city)
o Získá seznam URL adres jednotlivıch obcí.
* ziskej_kod_a_nazev_obce(soup_odkazy, adresa)
o Získá kód a název obce.
* ziskej_udaje_z_tabulky(table_tags)
o Extrahuje údaje o volièích, obálkách a hlasech.
* ziskej_hlasy_pro_strany(table_tags, nazvy_stran)
o Získá hlasy pro jednotlivé strany.
* uloz_vysledky_do_csv(vysledky_list, nazvy_stran, nazev_souboru)
o Uloí vısledky do CSV souboru.

Vıstupní formát CSV
CSV soubor obsahuje:
* Kód obce
* Název obce
* Poèet volièù v seznamu
* Odevzdané obálky
* Platné hlasy
* Poèet hlasù pro kadou politickou stranu
Kadı øádek v CSV odpovídá jedné obci.

Poznámky
* Skript je vytvoøen pro volební vısledky na stránkách https://www.volby.cz/pls/ps2017nss/
* Odkazy a struktura HTML mohou bıt zmìnìny, co mùe vyadovat úpravy kódu.
* Vıstupní CSV soubor pouívá støedník (;) jako oddìlovaè hodnot.

