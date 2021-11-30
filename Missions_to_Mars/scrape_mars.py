import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
# Splinter setup
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Open Mars site
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    #Scrape
    html = browser.html
    soup = bs(html, 'html.parser')

    #title
    news_title = soup.find_all('div', class_='content_title')[1].text

    #paragraph
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

    print(news_title)
    print(news_p)

    #JPL Mars Space Images
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")  

    images = soup.find_all('img')

    featured_img_url =  url + images[1]['src']

    print(featured_img_url)

    #Visit site
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    time.sleep(1)

    tml = browser.html
    soup = bs(html, 'html.parser')

    # Use Pandas to scrape data
    mars_facts = pd.read_html(url)
    mars_df = pd.DataFrame(mars_facts[1])
    mars_df

    mars_df.columns=['Measure', 'Value']
    mars_df

    #Convert to html
    mars_html=mars_df.to_html()
    mars_html

    mars_html.replace('\n','')
    print(mars_html)

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('div', class_='description')

    hemisphere_pic_urls = []

    for result in results:
    

        #find the title and href and add it to the base url
        title = result.h3.text
        href = result.find('a')['href']
        tempurl = url + href
    
        # go to temp url and find high res image link
        browser.visit(tempurl)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_src = soup.find('img', class_="wide-image")['src']
        img_url = url + img_src


        temp_dic = {}
        temp_dic['title'] = title
        temp_dic['img_url'] = img_url
        hemisphere_pic_urls.append(temp_dic)

        print(img_url)
        print(title)
        print('----------------')
        
        mars_data = {
          "news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_img_url,
            "mars_html" : str(mars_html),
            "hemisphere_image_urls": hemisphere_pic_urls
        }
    browser.quit()

    # Return results
    return mars_data


