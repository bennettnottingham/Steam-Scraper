from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
import pandas as pd

driver = webdriver.Chrome()
url = "https://store.steampowered.com/search/?sort_by=_ASC&os=win&supportedlang=english&filter=globaltopsellers"
driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("Reached the bottom of the page.")
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, "html.parser")

games_details = []

for game_element in soup.find_all('a', class_="search_result_row"):
    game_name = game_element.find(class_="title").text if game_element.find(class_="title") else None
    release_date = game_element.find(class_="search_released").text if game_element.find(class_="search_released") else None
    
    price_elem = game_element.find("div", {"class": re.compile("col search_price")})
    if price_elem:
        price_text = price_elem.text.strip()
        is_sale = 1 if "%" in price_text else 0
        final_price = price_text.split("$")[-1] if is_sale else price_text
    else:
        final_price = '0'
        is_sale = 0
    
    link = game_element['href'] if game_element.get('href') else None
    review_summary = game_element.find("span", {"class": re.compile("search_review_summary")})['data-tooltip-html'].split('<br>')[0] if game_element.find("span", {"class": re.compile("search_review_summary")}) else None
    num_reviews = game_element.find("span", {"class": re.compile("search_review_summary")})['data-tooltip-html'].split('<br>')[1] if game_element.find("span", {"class": re.compile("search_review_summary")}) and '<br>' in game_element.find("span", {"class": re.compile("search_review_summary")})['data-tooltip-html'] else None
    
    games_details.append({
        'Name': game_name,
        'Release Date': release_date,
        'Price': final_price,
        'Link': link,
        'Review Summary': review_summary,
        'Number of Reviews': num_reviews,
        'Is Sale': is_sale
    })

driver.close()

df = pd.DataFrame(games_details)
df.to_csv("steam_games.csv", index=False)
print("Data saved to 'steam_games.csv'")