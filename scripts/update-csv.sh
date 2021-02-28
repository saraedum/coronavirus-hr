#!/bin/bash
set -e

cd "$(dirname "$0")"

./parse-koronavirus-hr.py <(curl -L -v --cookie "__cfduid=d2634b8dadda375deeea23d66af8433141612828153" https://www.koronavirus.hr) >> ../koronavirus.csv

# Eliminate duplicate lines in koronavirus.csv. Sometimes the reported data changes during the day so we only keep the last one we got on that day:
tac ../koronavirus.csv | awk -F"," '!_[$1]++' | tac > ../koronavirus.csv.new
mv ../koronavirus.csv.new ../koronavirus.csv
