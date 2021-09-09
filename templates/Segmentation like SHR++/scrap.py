import requests
from bs4 import BeautifulSoup
import csv

def scrap_html(input):
    website = requests.get("https://sanskrit.inria.fr/cgi-bin/SKT/sktgraph.cgi?lex=SH&st=t&us=f&font=roma&text=raamasya+bhaaryaa+siitaa+tasya+anuja.h+lak.sma.na.h+ca+raame.na+saha+vanam+gacchata.h&t=VH&topic=&mode=g&corpmode=&corpdir=&sentno=")
    # print(website.status_code)
    soup = BeautifulSoup(website.text, 'html.parser')
    # print(soup)
    description = soup.select_one('.center')
    links_right = soup.find_all('a', {"class": "green"})
    links_wrong = soup.find_all('a',{"class":"red"})
    print(links_right)
    print(len(links_right))
    print(links_wrong)
    print(len(links_wrong))
    print(type(links_right))
    description = str(description)
    description = description.replace("/cgi-bin/SKT/sktgraph.cgi?","https://sanskrit.inria.fr/cgi-bin/SKT/sktgraph.cgi?")
    # print(description)
    return description
