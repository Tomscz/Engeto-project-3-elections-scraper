# ELECTIONS SCRAPER
## the third project of the python Engeto Academy



## APPLICATION DESCRIPTION
The election sraper project is used to download a defined part and then sort data from the website of the statistical office on the portal www.volby.cz. You can choose any district for scraping and than name the resulting file according to your requirements but the file extension must be csv.

## INSTALLATION OF LIBRARIES
The used libraries that are part of the project are located in the requirements.txt file.
To be able to install the used libraries, create a virtual environment and install the necessary packages:


```
$ pip3 --version # manager version verification

$ pip3 install -r requirements.txt # installing libraries
```


## STARTING THE PROGRAM
To run the election.py file, you need 2 mandatory arguments.

python election.py <"url referring to the desired territory"> <"filename.csv">

## SAMPLE PROGRAM (EXAMPLE)
Voting results for the Benešov district:

If you want to take result from Benešov district, in terminal (pycharm) you have to input link of this district and your own name of exported csv file, for example Benesov.csv. Or you can input any district you want and any name of exported file.

1. Argument(URL): '''https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'''

2. Argument(filename): "Benesov.csv"

### STARTING THE PROGRAM
python election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "Benesov.csv"

### DOWNLOADING
Downloading data from: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"

Saving data to: Benesov.csv

Data was saved. Exiting program!

### EXPECTED OUTPUT

```
Code,Location,Registered,Envelopers,Valid,...
529303,Benešov,13104,8485,8437,...
532568,Bernartice,191,148,148,...
```

### POSSIBLE ERRORS
"Program need 2 arguments. URL, CSV file. Exiting program!"

"First argument not correct. Exiting program! "

"Second argument not correct. Exiting program! "
