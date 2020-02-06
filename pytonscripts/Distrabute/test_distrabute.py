# -*- coding: utf-8 -*-
from pytest import mark
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re


@mark.distrabute
@pytest.mark.usefixtures("shufersal_chrome_login")
class DISTRABUTE_Tests:
    def test_distribute_cards(self,shufersal_chrome_login):
        self.driver=shufersal_chrome_login[0]
        self.verificationErrors =shufersal_chrome_login[1]
        self.accept_next_alert =shufersal_chrome_login[2]
        driver = self.driver
        driver.get(shufersal_chrome_login[3])
        element = WebDriverWait(driver,7).until(
        EC.invisibility_of_element_located((By.CLASS_NAME,"k-loading-mask")))
        driver.find_element_by_xpath("//div[@id='grid']/div/div/div[2]/div/span/span/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").send_keys(self.COSTUMER)
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='custmoers-list']/span/input").send_keys(Keys.DOWN)
        element = WebDriverWait(driver,8).until(
        EC.invisibility_of_element_located((By.CLASS_NAME,"k-loading-mask")))

        driver.find_element_by_xpath("//div[@id='grid']/table/tbody/tr[2]/td[11]/a").click()

        element = WebDriverWait(driver,40).until(
        EC.visibility_of_element_located((By.XPATH,"//div[@id='Wizard_TabStrip-1']/form/div[6]/label")))
        driver.find_element_by_xpath("//div[@id='Wizard_TabStrip-1']/form/div[6]/label").click()
        driver.find_element_by_xpath("//div[@id='Wizard_TabStrip-1']/form/div[6]/label").click()
        element = WebDriverWait(driver,3).until(
        EC.visibility_of_element_located((By.XPATH,"//div[@id='Wizard_TabStrip-1']/form/div[6]/label")))
        driver.find_element_by_name("arr[emp0][0]").clear()
        driver.find_element_by_name("arr[emp0][1]").clear()
        driver.find_element_by_name("arr[emp0][2]").clear()
        driver.find_element_by_name("arr[emp0][3]").clear()
        driver.find_element_by_name("arr[emp0][0]").send_keys(self.NAME)
        driver.find_element_by_name("arr[emp0][1]").send_keys("0542255135")
        driver.find_element_by_name("arr[emp0][2]").send_keys("311321590")
        driver.find_element_by_name("arr[emp0][3]").send_keys("100")
        element = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.ID,'Wizard_Next')))
        element.click()
        element = WebDriverWait(driver,13).until(
        EC.element_to_be_clickable((By.ID,'Wizard_Next')))
        element.click()
        element = WebDriverWait(driver,13).until(
        EC.element_to_be_clickable((By.ID,'SmsContent')))
        driver.find_element_by_id("SmsContent").click()
        driver.find_element_by_id("SmsContent").clear()
        driver.find_element_by_id("SmsContent").send_keys(u"[שם עובד]יגבר\nרק בדיקה אל תתלהב בבקשה [סכום] ₪")
        element = WebDriverWait(driver,25).until(
        EC.element_to_be_clickable((By.ID,'Wizard_Next')))
        element.click()
        driver.find_element_by_id("GreetingAlternateWorkerName").click()
        driver.find_element_by_id("GreetingAlternateWorkerName").clear()
        driver.find_element_by_id("GreetingAlternateWorkerName").send_keys(u"עובד יקר זאת בדיקה אוטומטית ")
        driver.find_element_by_id("Wizard_Next").click()
        driver.find_element_by_id("EmpCheckPhone").click()
        driver.find_element_by_id("EmpCheckPhone").clear()
        driver.find_element_by_id("EmpCheckPhone").send_keys("0542255135")
        driver.find_element_by_id("sendsmsphone").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_id("Wizard_Next").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        
    @mark.skip
    def test_sql_data_to_be_true():
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; Server=172.29.45.45\sql2005;Database=ShufersalTavim;UID=sqladmin;PWD=Erg0110$;Trusted_Connection=no;')
        cursor = conn.cursor()
        sql = 'select Max(OrderId)as id from Orders '
        id = cursor.execute(sql)
        for row in id:id = row.id
        sql = ('''select top 1 od.IsDone,od.IsSuccess from ShufersalTavim..OrderDistribution od where orderid IN (?) ORDER by od.Timestamp desc''')
        params=(id)     
        assert all(row.IsDone ==True and row.IsSuccess ==True for row in cursor.execute(sql,params))
  



    