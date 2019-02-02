# Import scrapy library
import scrapy
import re
import requests
# import urllib
# import csv
# import pandas as pd
from bs4 import BeautifulSoup

url_prefix = 'https://www.indeed.com'

# Create the spider class
class YourSpider(scrapy.Spider):
    name = "indeed"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.indeed.com/jobs?q=data+science&l=NC&limit=50&start=',
        ]

        for url in urls:
            for i in range(0,50,50):
                url_ = url + str(i)
                yield scrapy.Request(url=url_, callback=self.parse)
    
    def parse(self, response):
        
        links = response.css('a.turnstileLink::attr(href)').extract()
        # links = links + response.css('h2.jobtitle > a::attr(href)').extract()
        links = [re.search('clk\?jk=(\w+)\&',link).group(1) for link in links if re.search('clk\?jk', link) is not None]
        links = ['https://www.indeed.com/viewjob?jk=' + link for link in links]


        # for link in links:
        #     if re.match('^//rc', link):

        # links = [link if re.match('^http', link) else 'https://www.indeed.com' + link for link in links]
        
        # links_new = []

        # for link in links:
        #     link_ = urllib.request.urlopen(link).geturl()
        #     if re.search('viewjob', link_):
        #         links_new.append(re.search('(^[\w./:-/?]+)&', link_).group(1))
        #     else:
        #         links_new.append(re.search('(^[\w./:-]+)?', link_).group(1))

        # for string in links:
        #     if re.match('viewjob', string):
        #         links_new.append(re.search('(^[\w./:-?]+)&', string).group(1))
        #     else:
        #         links_new.append(re.search('(^[\w./:-]+)?', string).group())
        
        for link in links:
            # need to short the urls
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

    # def parse_url(self, response):
    #     link_ = response.url
    #     print(link_)
    #     if re.search('viewjob', link_):
    #         link = re.search('(^[\w./:-/?]+)&', link_).group(1)
    #     else:
    #         link = re.search('(^[\w./:-]+)?', link_).group(1)
    #     print(link_)

    #     yield scrapy.Request(url=link_, callback=self.parse_job_page)

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