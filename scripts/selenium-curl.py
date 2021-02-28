#!/usr/bin/env python
r"""
Download a web page with Selenium to work around Cloudflare protections on
koronavirus.hr that block github.com.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from sys import stderr

options = Options()
options.headless=True

print("Spawning Firefox", file=stderr)
driver = webdriver.Firefox(options=options)

print("Visiting koronavirus.hr", file=stderr)
driver.get('https://www.koronavirus.hr')

print("Waiting for CloudFlare checks to clear", file=stderr)
sleep(10)

print(driver.page_source, file=stderr)
print(driver.page_source)
