from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

options = Options()
#options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = 'C:/Program Files/chromedriver/chromedriver.exe'
service = Service(r"C:\Program Files\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

def get_emails(page):
    global options, DRIVER_PATH, driver
    
    driver.get(page)
    time.sleep(5)
    select = driver.find_elements(By.CSS_SELECTOR, ".hUL4le") # hUL4le is name
    emails = []

    for email in select:
        emails.append(email.text)

    with open(f"CODE/Python/Selenium/School Email Scraper/out.txt", "w+") as f:
        for email in emails:
            f.write(email + "\n")

a = input()

get_emails("https://contacts.google.com/u/0/directory")

driver.close()