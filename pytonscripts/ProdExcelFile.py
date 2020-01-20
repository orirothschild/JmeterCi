# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:58:39 2020

@author: orir
"""

#
#  -*- coding: utf-8! -*-
from drivers import mydriver
currentdriver=mydriver()
chromepath = currentdriver.chrome
downloads_path ='/c/Users/orir/Downloads/'
file_path ="ניהול הזמנה_יום שלישי 14 ינואר 2020"
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os.path
import unittest, time




class EXCELPROD(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=chromepath)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.maximize_window()
        driver.get("https://shufersal.verifone.co.il/")
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("omri@dts-4u.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234567")
        driver.find_element_by_id("loginsystem").click()


    def test_e_x_c_e_l(self):
        driver = self.driver
        driver.get("https://shufersal.verifone.co.il/Orders/OrdersUpdate")
        element = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='₪'])[1]/following::span[3]")# .click()
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").send_keys(u"א.ב הובלות בעמ")
        time.sleep(3)
        element = driver.find_element_by_xpath("//div[@id='grid']/div/div/div[2]/div/span/span/span")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        actions = ActionChains(driver)
        actions.send_keys(Keys.DOWN).perform()
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"row")))
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,u"יצוא לאקסל")))
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
        time.sleep(6)
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
