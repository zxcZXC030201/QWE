from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time
import fake_useragent

user = fake_useragent.UserAgent().random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user}')
driver = webdriver.Chrome(options=options)


def get_drug_names(link):
        page_urls = []
        driver.get(url = link)
        time.sleep(2)
        btn = driver.find_element(By.TAG_NAME, 'svg').click()
        time.sleep(5)
        bttn_list = driver.find_element(By.CLASS_NAME, 'Autocomplete_autocomplete-suggestions__pF1oZ')
        bttns = bttn_list.find_elements(By.TAG_NAME, 'li')
        for i in range(len(bttns)):
            bttn_list = driver.find_element(By.CLASS_NAME, 'Autocomplete_autocomplete-suggestions__pF1oZ')
            bttns = bttn_list.find_elements(By.TAG_NAME, 'li')
            bttn = bttns[i]
            bttn.click()
            print(1)
            time.sleep(3)
            local_url = driver.find_element(By.CLASS_NAME, "Container_container__f9MJQ").find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "a")[3].get_attribute("href").replace("https://zdravcity.ru/", "https://zdravcity.ru/catalog/lekarstvennye-preparaty/")
            page_urls.append(local_url)
            print(local_url)
            print(2)
            time.sleep(2)
            btn = driver.find_element(By.TAG_NAME, 'svg').click()
            time.sleep(2)
        with open("pgs_list.txt", "a") as file:
                 for line in page_urls:
                      file.write(f"{line}\n")
def main():
    # get_city_list('https://zdravcity.ru/')
    get_drug_names('https://zdravcity.ru/')

if __name__ == '__main__':
    main()
