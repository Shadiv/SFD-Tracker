import mechanicalsoup as ms
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

browser = ms.Browser()
url = 'https://www.sec.gov/edgar/search/#'
page = browser.get(url)
print(page.soup)