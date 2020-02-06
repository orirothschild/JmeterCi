
from pytest import mark
import pytest
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains

@mark.reports
@pytest.mark.usefixtures("shufersal_chrome_login")
class Reports_Tests:  
    def test_tavim_reports_as_excpected(self,shufersal_chrome_login):
        self.driver=shufersal_chrome_login[0]
        self.verificationErrors =shufersal_chrome_login[1]
        self.accept_next_alert =shufersal_chrome_login[2]
        driver = self.driver
        driver.get("http://172.29.46.11/Reports/ReportsHistory")
        driver.find_element_by_id("FieldFilter").clear()
        element =driver.find_element_by_class_name("k-input")
        driver.execute_script("arguments[0].click();", element)
        while(len(driver.find_elements_by_class_name("k-state-border-down"))==0):
            driver.execute_script("arguments[0].click();", element)
       
        element.send_keys(Keys.DOWN) 
        driver.find_element_by_class_name("form-control").send_keys("0542255135")
        driver.find_element_by_class_name("//div[@id='grid']/div/div/div/div/span/span/span[2]/span").click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()