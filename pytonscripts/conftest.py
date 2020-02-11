﻿import pytest
from pytest import fixture
import sys
from drivers import chrome
import pyodbc
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
from config import Config
import argparse


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="choose the Enviroment to run tests in"
    )


# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; Server=172.29.45.45\sql2005;Database=ShufersalTavim;UID=sqladmin;PWD=Erg0110$;Trusted_Connection=no;')

# currentdriver=mydriver() #connect to webdriver
# chromepath = currentdriver.chrome
# from selenium import webdriver
# import pyodbc

# cursor = conn.cursor()
# element = cursor.execute('SELECT * FROM Orders')
@fixture()
def env(request):
    return request.config.getoption("--env")


@fixture()
def web_config(env):
    return Config(env)


def create_db_conn(servername):
    yield pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                         server='172.29.45.45\sql2005',
                         database='ShufersalTavim',
                         uid='sqladmin',
                         pwd='Erg0110$',
                         )


@fixture()  # this is if we have a test can should only run in a preticular env
def shufersal_chrome_login(web_config):
    driver = chrome()
    verificationErrors = []
    accept_next_alert = True
    driver.maximize_window()
    base_url = web_config.base_url
    port = web_config.web_port
    driver.get(base_url + ":" + port)
    driver.find_element_by_id("Email").clear()
    driver.find_element_by_id("Email").send_keys("omri@dts-4u.com")
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("1234567")
    driver.find_element_by_id("loginsystem").click()
    chrome_essentials = [driver, verificationErrors, accept_next_alert]

    yield driver, verificationErrors, accept_next_alert
    driver.quit()


@fixture(params=['https://shufersal.verifone.co.il/Orders/OrdersUpdate',
                 'http://172.29.46.11/Orders/OrdersUpdate'])  # run once per each site in chrome
def shufersal_chrome_login(request):
    # connect to webdrsiver
    con = '172.29.25.20\sql2005' if request.param == 'https://shufersal.verifone.co.il/Orders/OrdersUpdate' else '172.29.92.20\sql2005'
    dbc = create_db_conn(con)
    driver = chrome()
    verificationerrors = []
    accept_next_alert = True
    driver.get(request.param)
    driver.find_element_by_id("Email").clear()
    driver.find_element_by_id("Email").send_keys("omri@dts-4u.com")
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("1234567")
    driver.find_element_by_id("loginsystem").click()
    chrome_essentials = [driver, verificationerrors, accept_next_alert]

    yield driver, verificationerrors, accept_next_alert, dbc, request.param
    driver.quit()
