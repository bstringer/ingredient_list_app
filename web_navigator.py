"""
Program made by Blair Stringer

help link - https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ
"""

from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import time;

PATH = "C:\Program Files (x86)\chromedriver.exe";

def search_recipe(searchword):
    driver = webdriver.Chrome(PATH);
    driver.get("https://www.allrecipes.com/")
    collect_recipes = []

    #Click to open up the searchbar
    search_icon = driver.find_element_by_class_name("general-search__icon-button")
    search_icon.click()
    #Search our searchword
    search = driver.find_element_by_id("fullscreen-nav__search__search-input")
    search.send_keys(searchword)
    search.send_keys(Keys.RETURN)

    try:
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "card-list_1-0"))
        )

        recipes = search_results.find_elements_by_tag_name("a")
        for recipe in recipes:
            meal = recipe.find_element_by_class_name("card__title-text")
            collect_recipes.append(meal.text)
    except Exception as e:
        print("error: ", e, flush=True)
        driver.quit()

    driver.quit()
    return collect_recipes

# list = search_recipe("meatloaf")
# print("list: ", list, flush=True)
