# ELECTIONS SCRAPER - the third project of the python Engeto Academy



## APPLICATION DESCRIPTION
The election srapcer project is used to download a defined part and then sort data from the website of the statistical office on the portal www.volby.cz.

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

## SAMPLE PROGRAM
Voting results for the Benešov district:

1. Argument(URL): '''https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101'''

2. Argument(filename): "result.csv"

### STARTING THE PROGRAM
python election.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "result.csv"

### DOWNLOADING
Downloading data from: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"

Saving data to: result.csv

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
