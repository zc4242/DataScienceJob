import requests
import csv
from bs4 import BeautifulSoup
from scrapy import Selector
url_prefix = 'https://www.indeed.com'
url_nopage = 'https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park%2C+NC'
url = 'https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park,+NC&start=10'

html = requests.get(url).content

response = Selector(text=html)

links = response.css('a.jobtitle.turnstileLink::attr(href)').extract()
links = links + response.css('h2.jobtitle > a::attr(href)').extract()
titles = response.css('a.jobtitle.turnstileLink::attr(title)').extract()
titles = titles + response.css('h2.jobtitle > a::attr(title)').extract()
        
linksr = ["https://www.indeed.com" + link for link in links]


filename = './indeed_test.csv'

with open(filename, 'w', newline='') as f:
    wr = csv.writer(f)
    for link in links:
        link = url_prefix + link
        wr.writerow([link])
