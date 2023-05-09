from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
#####################################################################################

login = ""
password = ""

driver.get("https://menu.am/am/auth-sign-in")

#####################################################################################
# Logging in

inputs = driver.find_elements(By.CLASS_NAME, "MuiInputBase-inputAdornedEnd")
inputs[0].send_keys(login)
inputs[1].send_keys(password)

sign_in_button = driver.find_element(
    By.CLASS_NAME, "MuiButton-containedPrimary")
sign_in_button.click()
time.sleep(5)

#####################################################################################
# Select my address

address_searcher = driver.find_element(
    By.CLASS_NAME, "MuiInputAdornment-positionEnd")
address_searcher.click()
time.sleep(1)

my_address = driver.find_element(
    By.CLASS_NAME, "MuiListItem-gutters")
my_address.click()
time.sleep(3)

#####################################################################################
# Write pizza restaurant name

search_box = driver.find_element(
    By.CLASS_NAME, "MuiInputBase-inputAdornedStart")
search_box.send_keys("pizza hut")

search_button = driver.find_element(By.XPATH, "//span[text()='Որոնում']")
time.sleep(2)
search_button.click()
time.sleep(5)

# Selecting pizza hut from bringed examples
pizza_hut = driver.find_element(
    By.XPATH, "//h2[contains(text(),'Պիցցա Հաթ')]")
pizza_hut.click()
time.sleep(3)


#####################################################################################
# scrolling to make site load

driver.execute_script("window.scrollTo(0, 900)")

selected_pizzas = [
    'Պիցցա Մսային Սիրահարներ պան քրասթ մեծ',
    'Պիցցա Պեպպերոնիի սիրահարներ պան քրասթ մեծ'
]

for item in selected_pizzas:
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

order_proceed = driver.find_element(
    By.CLASS_NAME, "MuiButton-label")
order_proceed.click()
time.sleep(2)

