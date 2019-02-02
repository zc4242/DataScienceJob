import scrapy
import re
from bs4 import BeautifulSoup

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL ','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

# Create the spider class
class YourSpider(scrapy.Spider):
    name = "indeed_state"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.indeed.com/jobs?q=data+science&l=',
        ]

        for url in urls:
            for state in states:
                url_ = url + state
                yield scrapy.Request(url=url_, callback=self.parse_state)
    
    def parse_state(self, response):
        link = response.url
        location = re.search('l-([\w]+)',link).group(1)
        searchcount = response.css('div#searchCount::text').extract().toreplace(',','')
        # count = re.search('([\d]+) jobs',searchcount).group(1)
        
        yield {
            'location': location,
            # 'count': count,
            # 'link': link,
            'searchcount': searchcount
        }