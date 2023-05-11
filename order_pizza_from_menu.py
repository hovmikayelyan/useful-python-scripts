#!/usr/bin/env python3
# @author hovmikayelyan

# This script can order a pizza for you 
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

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Restaurant name you want to order from
restaurant_name = "Պիցցա Հաթ"
# Food you would like to order
desired_food = [
    'Պիցցա Մսային Սիրահարներ պան քրասթ մեծ',
    'Պիցցա Պեպպերոնիի սիրահարներ պան քրասթ մեծ'
]

driver = webdriver.Firefox() # creates a driver firefox
driver.maximize_window() # maximizes the friefox windows

wait = WebDriverWait(driver, 10) # this will help you later, to weait for some element to appear

# Your credentials which you will be asked to input
login = input("Please enter your email for menu.am account:\n")
password = input("Please enter your password:")

# Main url of menu.am's login page
driver.get("https://menu.am/am/auth-sign-in")

# Finding input areas, and pasting the credentials
inputs = driver.find_elements(By.CLASS_NAME, "MuiInputBase-inputAdornedEnd")
inputs[0].send_keys(login)
inputs[1].send_keys(password)

# Finding sign-in button and tapping on it
sign_in_button = driver.find_element(
    By.CLASS_NAME, "MuiButton-containedPrimary")
sign_in_button.click()
time.sleep(5)

# Selects your saved address as main address for the delivery
address_searcher = driver.find_element(
    By.CLASS_NAME, "MuiInputAdornment-positionEnd")
address_searcher.click()
time.sleep(1)
my_address = driver.find_element(
    By.CLASS_NAME, "MuiListItem-gutters")
my_address.click()
time.sleep(3)

# Writes the restaurant name and searches it
search_box = driver.find_element(
    By.CLASS_NAME, "MuiInputBase-inputAdornedStart")
search_box.send_keys(restaurant_name)
search_button = driver.find_element(By.XPATH, "//span[text()='Որոնում']")
time.sleep(1)
search_button.click()
time.sleep(5)

# Selecting the restaurant from bringed examples
pizza_hut = driver.find_element(
    By.XPATH, f"//h2[contains(text(),'{restaurant_name}')]")
pizza_hut.click()
time.sleep(3)

# scrolling a little to make the site load its content
driver.execute_script("window.scrollTo(0, 900)")

# loop to order the food
for item in desired_food:
    pizza = driver.find_element(
        By.XPATH, f"//img[@title='{item}']")
    pizza.click()
    time.sleep(1)

    pizza_hut = driver.find_element(
        By.XPATH, "//span[contains(text(),'Ավելացնել զամբյուղ')]")
    pizza_hut.click()
    time.sleep(1)


# opening shopping cart
shopping_cart = wait.until(EC.element_to_be_clickable(driver.find_element(
    By.CLASS_NAME, "badge")))
shopping_cart.click()
time.sleep(3)

# tapping to order
ordering = driver.find_element(
    By.XPATH, "//span[contains(text(),'Պատվիրել հիմա')]")
ordering.click()
time.sleep(3)

# choose in place type of payment
pay_in_place = driver.find_element(
    By.XPATH, "//input[@name='pay_in_place']").click()
time.sleep(1)

# finally, order it!
order_proceed = driver.find_element(
    By.CLASS_NAME, "MuiButton-label")
order_proceed.click()
time.sleep(2)

