import pyodbc
import pytest
from pytest import fixture
from pytest import mark

from Excel.Compare.test_ExcelCompare import excelCompare
from config import Config
from drivers.drivers import chrome

#global variables for driver and enviroments
driver = None
envs = ['https://shufersal.verifone.co.il/Orders/OrdersUpdate',
                                 'http://172.29.46.11//Orders/OrdersUpdate']


#function used for dependencies in pytest
def instances(name, params):
    def vstr(val):
        if isinstance(val, (list, tuple)):
            return "-".join([str(v) for v in val])
        else:
            return str(val)
    return ["%s[%s]" % (name, vstr(v)) for v in params]



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
def shufersal_chrome_login_config(web_config):
    local_driver = chrome()
    verificationErrors = []
    accept_next_alert = True
    local_driver.maximize_window()
    base_url = web_config.base_url
    port = web_config.web_port
    local_driver.get(base_url + ":" + port)
    local_driver.find_element_by_xpath('//span/input').clear()
    local_driver.find_element_by_xpath('//span/input').send_keys("omri@dts-4u.com")
    # driver.find_element_by_id("Email").clear()
    # driver.find_element_by_id("Email").send_keys("omri@dts-4u.com")
    local_driver.find_element_by_id("password").click()
    local_driver.find_element_by_id("password").clear()
    local_driver.find_element_by_id("password").send_keys("1234567")
    local_driver.find_element_by_id("loginsystem").click()
    chrome_essentials = [local_driver, verificationErrors, accept_next_alert]

    yield local_driver, verificationErrors, accept_next_alert
    local_driver.quit()


@fixture(scope="session")
def get_chrome():
    global driver
    driver = driver if driver is not None else chrome()
    yield driver
    driver.quit()


@pytest.mark.dependency(name="all_shufersal_logins")
@fixture(scope="module", params=envs)  # run once per each site in chrome
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

    return driver_shufersal, errors, accept_next_alert, dbc, request.param, len(envs)


@mark.parametrize('report_name', ['דוח פירוט הפצות להזמנה'])
@pytest.mark.dependency(depends=instances("shufersal_chrome_login", envs))
def test_tevim_excel_as_expected(report_name):
    excelCompare(f"{report_name}")
