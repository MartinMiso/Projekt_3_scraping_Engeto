import csv
import requests
from bs4 import BeautifulSoup as bs
import sys

def nacti_hlavni_stranku(url):
    """
    Načte hlavní stránku z URL a vrátí objekt BeautifulSoup pro analýzu HTML.

    Parameters:
        url (str): URL hlavní stránky pro načtení.

    Returns:
        BeautifulSoup: Načtený a zparsovaný HTML obsah.
    """
    response = requests.get(url)
    return bs(response.text, "html.parser")

def najdi_odkaz_na_mesto(soup, mesto):
    """
    Najde odkaz na stránku města podle jeho názvu na hlavní stránce.

    Parameters:
        soup (BeautifulSoup): Objekt BeautifulSoup obsahující hlavní stránku.
        mesto (str): Název města pro hledání odkazu.

    Returns:
        str or None: Odkaz na stránku města nebo None, pokud není nalezen.
    """
    for td in soup.find_all("td"):
        if td.get_text(strip=True) == mesto:
            row = td.find_parent("tr")
            tds = row.find_all("td")
            if len(tds) > 1:
                link_td = tds[3]
                a_tag = link_td.find("a")
                if a_tag:
                    return a_tag.get("href")
    return None

def ziskej_vysledne_adresy(soup_city):
    """
    Získá všechny výsledné adresy (odkazy na stránky obcí) z dané stránky města.

    Parameters:
        soup_city (BeautifulSoup): Objekt BeautifulSoup obsahující stránku města.

    Returns:
        list: Seznam URL adres pro každou obec.
    """
    vysledna_adresa = []
    for row in soup_city.find_all("tr"):
        tds = row.find_all("td")
        if len(tds) >= 2:
            link_td = tds[0]
            a_tag = link_td.find("a")
            if a_tag:
                relative_url = a_tag.get("href")
                base_url = "https://www.volby.cz/pls/ps2017nss/"
                full_url = base_url + relative_url if not relative_url.startswith("http") else relative_url
                vysledna_adresa.append(full_url)
    return vysledna_adresa

def ziskej_kod_a_nazev_obce(soup_odkazy, adresa):
    """
    Získá kód a název obce z dané stránky na základě URL.

    Parameters:
        soup_odkazy (BeautifulSoup): Objekt BeautifulSoup obsahující stránku s výsledky.
        adresa (str): URL adresa pro získání kódu obce.

    Returns:
        tuple: Kód obce (str), název obce (str).
    """
    kod_obce = adresa.split("xobec=")[-1].split("&")[0]
    try:
        h3_tags = soup_odkazy.find("div", {"class": "topline"}).find_all("h3")
        obec = h3_tags[2].get_text(strip=True).split(": ")[1]
    except Exception as e:
        print(f"Chyba při získávání názvu obce pro kód {kod_obce}: {e}")
        obec = "Neznámá"
    return kod_obce, obec

def ziskej_udaje_z_tabulky(table_tags):
    """
    Získá údaje o voličích, odevzdaných obálkách a platných hlasech z tabulky.

    Parameters:
        table_tags (list): Seznam objektů BeautifulSoup pro tabulky na stránce.

    Returns:
        dict: Slovník s údaji o voličích, obálkách a hlasech.
    """
    udaje = {}
    if len(table_tags) >= 1:
        table_top = table_tags[0]
        for trs in table_top.find_all("tr"):
            tds = trs.find_all("td")
            if len(tds) >= 8:
                udaje["Voliči v seznamu"] = tds[3].text.strip().replace('\xa0', '')
                udaje["Odevzdané obálky"] = tds[4].text.strip().replace('\xa0', '')
                udaje["Platné hlasy"] = tds[7].text.strip().replace('\xa0', '')
    return udaje

