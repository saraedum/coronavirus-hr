#!/usr/bin/env python
r"""
Takes the HTML file served at koronavirus.hr and extracts the ukupno numbers
for every county and prints them as CSV. The format is date, time, and the
county given in the order below.
"""

import click
import sys
import csv
import datetime

from bs4 import BeautifulSoup, NavigableString

županji = ['bjelovarsko-bilogorska', 'brodsko-posavska', 'dubrovacko-neretvanska', 'grad-zagreb', 'istarska', 'karlovacka', 'koprivnicko-krizevacka', 'krapinsko-zagorska-zupanija', 'licko-senjska', 'medjimurska', 'osjecko-baranjska', 'pozesko-slavonska', 'primorsko-goranska', 'sibensko-kninska', 'sisacko-moslavacka', 'splitsko-dalmatinska', 'varazdinska', 'viroviticko-podravska', 'vukovarsko-srijemska', 'zadarska', 'zagrebacka']

@click.command()
@click.argument('input', type=click.File('rb'))
def parse(input):
    soup = BeautifulSoup(input, 'html.parser')

    timestamp = soup.find('span', attrs={"class": "date"})
    date = datetime.datetime.strptime(timestamp.text, "%d.%m.%Y. %H:%M")

    zarazeni = soup.findAll('text', attrs={"class": "zarazeni"})
    zarazeni = { z['data-url'].split('/')[3]: int(z.text.replace('.', '')) for z in zarazeni if z['data-url']}

    output = [date.strftime("%Y-%m-%d 12:00:00")] + [zarazeni.get(ž, 0) for ž in županji]
    csv.writer(sys.stdout, delimiter=',').writerow(output)

    if datetime.datetime.now() - date > datetime.timedelta(days=2):
        print(f"Outdated data from {date}.", file=sys.stderr);
        return 1

    print(f"Recent data from {date}.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    exit(parse())
