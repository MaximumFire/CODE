from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = 'C:/Program Files/chromedriver/chromedriver.exe'
service = Service(r"C:\Program Files\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

def get_options(page):
    global options, DRIVER_PATH, driver
    
    driver.get(page)
    select = Select(driver.find_element(By.ID, "addon_option_1"))
    options = []

    for opt in select.options:
        if " - New" in opt.text:
            options.append(opt.text.replace(" - New", ""))
        elif "(New)" in opt.text:
            options.append(opt.text.replace("(New)", ""))
        elif "- New" in opt.text:
            options.append(opt.text.replace("- New", ""))
        elif " - Best Flavour" in opt.text:
            options.append(opt.text.replace(" - Best Flavour", ""))
        elif opt.text != "Choose an option":
            options.append(opt.text)

    if "lost-mary-bm3500" in page:
        filename = "lostmary.txt"
    elif "elf-bar-disposable-pen" in page:
        filename = "elfbar.txt"
    elif "aroma-king-ak5500" in page:
        filename = "aromaking.txt"
    elif "crystal-bar" in page:
        filename = "crystalbar.txt"
    elif "elux-legend-pro" in page:
        filename = "eluxlegend.txt"

    with open(f"CODE/Python/Selenium/Vape Shop Scraping/{filename}", "w+") as f:
        for opt in options:
            f.write(opt + "\n")


get_options(page="https://www.ninja-vapes.co.uk/product/lost-mary-bm3500-20mg-disposable-pod-device")
get_options(page="https://www.ninja-vapes.co.uk/product/elf-bar-disposable-pen-2ml-600-puffs-20mg")
get_options(page="https://www.ninja-vapes.co.uk/product/aroma-king-ak5500-disposable-vape-device")
get_options(page="https://www.ninja-vapes.co.uk/product/crystal-bar-600-puff-disposable-vape-device")
get_options(page="https://www.ninja-vapes.co.uk/product/elux-legend-pro-3500-rechargeable-vape-device")

driver.close()