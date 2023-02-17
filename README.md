# ELECTIONS SCRAPER - třetí python projekt Engeto akademie



## POPIS APLIKACE
Projekt election srapcer slouží ke stahování vymezené části a následného třídění dat ze stránek statistiského úřadu a to na portále www.volby.cz.

## INSTALACE KNIHOVEN
Použité knihovny, které jsou součástí projektu se nacházejí v souboru requirements.txt.
K tomu aby jste mohli nainstalovat použité knihovny, vytvořte virtuální prostředí a nainstalujte potřebné balíčky:


```
$ pip3 --version # ověření verze manažera

$ pip3 install -r requirements.txt # instalace knihoven
```


## SPUŠTĚNÍ PROGRAMU
Ke spuštění souboru election.py, potřebujete 2 povinné argumenty.

python election.py <"url odkazující na požadované území"> <"název_souboru.csv">

## UKÁZKA PROGRAMU
Výsledky hlasování pro okres Benešov:

1. Argument(URL): '''https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'''

2. Argument(Název souboru): "vysledky_benesov.csv"

### SPUŠTĚNÍ PROGRAMU
python election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_benesov.csv"

### STAHOVÁNÍ
Downloading data from: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"

Saving data to: vysledky_benesov.csv

Data was saved. Exiting program!

### OČEKÁVANÝ VÝSTUP

```
Code,Location,Registered,Envelopers,Valid,...
529303,Benešov,13104,8485,8437,...
532568,Bernartice,191,148,148,...
```

### MOŽNÉ CHYBY
"Program need 2 arguments. URL, CSV file. Exiting program!"

"First argument not correct. Exiting program! "

"Second argument not correct. Exiting program! "
