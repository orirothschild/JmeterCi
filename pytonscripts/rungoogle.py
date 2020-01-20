# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver_path = "D:\drivers\chrome\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()