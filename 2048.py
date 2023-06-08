# Sends keystroke commands for up, right, down, left
# for game 2048 at https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://play2048.co/'
driver.get(url)

website = driver.find_element(By.TAG_NAME, 'html')


while True:
        website.send_keys(Keys.UP)
        website.send_keys(Keys.RIGHT)
        website.send_keys(Keys.DOWN)
        website.send_keys(Keys.LEFT)
        try:
            retryBtn = driver.find_element(By.CLASS_NAME, 'retry-button').click()
            time.sleep(3)
        except:
            continue
