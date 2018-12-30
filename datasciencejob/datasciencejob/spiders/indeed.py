# Import scrapy library
import scrapy
# import csv
import pandas as pd

url_prefix = 'https://www.indeed.com'
# Create the spider class
class YourSpider(scrapy.Spider):
    name = "indeed"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park,+NC&start=']

        for url in urls:
            for i in range(0,100,10):
                url_ = url + str(i)
                yield scrapy.Request(url=url_, callback=self.parse)
    
    def parse(self, response):
        filename = './indeed_pandas.csv'        

        links = response.css('a.jobtitle.turnstileLink::attr(href)').extract()
        links = links + response.css('h2.jobtitle > a::attr(href)').extract()      
        links = ['https://www.indeed.com' + link for link in links]
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_job_page)

        # df = pd.DataFrame(data={'title':titles, 'link':links})
        # df.to_csv(filename, sep=',', index=False, mode='a')

        # with open('./indeed.html', 'wb') as f:
        #     f.write(response.body)

        # with open(filename, 'w', newline='') as f:
        #     wr = csv.writer(f)
        #     for link in links:
        #         link = url_prefix + link
        #         wr.writerow([link])
        self.log('Saved file')

    def parse_job_page(self, response):
        pass
