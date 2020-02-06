
from pytest import mark
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re



@mark.reports
@pytest.mark.usefixtures("shufersal_chrome_login")
class Reports_Tests:  
    def test_tavim_reports_as_excpected(self,shufersal_chrome_login):
        self.driver=shufersal_chrome_login[0]
        self.verificationErrors =shufersal_chrome_login[1]
        self.accept_next_alert =shufersal_chrome_login[2]
        driver = self.driver
        driver.get(shufersal_chrome_login[3])
        driver.find_element_by_id("FieldFilter").clear()
        element =driver.find_element_by_class_name("k-input")
        driver.execute_script("arguments[0].click();", element)
        while(len(driver.find_elements_by_class_name("k-state-border-down"))==0):
            driver.execute_script("arguments[0].click();", element)
       
        element.send_keys(Keys.DOWN) 
        driver.find_element_by_class_name("form-control").send_keys("0542255135")
        driver.find_element_by_class_name("//div[@id='grid']/div/div/div/div/span/span/span[2]/span").click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()