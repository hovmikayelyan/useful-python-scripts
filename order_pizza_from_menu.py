#!/usr/bin/env python3
# @author hovmikayelyan

# This script can order a pizza for you from menu.am
# I know, right? :D
# If you're from Armenia, and know about menu.am, then you're the chosen one for this script,
# Give you email and password of your menu.am account, and the script will order a food,
# from your given restaurant, and the food you want!
#
# IMPORTANT! You need to have at least 1 saved address in your account! Site must me in Armenian!
#
# If running the script, throws an error `there is no module '...' in your machine`, then run:
# pip install selenium

# Thank you!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Restaurant name you want to order from
restaurant_name = "Պապա Պիցցա"
# Food you would like to order
desired_food = [
    'Կոմբո մեծ',
    'Կոմբո միջին'
]

driver = webdriver.Firefox() # creates a driver firefox
driver.maximize_window() # maximizes the friefox windows

wait = WebDriverWait(driver, 10) # this will help you later, to weait for some element to appear

# Your credentials which you will be asked to input
# if you want, hard-code your log and password into variables below
login = input("Please enter your email for menu.am account:\n")
password = input("Please enter your password:")

# Main url of menu.am's login page
driver.get("https://menu.am/am/auth-sign-in")

# Finding input areas, and pasting the credentials
inputs = driver.find_elements(By.CLASS_NAME, "MuiInputBase-inputAdornedEnd")
inputs[0].send_keys(login)
inputs[1].send_keys(password)

# Finding sign-in button and tapping on it
sign_in_button = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.CLASS_NAME, "MuiButton-containedPrimary")))
sign_in_button.click()

# Selects your saved address as main address for the delivery
address_searcher = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.CLASS_NAME, "MuiInputAdornment-positionEnd")))
address_searcher.click()

my_address = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.CLASS_NAME, "MuiListItem-gutters")))
my_address.click()

# Writes the restaurant name and searches it
search_box = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.CLASS_NAME, "MuiInputBase-inputAdornedStart")))
search_box.send_keys(restaurant_name)
search_button = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//span[text()='Որոնում']")))

search_button.click()

# Selecting the restaurant from bringed examples
food_hut = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.XPATH, f"//mark[contains(text(),'{restaurant_name.split()[1]}')]")))
food_hut.click()

# scrolling a little to make the site load its content
driver.execute_script("window.scrollTo(0, 900)")

# loop to order the food
for item in desired_food:
    my_food = wait.until(EC.element_to_be_clickable(driver.find_element(
        By.XPATH, f"//img[@title='{item}']")))
    my_food.click()

    my_food_popup = wait.until(EC.element_to_be_clickable(driver.find_element(
        By.XPATH, "//span[contains(text(),'Ավելացնել զամբյուղ')]")))
    my_food_popup.click()


# opening shopping cart
shopping_cart = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.CLASS_NAME, "badge")))
shopping_cart.click()

# tapping to order
ordering = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.XPATH, "//span[contains(text(),'Պատվիրել հիմա')]")))
ordering.click()

# choose in place type of payment
pay_in_place = driver.find_element(
    By.XPATH, "//input[@name='pay_in_place']").click()

# finally, order it!
order_proceed = driver.find_element(
    By.CLASS_NAME, "MuiButton-label")

#ORDEEER
order_proceed.click()

# Ta-da, ready!