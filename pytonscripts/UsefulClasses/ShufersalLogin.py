
from drivers.drivers import mydriver
currentdriver=mydriver() #connect to webdriver 
chromepath = currentdriver.chrome
downloads_path ='/c/Users/orir/Downloads/'
file_path ="ניהול הזמנה_יום שלישי 14 ינואר 2020"
from selenium import webdriver
import pyodbc 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; Server=172.29.45.45\sql2005;Database=ShufersalTavim;UID=sqladmin;PWD=Erg0110$;Trusted_Connection=no;')

cursor = conn.cursor()
element = cursor.execute('SELECT * FROM Orders')


class ShufersalLogin_Tests:
    def __init__(self):
         self.name = "אורי"
         self.Pass = "א.ב"

    def chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(executable_path=chromepath,chrome_options=options)
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
        self.driver.get("http://172.29.46.11/User/Login?ReturnUrl=%2FOrders%2FOrdersUpdate")
        self.driver.find_element_by_id("Email").clear()
        self.driver.find_element_by_id("Email").send_keys("omri@dts-4u.com")
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("1234567")
        self.driver.find_element_by_id("loginsystem").click()
        chrome_essentials=[self.driver,self.verificationErrors, self.accept_next_alert]
        return chrome_essentials
