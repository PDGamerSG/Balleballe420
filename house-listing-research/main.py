import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path="C:\Development\chromedriver"
zillio_link='https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.85923291322895%2C%22east%22%3A-122.3208912980957%2C%22south%22%3A37.691255580355254%2C%22west%22%3A-122.5457677019043%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D'
form_link='https://docs.google.com/forms/d/e/1FAIpQLSc1W1VvGM3YzhriwX-QsH8iOUruj7HSMS9B8xoVS7nM_t7NRA/viewform?usp=sf_link'

headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    'Accept-Language':"en-US,en;q=0.6"
}



response= requests.get(zillio_link,headers=headers)
zillow_site=response.text
soup= BeautifulSoup(zillow_site,"html.parser")

all_listings= soup.find_all(name="article",class_="list-card_for-rent")

driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(form_link)
time.sleep(5)

for listing in all_listings:

    address=listing.find(name="address").text
    price=listing.find(name="span").text
    link=listing.find(name="a",class_="property-card-link")['href']
    if " " in price: price=f"{price.split('+')[0]}/mo"
    if "zillow" not in link:
        link=f"https://www.zillow.com{link}"

    add_box= driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_box.send_keys(address)

    price_box= driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box.send_keys(price)

    link_box= driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box.send_keys(link)
    time.sleep(1)

    submit=driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(3)
    sub_another_response= driver.find_element(By.CSS_SELECTOR,".c2gzEf a")
    sub_another_response.click()
    time.sleep(2)
