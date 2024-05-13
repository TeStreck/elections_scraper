"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Tereza Streckerová
email: tereza.vack@gmail.com
discord: te.str
"""

import requests
from bs4 import BeautifulSoup
import os
import csv
import sys


def get_municipalities(url):
    """
    Získání tabulky obcí a rozparsování pomocí BeautifulSoup
    :param url: url stránky se soupisem obcí, poskytnuté jako první argument
    :return: tabulka obcí """
    request = requests.get(url)
    pars_html = BeautifulSoup(request.text, features="html.parser")
    tab_municipality = pars_html.find_all("tr")[2:]
    return tab_municipality

def get_code_name(tab_municipality, url):
    """
    Získání kodu a názvu obce z tabulky obcí, úprava URL na proklik do jednotlivých obcí
     pro získání dalších dat. Funkce obsahuje vnořenou funkci, která zpracovává další část dat
     :param tab_municipality: tabulka obcí
     :param url: url stránky se soupisem obcí, poskytnuté jako první argument
     :return: list s daty kod obce, název obce, počet voličů, vydaných obálek a plátných hlasů a hlasy jedn. stran
    """
    results = []
    base_url = os.path.dirname(url)
    for i in tab_municipality:
        code = i.find( "td", {"class": "cislo"})
        if code == None:
            continue
        code = code.a.get_text()
        url_row = i.td.a.get('href')
        name = i.find("td", {"class": "overflow_name"}).get_text()
        url_page = base_url + "/" + url_row

        get_data_page_detail(url_page, code, name, results)
    return results

def get_data_page_detail(url_page, code, name, results):
    """
    Získání dat ze dvou tabulek - celkové počty voličů, platných hlasů a vydaných obálek
    a tabulka hlasů jednotlivých stran
    :param url_page: vytvořené url na získání dat obcí z jednotlivých prokliků
    :param code: kod obce
    :param name: název obce
    :param results: výsledný list se všemi daty
    """
    page_detail = requests.get(url_page)
    page_html = BeautifulSoup(page_detail.text, features="html.parser")
    volici = page_html.find("td", {"headers": "sa2"}).get_text()
    vydane_obalky = page_html.find("td", {"headers": "sa3"}).get_text()
    platne_hlasy = page_html.find("td", {"headers": "sa6"}).get_text()
    csv_row = {
        "Kód": code,
        "Obec": name,
        'Voliči': volici,
        'Vydané obálky': vydane_obalky,
        'Platné hlasy': platne_hlasy}
    tab_votes = page_html.find_all("tr")[5:]
    for row in tab_votes:
        columns = row.find_all("td")
        if (columns !=[]):
            parties = columns[1].text
            votes = columns[2].text
            if parties == '-':
                continue
            csv_row[parties] = votes
    results.append(csv_row)

def export_csv(results):
    """
    Export tabulky .csv se získanými daty o volbách
    :param results: výsledný list se všemi daty
    """
    output_file = sys.argv[2]
    with open(output_file, mode="w", newline='', encoding="utf-8") as new_file:
        header = results[0].keys()
        writer = csv.DictWriter(new_file, fieldnames=header)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print("Ukládám do souboru:", output_file)
    return


def main():
    """
    Hlavní funkce, ve které jsou definovány argumenty, kterými se program spouští, a také volání jednotlivých fcí
    """
    if len(sys.argv) != 3:
        print("Napiš dva argumenty")
        exit(1)
    url = sys.argv[1]
    tab_municipality = get_municipalities(url)
    print("Stahuji data z vybraného url:", url)
    code_name = get_code_name(tab_municipality, url)
    export_csv(code_name)
    print("Ukončuji Election Scraper")
    return


if __name__ == "__main__":
    main()