def ziskej_hlasy_pro_strany(table_tags, nazvy_stran):
    """
    Získá hlasy pro jednotlivé strany z tabulky a přidá názvy stran do setu.

    Parameters:
        table_tags (list): Seznam objektů BeautifulSoup pro tabulky na stránce.
        nazvy_stran (set): Set pro uložení názvů stran.

    Returns:
        dict: Slovník s názvy stran a počtem hlasů.
    """
    hlasy_stran = {}
    if len(table_tags) >= 2:
        table_strany = table_tags[1]
        for trs in table_strany.find_all("tr"):
            tds = trs.find_all("td")
            if len(tds) >= 4:
                strana = tds[1].text.strip()
                hlasy = tds[2].text.strip().replace('\xa0', '')
                nazvy_stran.add(strana)
                hlasy_stran[strana] = hlasy
    return hlasy_stran

def uloz_vysledky_do_csv(vysledky_list, nazvy_stran, nazev_souboru):
    """
    Uloží výsledky voleb do CSV souboru.

    Parameters:
        vysledky_list (list): Seznam slovníků s výsledky pro jednotlivé obce.
        nazvy_stran (set): Set názvů stran.
        nazev_souboru (str): Název souboru, do kterého se výsledky uloží.
    """
    nazvy_stran = sorted(nazvy_stran)
    with open(nazev_souboru, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Kód obce", "Obec", "Voliči v seznamu", "Odevzdané obálky", "Platné hlasy"] + nazvy_stran)
        for obecni_vysledky in vysledky_list:
            row = [
                obecni_vysledky.get("Kód obce", ""),
                obecni_vysledky.get("Obec", ""),
                obecni_vysledky.get("Voliči v seznamu", "0"),
                obecni_vysledky.get("Odevzdané obálky", "0"),
                obecni_vysledky.get("Platné hlasy", "0"),
            ] + [obecni_vysledky.get(strana, "0") for strana in nazvy_stran]
            writer.writerow(row)

def main():
    """
    Hlavní funkce pro spuštění skriptu. Načítá data z webu, zpracovává je
    a ukládá do CSV souboru na základě argumentů zadaných při spuštění.
    """
    if len(sys.argv) != 3:
        print("Použití: python <script.py (main.py)> <název_obce ('např. Olomouc')> <název_souboru.csv (např. 'vysledky_olomouc.csv')>")
        sys.exit(1)

    # Načtení názvu města a názvu souboru z argumentů
    mesto = sys.argv[1]
    nazev_souboru = sys.argv[2]

    # Hlavní URL pro získání seznamu měst
    url = "https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    soup_hlavni = nacti_hlavni_stranku(url)
    odkaz_mesto = najdi_odkaz_na_mesto(soup_hlavni, mesto)

    if not odkaz_mesto:
        print(f"Nebyl nalezen odkaz pro město {mesto}.")
        sys.exit(1)

    # URL pro město
    url_city = f"https://www.volby.cz/pls/ps2017nss/{odkaz_mesto}"
    print(f"Nalezený odkaz pro {mesto}: {url_city}")
    soup_city = nacti_hlavni_stranku(url_city)
    vysledna_adresa = ziskej_vysledne_adresy(soup_city)

    vysledky_list = []
    nazvy_stran = set()

    # Získání výsledků pro jednotlivé obce
    for adresa in vysledna_adresa:
        odkazy = requests.get(adresa)
        soup_odkazy = bs(odkazy.text, "html.parser")
        kod_obce, obec = ziskej_kod_a_nazev_obce(soup_odkazy, adresa)
        obecni_vysledky = {"Kód obce": kod_obce, "Obec": obec}
        obecni_vysledky.update(ziskej_udaje_z_tabulky(soup_odkazy.find_all("table", {"class": "table"})))
        obecni_vysledky.update(ziskej_hlasy_pro_strany(soup_odkazy.find_all("table", {"class": "table"}), nazvy_stran))
        vysledky_list.append(obecni_vysledky)

    # Uložení výsledků do CSV
    uloz_vysledky_do_csv(vysledky_list, nazvy_stran, nazev_souboru)
    print(f"Výsledky uloženy do souboru '{nazev_souboru}'.")

if __name__ == "__main__":
    main()
