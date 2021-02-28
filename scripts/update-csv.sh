#!/bin/bash
set -e

cd "$(dirname "$0")"

./parse-koronavirus-hr.py <(curl --request GET --url 'https://api.scrapingant.com/v1/general?url=https%3A%2F%2Fkoronavirus.hr' --header 'x-api-key: 6fe6249e2eb24c0fb61462cc4e290e47') >> ../koronavirus.csv

# Eliminate duplicate lines in koronavirus.csv. Sometimes the reported data changes during the day so we only keep the last one we got on that day:
tac ../koronavirus.csv | awk -F"," '!_[$1]++' | tac > ../koronavirus.csv.new
mv ../koronavirus.csv.new ../koronavirus.csv
