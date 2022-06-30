# Jupyter Notebook Conversion to Python Script
################################################

# Dependencies and Setup
from string import whitespace
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# Set Executable Path & Initialize Chrome Browser
#################################################
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

# NASA Mars News Site Web Scraper
#################################################
def mars_news(browser):
    # Visit the NASA Mars News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")

    # Parse Results HTML with BeautifulSoup
    # Find Everything Inside:
    #   <ul class="item_list">
    #     <li class="slide">
    try:
#         slide_element = news_soup.select_one("ul.item_list li.slide")
#         slide_element.find("div", class_="content_title")

        # Scrape the Latest News Title
        # Use Parent Element to Find First <a> Tag and Save it as news_title
#         news_title = slide_element.find("div", class_="content_title").get_text()

#         news_paragraph = slide_element.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    return news_title, news_paragraph