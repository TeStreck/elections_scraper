# ELECTIONS SCRAPER - 3.projekt PA
program pro stahování výsledků voleb jednotlivých územních celků

# Instalace knihoven
Použité knihovny jsou uloženy do soubory requirements.txt. Pro instalaci doporučuji použít nové virrtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
$ pip3 --version                    # ověření verze manažeru
$ pip3 install -r requirements.txt  # instalace knihoven
```
# Spuštění projektu
Spuštění projektu elections_scraper.py v rámci příkazového řádku požaduje dva povinné argumenty.
```
python elections_scraper.py <odkaz-uzemniho-celku> <vysledny-soubor>
```
Následně se stáhnou výsledky jako soubor s příponou .csv.

# Ukázka projektu
Výsledky hlasování pro okres Beroun:
  1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
  2. argument: beroun.csv

Spuštění projektu: 
```
python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" "beroun.csv"
```
Průběh stahování:
```
Stahuji data z vybraného url: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
Ukládám do souboru: beroun.csv
Ukončuji Elections scraper
```
Částečný výstup:
```
Kód,Obec,Voliči,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
534421,Bavoryně,239,151,150,18,0,0,6,0,8,7,5,2,4,0,0,16,0,0,11,55,0,2,3,0,0,0,2,11,0
531057,Beroun,14 804,9 145,9 076,1 363,16,11,576,1,433,651,140,78,205,8,12,1 290,4,6,641,2 433,3,13,279,2,61,17,12,800,21
```
