#!/usr/bin/env python

import cloudscraper

scraper = cloudscraper.create_scraper()
print(scraper.get("https://www.koronavirus.hr").text)
