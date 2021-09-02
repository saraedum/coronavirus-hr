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
import json

županji = ['bjelovarsko_bilogorska', 'brodsko_posavska', 'dubrovacko_neretvanska', 'grad_zagreb', 'istarska', 'karlovacka', 'koprivnicko_krizevacka', 'krapinsko_zagorska', 'licko_senjska', 'medjimurska', 'osjecko_baranjska', 'pozesko_slavonska', 'primorsko_goranska', 'sibensko_kninska', 'sisacko_moslavacka', 'splitsko_dalmatinska', 'varazdinska', 'viroviticko_podravska', 'vukovarsko_srijemska', 'zadarska', 'zagrebacka']

@click.command()
@click.argument('input', type=click.File('rb'))
def parse(input):
    soup = json.load(input)

    date = datetime.datetime.strptime(soup['lastUpdated'], "%Y-%m-%dT%H:%M:%S.000Z")

    output = [date.strftime("%Y-%m-%d 12:00:00")] + [soup['hrvatska'][ž]['infected'] for ž in županji]
    csv.writer(sys.stdout, delimiter=',').writerow(output)

    if datetime.datetime.now() - date > datetime.timedelta(days=2):
        print(f"Outdated data from {date}.", file=sys.stderr);
        return 1

    print(f"Recent data from {date}.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    exit(parse())
