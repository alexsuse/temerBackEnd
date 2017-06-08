"""Checks if Michel Temer is president of Brazil.

Simple library that fetches the english wikipedia page 
for Brazil, parses the html and looks in the infobox to
check if michel temer is the president of Brazil. This
should give us reasonable latency to detect changes as they happen.
"""
from bs4 import BeautifulSoup
import requests

EN_BR_wikipedia_page = "https://en.wikipedia.org/wiki/Brazil"

def getEnWikiPresident():
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(EN_BR_wikipedia_page, headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    infobox = soup.find('table',
                        {'class':'infobox geography vcard'})
    for row in infobox.findAll('tr'):
        headers = row.findAll('th')
        if not headers:
            continue
        header = headers[0]
        if (header.text.endswith("President\n")
            and "Vice" not in header.text):
            cells = row.findAll('td')
            if not cells:
                return  None
            return cells[0].text


if __name__ == "__main__":
    print(getEnWikiPresident())
