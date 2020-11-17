from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/temp/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    mars_news = {}
    url ="https://mars.nasa.gov/news/"
    # create soup
    #Mars News
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_news = soup.find("div", class_="slide")

    news_title = latest_news.find("div", class_="content_title")
    mars_news["title"] = news_title.find("a").get_text()
    news_article =  latest_news.find("div", class_="rollover_description")
    mars_news["article"] = news_article.find("div", class_="rollover_description_inner").get_text()
    mars_news["link"] = latest_news.a["href"]


    #Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    feature_img = soup.find("a", class_="fancybox")
    featured_image_link = feature_img['data-fancybox-href']
    mars_news["featured_image_link"] = "https://www.jpl.nasa.gov" + featured_image_link


    # ImportError: lxml not found, please install it : I can't fix this error so I've decided to just use the ipyb file to convert to html
    # But if i dont have that error I think this code would work.
    #Mars Facts
    #scrape_table = pd.read_html("https://space-facts.com/mars/")
    #mars_facts = scrape_table[0]
    #mars_facts.columns = ["Description", "Mars"]
    #mars_facts = mars_facts.set_index(["Description"])
    #mars_news["mars_facts"] = scrape_table
    
    #Mars Hemisphere
    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    schia_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    valles_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    
    #Cerberus
    response = requests.get(cerberus_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_container = soup.find('div', class_="wide-image-wrapper")

    img = img_container.find("li")
    mars_news["cerberus_img"] = img.a["href"]
    mars_news["cerberus_title"] = soup.find('h2', class_="title").text
#---------------------------------------------------------------------------
    #Schia
    response = requests.get(schia_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_container = soup.find('div', class_="wide-image-wrapper")

    img = img_container.find("li")
    mars_news["schia_img"] = img.a["href"]
    mars_news["schia_title"] =  soup.find('h2', class_="title").text
#---------------------------------------------------------------------------
    #Syrtis
    response = requests.get(syrtis_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_container = soup.find('div', class_="wide-image-wrapper")

    img = img_container.find("li")
    mars_news["syr_img"] = img.a["href"]
    mars_news["syr_title"] = soup.find('h2', class_="title").text    
#---------------------------------------------------------------------------
    #Valles
    response = requests.get(valles_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_container = soup.find('div', class_="wide-image-wrapper")

    img = img_container.find("li")
    mars_news["valles_img"] = img.a["href"]
    mars_news["valles_title"] = soup.find('h2', class_="title").text  


    return mars_news