from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time
import fake_useragent
from selenium.webdriver.common.keys import Keys

headers = {
    "Accept": "/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36 "
}

""" user = fake_useragent.UserAgent().random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user}')
driver = webdriver.Chrome(options=options) """

""" def get_main_py():
    with open("daun.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        GilterSS = []
        for line  in lines:
            browser = webdriver.Chrome()
            browser.get(line)
            html = browser.find_element(By.TAG_NAME, "html")
            for i in range(15):
                html.send_keys(Keys.DOWN)
            button = browser.find_element(By.CLASS_NAME, "CategoryDetails_more-button__Zi7d4").click()
            for i in range(10):
                html.send_keys(Keys.DOWN)
            button2 = browser.find_element(By.CLASS_NAME, "CategoryDetails_more-button__Zi7d4").click()
            all_prp_list = browser.find_elements(By.CLASS_NAME, "CategoryItem_category-item-link__FJ0iI")
            for card in all_prp_list:
                GilterSS.append(card.get_attribute("href"))
            with open("card_list.txt", "a") as file:
                for line in GilterSS:
                    file.write(f"{line}\n") """
def get_main2_py():
    with open("card_list.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        lek = []
        for line in lines:
            q = requests.get(line, headers = headers)
            soup = BeautifulSoup(q.content, "lxml")
            if soup.find("div", class_ = "Pagination_pagination__wSOfa List_list-pagination__OWaQ9") is not None:
                num = soup.find("button", class_ = "Button_button__znY7u Button_button--orange__UzsMb Button_button--orange--outlined__e6vGV Button_button--small__YGLme Pagination_pagination-control-button___6a2H").get("alt")
                cards0 = soup.find("div", class_ = "ProductsList_list-grid__76wlE")
                cards = cards0.find_all("a", class_ = "Horizontal_horizontal-title__XBc6D")
                for card in cards:
                    lek.append(card.get("href"))
                for i in range(2,int(num)+1):
                    q = requests.get(f"{line}?PAGEN_1={i}", headers = headers)
                    soup = BeautifulSoup(q.content, "lxml")
                    cards = cards0.find_all("a", class_ = "Horizontal_horizontal-title__XBc6D")
                    for card in cards:
                        lek.append(card.get("href"))
                with open("lists.txt", "a") as file:
                    for line in lek:
                        file.write(f"{line}\n")

                
            
            else:
                num = None
                cards = soup.find("div", class_ = "ProductsList_list-grid__76wlE").find_all("a", class_ = "Horizontal_horizontal-title__XBc6D")
                for card in cards:
                    lek.append(card.get("href"))
                
                

            
            
            




def main():
    # get_city_list('https://zdravcity.ru/')
    get_main2_py()

if __name__ == '__main__':
    main()