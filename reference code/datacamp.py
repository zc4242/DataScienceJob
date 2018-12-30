from scrapy import Selector
from scrapy.http import Response, Request
import requests

html = requests.get(url='https://www.datacamp.com/courses/all').content
sel = Selector(text = html)

# Create a SelectorList of the course titles
crs_title_els  = sel.css('h4::text')

# Extract the course titles 
crs_titles = crs_title_els.extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )



sel.xpath("//p").extract()
sel.xpath("//p").extract_first()



print(response)
# or

ps = sel.xpath("//p")
second_p = ps[1]
second_p.extract()

url = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'
html = requests.get(url).content
sel = Selector(text=html)
print("There are ", len(sel.xpath('//*')),'elements in the HTML document.')

# sel.xpath('//div').extract()

import inspect
def how_many_elements(css):
    sel = Selector(text=html)
    print(len(sel.css(css)))
inspect.getsource(how_many_elements)

def print_url_title( url, title ):
    print( "Here is what you found:" )
    print( "\\t-URL: %s" % url )
    print( "\\t-Title: %s" % title )




sel = Selector(text=html)
course_as = sel.css('div.course-block > a')
hrefs_from_css = course_as.css('::attr(href)')
hrefs_from_css
hrefs_from_xpath = course_as.xpath('./@href')
hrefs_from_xpath



