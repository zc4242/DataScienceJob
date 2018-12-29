# Import scrapy library
import scrapy
import csv
import pandas as pd

url_prefix = 'https://www.indeed.com'
# Create the spider class
class YourSpider(scrapy.Spider):
    name = "indeed-css"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park%2C+NC']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        filename = './indeed_pandas.csv'        
        links = response.css('a.jobtitle.turnstileLink::attr(href)').extract()
        links = [url_prefix + link for link in links]
        titles = response.css('a.jobtitle.turnstileLink::attr(title)').extract()

        df = pd.DataFrame(data={'title':titles, 'link':links})
        df.to_csv(filename, sep=',', index=False)

        # with open(filename, 'w', newline='') as f:
        #     wr = csv.writer(f)
        #     for link in links:
        #         link = url_prefix + link
        #         wr.writerow([link])
        self.log('Saved file')
