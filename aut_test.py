from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jayagas.com/")



# get all <div> elements
divs = driver.find_elements(By.TAG_NAME, "div")

with open("alldivs.txt","w") as f:
    f.write(f"Found {len(divs)} divs\n")

    # iterate and print their text

    print(type(divs[2].text))



    for idx, div in enumerate(divs, start=1):
        f.write(f"id: {idx}, text: {div.text}\n\n")  # visible text
