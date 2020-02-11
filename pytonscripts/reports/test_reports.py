from pytest import mark
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re


@mark.smoke
@mark.reports
@pytest.mark.usefixtures("shufersal_chrome_login")
class Reports_Tests:
    def test_tavim_reports_as_excpected(self, shufersal_chrome_login):
        driver = shufersal_chrome_login[0]
        verificationErrors = shufersal_chrome_login[1]
        accept_next_alert = shufersal_chrome_login[2]
        dbc = shufersal_chrome_login[3]
        driver.get(shufersal_chrome_login[4])
        driver.find_element_by_id("FieldFilter").clear()
        element = driver.find_element_by_xpath("/html/body/div[2]/nav/div/ul/li[3]/span")
        driver.execute_script("arguments[0].click();", element)
        element = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/nav/div/ul/li[3]/ul/li[1]/a")))
        element = driver.find_element_by_xpath("/html/body/div[2]/nav/div/ul/li[3]/ul/li[1]/a").click()
        element = WebDriverWait(driver, 8).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))

        element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div[1]/div/div/div['
                                               '1]/span/span/span[1]')
        while len(driver.find_elements_by_class_name("k-state-border-down")) == 0:
            driver.execute_script("arguments[0].click();", element)
            driver.find_element_by_xpath("/html/body/div[4]/div/span/input").send_keys("א.ב")

        element.send_keys(Keys.DOWN)
        driver.find_element_by_class_name("form-control").send_keys("0542255135")
        driver.find_element_by_class_name("//div[@id='grid']/div/div/div/div/span/span/span[2]/span").click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
