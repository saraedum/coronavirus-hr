#!/bin/bash
set -e

cd "$(dirname "$0")"

tmp=`mktemp`
wget https://www.koronavirus.hr -O $tmp

./parse-koronavirus-hr.py $tmp >> ../koronavirus.csv

# Eliminate duplicate lines in koronavirus.csv. Sometimes the reported data changes during the day so we only keep the last one we got on that day:
tac ../koronavirus.csv | awk -F"," '!_[$1]++' | tac > ../koronavirus.csv.new
mv ../koronavirus.csv.new ../koronavirus.csv
