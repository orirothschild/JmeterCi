﻿#  -*- coding: utf-8 -*-
from pytest import mark
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re


@mark.orderdiff
@pytest.mark.usefixtures("shufersal_chrome_login")
def test_e_x_c_e_l(shufersal_chrome_login):
    driver = shufersal_chrome_login[0]
    verificationErrors = shufersal_chrome_login[1]
    accept_next_alert = shufersal_chrome_login[2]
    dbc = shufersal_chrome_login[3]
    driver.get(shufersal_chrome_login[4])
    element = driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='₪'])[1]/following::span[3]")  # .click()
    time.sleep(1)
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").send_keys(u"א.ב הובלות בעמ")
    time.sleep(1)
    element = driver.find_element_by_xpath("//div[@id='grid']/div/div/div[2]/div/span/span/span")
    time.sleep(1)
    driver.execute_script("arguments[0].click();", element)
    actions = ActionChains(driver)
    actions.send_keys(Keys.DOWN).perform()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "row")))
    time.sleep(6)
    driver.find_element_by_link_text(u"יצוא לאקסל").click()
    time.sleep(7)
