import requests
import csv
from bs4 import BeautifulSoup
from scrapy import Selector
url_prefix = 'https://www.indeed.com'
url_nopage = 'https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park%2C+NC'
url = 'https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park,+NC&start=10'
html = requests.get(url).content

sel = Selector(text=html)
links = sel.css('a.jobtitle.turnstileLink::attr(href)').extract()
sel.css('h2.jobtitle > a::attr(herf)').extract()

filename = './indeed1.csv'

with open(filename, 'w', newline='') as f:
    wr = csv.writer(f)
    for link in links:
        link = url_prefix + link
        wr.writerow([link])
