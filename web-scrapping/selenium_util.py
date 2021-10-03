from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import OS,CHROME_DRIVER_PATH

def getLinks(key):
    if OS == 'MAC' or OS == 'LINUX':
        driver = webdriver.Chrome()
    elif OS == 'WINDOWS':
        driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    else:
        raise Exception('Unknown Operating System. Please check readme for guidelines')
    youtubeSearchUrl = 'https://www.youtube.com/results?search_query=' + '+'.join(key.split())
    driver.get(youtubeSearchUrl)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    links = []
    for i in user_data:
        links.append(i.get_attribute('href'))
    return links
