#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

# Function to scrape Mars data
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Scrape news
    news_url = 'https://redplanetscience.com'
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_='article_teaser_body').get_text()

    # Scrape image
    space_image_url = 'https://spaceimages-mars.com/'
    browser.visit(space_image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find('img', class_='headerimage')
    featured_image_url = space_image_url + image['src']

    # Scrape facts
    facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(facts_url)
    mars_earth_df = tables[0]
    mars_earth_df.rename(columns=mars_earth_df.iloc[0], inplace = True)
    mars_earth_df.drop([0], inplace = True)
    mars_table = mars_earth_df.to_html(index=False, classes=['table-primary','table-striped','table-hover'])
    mars_table = mars_table.replace('\n', '')

    # Scrape hemisphere data
    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find the image title and url
    item_links = soup.find_all('div', class_='description')
    hemisphere_image_urls = []
    for item in item_links:
        image_dict = {}
        link = item.find('a')['href']
        ful_link = hemisphere_url + link
        browser.visit(ful_link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image_dict["title"] = soup.find('h2',class_='title').get_text()
        divs = soup.find('div', class_='downloads')
        res_image = divs.find('li').a['href']
        image_dict["img_url"] = hemisphere_url + res_image
        hemisphere_image_urls.append(image_dict)

    scraped_data = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "mars_table":mars_table,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    browser.quit()
    return (scraped_data)
