import pyodbc
from pytest import fixture

from config import Config
from drivers.drivers import chrome

driver = chrome()


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="choose the Enviroment to run tests in"
    )


@fixture()
def env(request):
    return request.config.getoption("--env")


@fixture()
def web_config(env):
    return Config(env)


def create_db_conn(servername):
    yield pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                         server=servername,
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


@fixture(scope="module")
def get_chrome():
    yield driver
    driver.quit()


@fixture(params=['https://shufersal.verifone.co.il/Orders/OrdersUpdate',
                 'http://172.29.46.11/Orders/OrdersUpdate'])  # run once per each site in chrome
def shufersal_chrome_login(get_chrome, request):
    # connect to webdrsiver
    con = '172.29.25.20\sql2005' if request.param == 'https://shufersal.verifone.co.il/Orders/OrdersUpdate' else '172.29.92.20\sql2005'
    dbc = create_db_conn(con)
    driver_shufersal = get_chrome
    errors = []
    accept_next_alert = True
    driver_shufersal.get(request.param)
    driver_shufersal.find_element_by_id("Email").clear()
    driver_shufersal.find_element_by_id("Email").send_keys("omri@dts-4u.com")
    driver_shufersal.find_element_by_id("password").click()
    driver_shufersal.find_element_by_id("password").clear()
    driver_shufersal.find_element_by_id("password").send_keys("1234567")
    driver_shufersal.find_element_by_id("loginsystem").click()
    chrome_essentials = [driver_shufersal, errors, accept_next_alert]

    yield driver_shufersal, errors, accept_next_alert, dbc, request.param
