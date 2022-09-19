# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    hemisphere_image_urls = mars_hemispheres(browser)

    # Run all scraping functions and store results in a dictionary
    data =  hemisphere_image_urls

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_hemispheres(browser):
    url = 'https://marshemispheres.com/'

    browser.visit(url)


    # In[26]:


    # 2. Create a list to hold the images and titles.
    html = browser.html
    hemisphere_soup = soup(html, 'html.parser')

    hemisphere_tags = hemisphere_soup.find_all('div', class_='description')
    hemisphere_image_urls = []



    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    for tag in hemisphere_tags:
        url = f'https://marshemispheres.com/{tag.find("a").get("href")}'
        title = tag.find('h3').get_text()
        hemisphere_image_urls.append({"url": url, "title": title})
    hemisphere_image_urls

    # Scrape Mars News
    # Visit the mars nasa news site
    
    try:

        hemisphere_tags = hemisphere_soup.find_all('div', class_='description')
        hemisphere_image_urls = []



        # 3. Write code to retrieve the image urls and titles for each hemisphere.
        for tag in hemisphere_tags:
            url = f'https://marshemispheres.com/{tag.find("a").get("href")}'
            title = tag.find('h3').get_text()
            hemisphere_image_urls.append({"url": url, "title": title})
        
    except AttributeError:
        return None

    return hemisphere_image_urls


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
