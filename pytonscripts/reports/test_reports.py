import glob
import os
import time
from pathlib import Path

import pandas as pd
import pytest
from pytest import mark
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Excel.Compare.test_ExcelCompare import test_excelCompare
from selenium.webdriver.common.keys import Keys


@mark.smoke
@mark.reports
class Reports_Tests:
    def execute_reports_by_parameter(self, driver, drop_down):
        element = driver.find_element_by_xpath("/html/body/div[2]/nav/div/ul/li[3]/span")
        driver.execute_script("arguments[0].click();", element)
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, f'{drop_down}')))
        time.sleep(2.5)
        driver.find_element_by_link_text(f'{drop_down}').click()
        element = WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
        time.sleep(2.5)
        element = driver.find_element_by_class_name('k-input')
        # driver.execute_script("arguments[0].click();", element)
        sent_keys_flag = True
        while len(driver.find_elements_by_class_name("k-state-border-down")) == 0 and sent_keys_flag:
            driver.execute_script("arguments[0].click();", element)
            if len(driver.find_elements_by_class_name("k-state-border-down")) != 0:
                driver.find_element_by_xpath("/html/body/div[3]/div/span/input").clear()
                driver.find_element_by_xpath("/html/body/div[3]/div/span/input").send_keys("א.ב")
                time.sleep(1)
                actions = ActionChains(driver)
                actions.send_keys(Keys.ENTER).perform()
                if driver.find_element_by_xpath("//span/span/span[1]").text != 'בחר ארגון...':
                    sent_keys_flag = False
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div[1]/div/div/div[2]/div/span['
                                     '2]/button').click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
        time.sleep(2)

    @pytest.mark.dependency(name="a")
    @pytest.mark.usefixtures("shufersal_chrome_login")
    @mark.parametrize('drop_down', ['דוח היסטוריית מסגרת הזמנה', 'דוח פירוט הפצות להזמנה'])
    def test_tavim_reports_as_excpected(self, shufersal_chrome_login, drop_down):
        driver = shufersal_chrome_login[0]
        verificationErrors = shufersal_chrome_login[1]
        accept_next_alert = shufersal_chrome_login[2]
        dbc = shufersal_chrome_login[3]
        driver.get(shufersal_chrome_login[4])
        driver.find_element_by_id("FieldFilter").clear()
        self.execute_reports_by_parameter(driver, drop_down)

    @pytest.mark.dependency(depends=["a"])
    @mark.parametrize('rep', ['דוח פירוט הפצות להזמנה'])
    def test_tevim_excel_as_expected(self, rep):
        test_excelCompare(f"{rep}")
