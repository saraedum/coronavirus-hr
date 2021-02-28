#!/usr/bin/env python
r"""
Download a web page with Selenium to work around Cloudflare protections on
koronavirus.hr that block github.com.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from sys import stderr

options = Options()
options.headless=True

print("Spawning Firefox", file=stderr)
driver = webdriver.Firefox(options=options)

print("Visiting koronavirus.hr", file=stderr)
driver.get('https://www.koronavirus.hr')

print("Waiting for CloudFlare checks to clear", file=stderr)
element = WebDriverWait(driver, 30).until(expected_conditions.title_contains('informacije o koronavirusu'))

print(driver.page_source, file=stderr)
print(driver.page_source)
