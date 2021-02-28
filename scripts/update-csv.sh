#!/bin/bash
set -e

cd "$(dirname "$0")"

tmp=`mktemp`
# The cloudflare setup seems to rate limit github so we get 503 errors. Use an open proxy instead.
http_proxy=192.109.165.129 wget https://www.koronavirus.hr -O $tmp

./parse-koronavirus-hr.py $tmp >> ../koronavirus.csv

# Eliminate duplicate lines in koronavirus.csv. Sometimes the reported data changes during the day so we only keep the last one we got on that day:
tac ../koronavirus.csv | awk -F"," '!_[$1]++' | tac > ../koronavirus.csv.new
mv ../koronavirus.csv.new ../koronavirus.csv
