# Import scrapy library
import scrapy

url = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Create the spider class
class YourSpider(scrapy.Spider):
    name = "your_spider"
    # start_requests method
    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # def parse(self, response):
    #     link = response.css('div.course-block > a::attr(href)').extract()
    #     filepath = 'DC_links.csv'
    #     with open( filepath, 'w') as f:
    #         f.writelines([link + '/n' for link in links])

    def parse(self, response):
        link = response.css('div.course-block > a::attr(href)').extract()
           for link in links:
               yield response.follow( url=link, callback = self.parse_descr)
    
    def parse_descr(self, response):
        course_descr = response.css('p.course__description::text').extract()
        yield course_descr


def inspect_spider( s ):
    news = s()
    try:
        req1 = list( news.start_requests() )[0]
        html1 = requests.get( req1.url ).content
        response1 = TextResponse( url = req1.url, body = html1, encoding = 'utf-8' )
        req2 = list( news.parse( response1 ) )[0]
        html2 = requests.get( req2.url ).content
        response2 = TextResponse( url = req2.url, body = html2, encoding = 'utf-8' )
        for d in news.parse_descr( response2 ):
            print("One course description you found is:", d )
            break
    except:
        print("Oh no! Something is wrong with the code. Keep trying!")

def previewCourses( dc_dict, n = 3 ):
    crs_titles = list( dc_dict.keys() )
    print( "A preview of DataCamp Courses:")
    print("---------------------------------------\n")
    for t in crs_titles[:n]:
        print( "TITLE: %s" % t)
        for i,ct in enumerate(dc_dict[t]):
            print("\tChapter %d: %s" % (i+1,ct) )
        print("")


# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
    name = "dc_chapter_spider"
    # start_requests method
    def start_requests(self):
        yield scrapy.Request(url = url_short, callback = self.parse_front)
    # First parsing method
    def parse_front(self, response):
        course_blocks = response.css('div.course-block')
        course_links = course_blocks.xpath('./a/@href')
        links_to_follow = course_links.extract()
        for url in links_to_follow:
            yield response.follow(url = url, callback = self.parse_pages)
    # Second parsing method
    def parse_pages(self, response):
        crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
        crs_title_ext = crs_title.extract_first().strip()
        ch_titles = response.css('h4.chapter__title::text')
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        dc_dict[ crs_title_ext ] = ch_titles_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)