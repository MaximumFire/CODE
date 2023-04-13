from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep as s

options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
options.add_argument("user-data-dir=C:\\Users\\conno\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
DRIVER_PATH = 'C:/Program Files/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
try:    
    driver.get("https://app.senecalearning.com/classroom/course/10335c2e-3876-431a-b7f6-3f69305b5ec8/section/e2cbedc1-313b-4cc3-b6e4-351ffaeb9b41/session")
    s(10)

    # start new session
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "session_startNewSession"))
    ).click()
    s(5)

    # question loop
    

finally:
    driver.quit()