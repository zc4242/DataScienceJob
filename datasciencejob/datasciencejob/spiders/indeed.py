# Import scrapy library
import scrapy
# import csv
# import pandas as pd
from bs4 import BeautifulSoup

url_prefix = 'https://www.indeed.com'

# Create the spider class
class YourSpider(scrapy.Spider):
    name = "indeed"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park,+NC&start=']

        for url in urls:
            for i in range(0,10,10):
                url_ = url + str(i)
                yield scrapy.Request(url=url_, callback=self.parse)
    
    def parse(self, response):
        filename = './indeed_pandas.csv'        

        links = response.css('a.jobtitle::attr(href)').extract()
        links = links + response.css('h2.jobtitle > a::attr(href)').extract()
        links = links + response.css('h1.jobtitle > a::attr(href)').extract() 
        links = links + response.css('h3.jobtitle > a::attr(href)').extract()     
        links = ['https://www.indeed.com' + link for link in links]
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_job_page)

        # df = pd.DataFrame(data={'title':titles, 'link':links})
        # df.to_csv(filename, sep=',', index=False, mode='a')

        # with open('./indeed.html', 'wb') as f:
        #      f.write(response.body)

        # with open(filename, 'w', newline='') as f:
        #     wr = csv.writer(f)
        #     for link in links:
        #         link = url_prefix + link
        #         wr.writerow([link])
        # self.log('Saved file')

    def parse_job_page(self, response):
        # yield {
        #     'title': response.css('h3.icl-u-xs-mb--xs.icl-u-xs-mt--none.jobsearch-JobInfoHeader-title::text').extract(),
        #     'company': response.css('div.icl-u-lg-mr--sm.icl-u-xs-mr--xs::text').extract(),
        #     'location': response.css('div.jobsearch-InlineCompanyRating ::text').extract(),
        #     'desc': response.css('div.jobsearch-JobComponent-description ::text').extract(),
        #     'link': response.url
        #     }

        soup = BeautifulSoup(response.text)

        yield {
            'title': soup.find('h3', attrs={'class': 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'}).text,
            'company': soup.find('div', attrs={'class': 'icl-u-lg-mr--sm icl-u-xs-mr--xs'}).text,
            'location': soup.find('div', attrs={'class': 'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'}).text,
            'link': response.url,
            'desc': soup.find('div', attrs={'class': 'jobsearch-JobComponent-description icl-u-xs-mt--md'}).text
            # 'city': soup.find('div', attrs={'class': 'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'}).text.split('-').split(', ').str[0],
            # 'state': soup.find('div', attrs={'class': 'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'}).text.split('-').split(' ').str[1]
        }