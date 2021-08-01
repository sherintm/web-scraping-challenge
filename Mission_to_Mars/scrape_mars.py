#!/usr/bin/env python
# coding: utf-8

# In[167]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import pymongo


# In[168]:


# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[169]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)


# In[170]:


news_url = 'https://redplanetscience.com'
browser.visit(news_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
news_title = soup.find('div', class_='content_title').get_text()
news_p = soup.find('div', class_='article_teaser_body').get_text()

print(news_title)
print(news_p)


# In[171]:


space_image_url = 'https://spaceimages-mars.com/'
browser.visit(space_image_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.find('img', class_='headerimage')
featured_image_url = space_image_url + image['src']
print(featured_image_url)


# In[172]:


facts_url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(facts_url)
len(tables)


# In[173]:


mars_earth_df = tables[0]
mars_earth_df 


# In[174]:


mars_table = mars_earth_df.to_html()
mars_table


# In[175]:


hemisphere_url = 'https://marshemispheres.com/'
browser.visit(hemisphere_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[176]:


item_links = soup.find_all('div', class_='description')
hemisphere_image_urls = []
for item in item_links:
    image_dict = {}
    link = item.find('a')['href']
    ful_link = hemisphere_url + link
    #print(ful_link)
    browser.visit(ful_link)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_dict["title"] = soup.find('h2',class_='title').get_text()
    divs = soup.find('div', class_='downloads')
    res_image = divs.find('li').a['href']
    image_dict["img_url"] = hemisphere_url + res_image
    #print(image_dict["img_url"])
    #print(image_dict["title"])
    hemisphere_image_urls.append(image_dict)
print(hemisphere_image_urls)


# In[ ]:





# In[ ]:




