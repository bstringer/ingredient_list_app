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

def search_recipe(req_dat):
    searchword = req_dat['package']
    pages = int(req_dat['numpage'])
    driver = webdriver.Chrome(PATH);
    driver.get("https://www.allrecipes.com/")
    collect_recipes_obj = {}

    #Click to open up the searchbar
    search_icon = driver.find_element_by_class_name("general-search__icon-button")
    search_icon.click()
    #Search our searchword
    search = driver.find_element_by_id("fullscreen-nav__search__search-input")
    search.send_keys(searchword)
    search.send_keys(Keys.RETURN)

    for i in range(pages):

        try:
            search_results = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "card-list_1-0"))
            )

            recipes = search_results.find_elements_by_tag_name("a")
            for recipe in recipes:
                try:
                    meal = recipe.find_element_by_class_name("card__title-text")
                    image = recipe.find_element_by_tag_name("img").get_attribute("src")
                    link = recipe.get_attribute("href")
                    if image != None:
                        collect_recipes_obj[meal.text] = {"image": image,
                                                        "link": link
                                                        }
                except Exception as e:
                            print("error each one: ", e, flush=True)                                                        
        except Exception as e:
            print("error: ", e, flush=True)

        next_page = driver.find_element(By.LINK_TEXT, 'NEXT')
        next_page.send_keys(Keys.RETURN)
        time.sleep(1)

    driver.quit()
    return collect_recipes_obj


def web_collect(search_obj):
    driver = webdriver.Chrome(PATH);
    driver.get("https://www.allrecipes.com/")
    parts = []
    recipe_obj = {}

    for meal in search_obj:
        meal_info = search_obj[meal]
        recipie_link = meal_info["link"]
        driver.get(recipie_link)

        try:
            ingredient = "";
            quantity = "";
            units = "";

            search_results = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "mntl-structured-ingredients_1-0"))
            )

            ingredient_string = ""
            info = search_results.find_elements_by_tag_name("p")
            for each_ingredient in info:
                ingredient = each_ingredient.find_element_by_css_selector('span[data-ingredient-name="true"]')
                quantity = each_ingredient.find_element_by_css_selector('span[data-ingredient-quantity="true"]')
                units = each_ingredient.find_element_by_css_selector('span[data-ingredient-unit="true"]')
                ingredient_string += createOrFill_obj(ingredient.text, quantity.text, units.text)

            search_obj[meal]["ingredients"] = ingredient_string;

        except Exception as e:
            print("error: ", e, flush=True)
            # driver.quit()

    driver.quit()
    return search_obj


def createOrFill_obj(ingredient, quantity, units):
    add_to_obj = False
    if units == "":
        units = "single"
    
    if quantity == "":
        quantity = "n/a"

    return (quantity + " " + units + " " + ingredient +"<br>")




# def createOrFill_obj(ingredient, quantity, units, recipe_obj):
#     add_to_obj = False
#     if units == "":
#         units = "single"
#         print("units single: ", flush=True)
    
#     if quantity == "":
#         quantity = "n/a"
#         print("quantity n/a: ", flush=True)
    
#     try:
#         print("\n ingredient: ", ingredient, units, quantity, flush=True)
#     except Exception as e:
#         print("error: ", e, flush=True)

    
#     for used_ingredient in recipe_obj:
#         if ingredient in used_ingredient or used_ingredient in ingredient:
#             add_to_obj = True
#             if units in recipe_obj[used_ingredient]:
#                 print("units there: ", ingredient, units, flush=True)
#                 recipe_obj[used_ingredient][units].append(quantity);
#             else:
#                 print("make object with units: ", ingredient, flush=True)
#                 recipe_obj[used_ingredient][units] = [quantity];

#     if add_to_obj == False:
#         print("make new object: ", flush=True)
#         recipe_obj[ingredient] = {
#                                 units: [quantity]
#                             };

#     return True
