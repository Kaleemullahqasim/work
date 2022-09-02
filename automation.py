# import packeges 
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


url = 'https://mopan.baijia.com/receiveLabelTask'


# get the driver
driver = webdriver.Chrome('/Users/kaleemullahqasim/Documents/GitHub/news_automation/chromedriver')
driver.get(url)
time.sleep(100)

