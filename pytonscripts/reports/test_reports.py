import glob
import os
import time
from pathlib import Path

import pandas as pd
import pytest
from pytest import mark
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xlsxwriter.utility import xl_rowcol_to_cell

from Excel.Compare.test_ExcelCompare import test_excelCompare


@mark.smoke
@mark.reports
class Reports_Tests:
    @pytest.mark.dependency(name="a")
    @pytest.mark.usefixtures("shufersal_chrome_login")
    def test_tavim_reports_as_excpected(self, shufersal_chrome_login):
        driver = shufersal_chrome_login[0]
        verificationErrors = shufersal_chrome_login[1]
        accept_next_alert = shufersal_chrome_login[2]
        dbc = shufersal_chrome_login[3]
        driver.get(shufersal_chrome_login[4])
        driver.find_element_by_id("FieldFilter").clear()
        element = driver.find_element_by_xpath("/html/body/div[2]/nav/div/ul/li[3]/span")
        driver.execute_script("arguments[0].click();", element)
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/nav/div/ul/li[3]/ul/li[1]/a")))
        time.sleep(2.5)
        element = driver.find_element_by_xpath("/html/body/div[2]/nav/div/ul/li[3]/ul/li[1]/a").click()
        element = WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
        time.sleep(2.5)
        element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div[1]/div/div/div['
                                               '1]/span/span/span[1]')
        # driver.execute_script("arguments[0].click();", element)
        while len(driver.find_elements_by_class_name("k-state-border-down")) == 0:
            driver.execute_script("arguments[0].click();", element)
            if len(driver.find_elements_by_class_name("k-state-border-down")) != 0:
                driver.find_element_by_xpath("/html/body/div[3]/div/span/input").clear()
                driver.find_element_by_xpath("/html/body/div[3]/div/span/input").send_keys("א.ב")
                time.sleep(1)
                actions = ActionChains(driver)
                actions.send_keys(Keys.ENTER).perform()
                #text = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/ul/li[1]").text
                # if len(driver.find_elements_by_class_name("k-state-border-down")) != 0:
        driver.find_element_by_class_name("form-control").send_keys("050740239")
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div[1]/div/div/div[2]/div/span['
                                     '2]/button').click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
        time.sleep(2)

    @pytest.mark.dependency(depends=["a"])
    def test_tevim_excel_as_expected(self):
        test_excelCompare("misgeret_limit_information")
