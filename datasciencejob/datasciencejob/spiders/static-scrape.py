# import requests
# import re
# import urllib
# import csv
# from bs4 import BeautifulSoup
# from scrapy import Selector
# url_prefix = 'https://www.indeed.com'
# url_nopage = 'https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park%2C+NC'
# url = 'https://www.indeed.com/jobs?q=data+science&l=Research+Triangle+Park,+NC&start=10'

# html = requests.get(url).content

# response = Selector(text=html)

# # links = response.css('a.jobtitle.turnstileLink::attr(href)').extract()
# links = response.css('a.turnstileLink::attr(href)').extract()

# links = [re.search('clk\?jk=(\w+)\&',link).group(1) for link in links if re.search('clk\?jk', link) is not None]

# # links = links + response.css('h2.jobtitle > a::attr(href)').extract()
# titles = response.css('a.jobtitle.turnstileLink::attr(title)').extract()
# titles = titles + response.css('h2.jobtitle > a::attr(title)').extract()

# print(links)

# linksr = ["https://www.indeed.com" + link for link in links]

# linksr = [requests.head(link, allow_redirects=True).url for link in linksr]

# # linksr = [urllib.request.urlopen(link).geturl() for link in linksr]

# print(linksr)

# linksr = [requests.head(link, allow_redirects=True).url for link in linksr]

# # linksr = [urllib.request.urlopen(link).geturl() for link in linksr]

# print(linksr)

# link_new = []

# for link_ in linksr:
#     if re.search('viewjob', link_):
#         link_new.append(re.search('(^[\w./:-\?]+)&', link_).group(1))
#     else:
#         link_new.append(re.search('(^[\w./:-]+)?', link_).group(1))

# print(linksr)
# print(link_new)

# # filename = './indeed_test.csv'

# # with open(filename, 'w', newline='') as f:
# #     wr = csv.writer(f)
# #     for link in links:
# #         link = url_prefix + link
# #         wr.writerow([link])
