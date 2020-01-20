#
#  -*- coding: utf-8 -*-
from drivers import mydriver
currentdriver=mydriver()
chromepath = currentdriver.chrome
downloads_path ='/c/Users/orir/Downloads/'
file_path ="ניהול הזמנה_יום שלישי 14 ינואר 2020"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui 
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os.path
import unittest, time, re




class EXCEL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=chromepath)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get("http://172.29.46.11/User/Login?ReturnUrl=%2FOrders%2FOrdersUpdate")
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("omri@dts-4u.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234567")
        driver.find_element_by_id("loginsystem").click()


    def test_e_x_c_e_l(self):
        driver = self.driver
        driver.get("http://172.29.46.11/Orders/OrdersUpdate")
        element = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='₪'])[1]/following::span[3]")# .click()
        driver.execute_script("arguments[0].click();", element)
      #  driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='₪'])[1]/following::span[3]").click()
#        driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").clear()
 
        element = driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").send_keys(u"א.ב הובלות בעמ")
        time.sleep(1)
        element = driver.find_element_by_xpath("//div[@id='grid']/div/div/div[2]/div/span/span/span")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        actions = ActionChains(driver)
        actions.send_keys(Keys.DOWN).perform()
        #driver.execute_script(value="א.ב הובלות בעמ",element)
        #driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").send_keys(Keys.ENTER)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"row")))


        time.sleep(6)
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
        time.sleep(4)
       ## driver.find_element_by_xpath(u"//div[@id='grid']/div/div/div[2]/div[4]/a/span").click()
       # #time.sleep(5)
       # #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='ניהול הזמנה'])[1]/following::div[3]").click()
       # #time.sleep(7)

 #       driver.find_element_by_class_name("k-grid-excel").click()
        #driver.find_element_by_class_name(u"k-grid-excel").click()

        print('ok')
    
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
