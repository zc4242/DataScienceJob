#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'datasciencejob/datasciencejob'))
	print(os.getcwd())
except:
	pass

#%%
# Import packages
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


#%%
def scrape_links(url):
    soup = BeautifulSoup(requests.get(url).text)

    link = [l.get('href') for l in soup.find_all('a') if (l.get('href') is not None) & (str(l.get('href')).startswith('/pagead/'))]
    
    link2 = ['https://www.indeed.com' + l for l in link]
    
    return link2


#%%
starting_url = 'https://www.indeed.com/jobs?q=data+scientist&l=Raleigh-Durham,+NC'
search_urls = [starting_url + '&start=' + str(l) for l in np.arange(10, 1000, 10)]
search_urls.insert(0, starting_url)
search_urls[:5]


#%%
print(len(search_urls))


#%%
links = []
for i, u in enumerate(search_urls):
    print(i)
    links += scrape_links(u)
links[:1]


#%%
print(len(links))


#%%
def scrape_post(url):
    soup = BeautifulSoup(requests.get(url).text)
    
    desc = {
    'title': soup.find('h3', attrs={'class': 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'}).text,
    'company': soup.find('div', attrs={'class': 'icl-u-lg-mr--sm icl-u-xs-mr--xs'}).text,
    'location': soup.find('div', attrs={'class': 'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'}).text,
    'desc': soup.find('div', attrs={'class': 'jobsearch-JobComponent-description icl-u-xs-mt--md'}).text
    }
    
    return desc


#%%
descs = []
for i, l in enumerate(links):
    print(i)
    descs.append(scrape_post(l))


#%%
df = pd.DataFrame.from_dict(descs)
print(df.shape)


#%%
df.head()


#%%
df['city'] = df.location.str.split('-').str[1].str.split(', ').str[0]
df['state'] = df.location.str.split('-').str[1].str.split(' ').str[1]
df = df[['title', 'company', 'city', 'state', 'desc']]
df.head()


