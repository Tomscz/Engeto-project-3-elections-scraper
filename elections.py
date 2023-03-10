"""
Project no.3 Engeto Python Academy
author: Tomáš Šmíd
email: tomas.smid@gmail.com
discord: Tomáš Š#9081
"""


import requests
import sys
from bs4 import BeautifulSoup as bs
import pandas as pd


def response_server(url):
    """This function gets and parses the data from the requested url"""
    response = requests.get(url)
    soup = bs(response.content, "html.parser")
    return soup


def locations_all(soup):
    """This function retrieves the names of individual municipalities"""
    locations_all = soup.find_all("td", {"class": "overflow_name"})
    locations = [location.text for location in locations_all]
    return locations


def codes_cities(soup):
    """This function retrieves the codes of individual municipalities"""
    codes_cities = soup.find_all("td", {"class": "cislo"})
    codes = [code.text for code in codes_cities]
    return codes


def parties_all(url_sub, codes):
    """This function retrieves the names of individual political parties"""
    for code in codes:
        url = f"{url_sub}{code}"
        soup = response_server(url)
        parties_soup = soup.find_all("td", {"class": "overflow_name", "headers": ["t1sa1 t1sb2", "t2sa1 t2sb2"]})
        parties = [party.text for party in parties_soup]
    return parties


def data_collector(url_sub, codes, locations, parties):
    """This function collects, sorts and completes all the data"""
    registered = []
    envelopers = []
    valid = []
    data_votes = []
    for code in codes:
        url = f"{url_sub}{code}"
        soup = response_server(url)
        registered.append(soup.find("td", {"class": "cislo", "headers": "sa2"}).text.replace(" ", "").replace('\xa0', ''))
        envelopers.append(soup.find("td", {"class": "cislo", "headers": "sa3"}).text.replace(" ", "").replace('\xa0', ''))
        valid.append(soup.find("td", {"class": "cislo", "headers": "sa6"}).text.replace(" ", "").replace('\xa0', ''))
        votes = soup.find_all("td", {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        votes_clear = [vote.text.replace(" ", "").replace('\xa0', '') for vote in votes]
        data_votes.append(votes_clear)
        data_1 = {'Code': codes, 'Location': locations, 'Registered': registered, 'Envelopers': envelopers, 'Valid': valid}
        data_2 = {a: [data_votes[b][c] for b in range(len(data_votes)) for c, d in enumerate(parties) if d == a] for a in parties}
        data_all = {**data_1, **data_2}
    return data_all


def csv_maker(data_all, csv_file):
    """This function converts and stores data from data_collector to CSV"""
    df = pd.DataFrame.from_dict(data_all)
    print ("Printing file into CSV File! ")
    df.to_csv(csv_file, index=False)
    return df


def arguments():
    """This function checks for valid arguments so that the program can run"""
    if len(sys.argv) != 3:
        print(f"Program need 2 arguments to run: URL and CSV file name. Exiting program! ")
        sys.exit()
    if not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print(f"First argument  is not correct. Exiting program! ")
        sys.exit()
    if not sys.argv[2].endswith(".csv"):
        print(f"Second argument  is not correct. Exiting program! ")
        sys.exit()
    else:
        print(f"Downloading data from: {sys.argv[1]} ")


def main():
    """Main function to run"""
    arguments()
    csv_file = sys.argv[2]
    url = sys.argv[1]
    url_sub = f"https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec="
    soup=response_server(url)
    codes=codes_cities(soup)
    locations=locations_all(soup)
    parties=parties_all(url_sub, codes)
    data_all=data_collector(url_sub, codes, locations, parties)
    csv_maker(data_all,csv_file)
    print(f"Data was saved into file: {csv_file}. Exiting program! ")


if __name__ == '__main__':
    main()
