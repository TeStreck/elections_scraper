# elections_scraper
program pro stahování výsledků voleb jednotlivých územních celků

# Instalace knihoven
Použité knihovny jsou uloženy do soubory requirements.txt. Pro instalaci doporučuji použít nové virrtuální prostředí a s nainstalovaným manažerem spustit následovně:

$ pip3 --version                    # ověření verze manažeru
$ pip3 install -r requirements.txt  # instalace knihoven

# Spuštění projektu
Spuštění projektu elections_scraper.py v rámci příkazového řádku požaduje dva povinné argumenty.

python elections_scraper.py <odkaz-uzemniho-celku> <vysledny-soubor>

Následně se stáhnou výsledky jako soubor s příponou .csv.

# Ukázka projektu
Výsledky hlasování pro okres Beroun:
  1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
  2. argument: beroun.csv

Spuštění projektu: 
python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" "beroun.csv"

Průběh stahování
