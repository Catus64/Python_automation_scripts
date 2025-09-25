from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://localhost:5173/")

uls = driver.find_elements(By.CSS_SELECTOR, "ul.list-group")

for ul in uls:
    items = ul.find_elements(By.CLASS_NAME, "list-group-item")
    for item in items:
        item.click()
        time.sleep(1)
        print(item.text)

driver.refresh()

#items = driver.find_elements(By.CSS_SELECTOR, "ul.list-group li.list-group-item")

#breakpoint()