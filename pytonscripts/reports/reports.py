
from drivers import mydriver
currentdriver=mydriver() #connect to webdriver 
chromepath = currentdriver.chrome
downloads_path ='/c/Users/orir/Downloads/'
file_path ="ניהול הזמנה_יום שלישי 14 ינואר 2020"
from selenium import webdriver
import pyodbc 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; Server=172.29.45.45\sql2005;Database=ShufersalTavim;UID=sqladmin;PWD=Erg0110$;Trusted_Connection=no;')

cursor = conn.cursor()
element = cursor.execute('SELECT * FROM Orders')
import sys
from UsefulClasses.ShufersalLogin import ShufersalLogin 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os.path
import unittest, time

class REPORTS(unittest.TestCase):
    PHONE = "0507402339"
    @classmethod
    def setUpClass(self):
        self.chrome_essentials =ShufersalLogin().chrome()
        self.driver=self.chrome_essentials[0]
        self.verificationErrors = self.chrome_essentials[1]
        self.accept_next_alert = self.chrome_essentials[2]
        
        #SELF.DRIVER = WEBDRIVER.CHROME(EXECUTABLE_PATH=CHROMEPATH)
        #SELF.DRIVER.IMPLICITLY_WAIT(5)
        #SELF.VERIFICATIONERRORS = []
        #SELF.ACCEPT_NEXT_ALERT = TRUE
        #DRIVER = SELF.DRIVER
        #DRIVER.MAXIMIZE_WINDOW()
        #DRIVER.GET("HTTP://172.29.46.11/USER/LOGIN?RETURNURL=%2FORDERS%2FORDERSUPDATE")
        #DRIVER.FIND_ELEMENT_BY_ID("EMAIL").CLEAR()
        #DRIVER.FIND_ELEMENT_BY_ID("EMAIL").SEND_KEYS("OMRI@DTS-4U.COM")
        #DRIVER.FIND_ELEMENT_BY_ID("PASSWORD").CLICK()
        #DRIVER.FIND_ELEMENT_BY_ID("PASSWORD").CLEAR()
        #DRIVER.FIND_ELEMENT_BY_ID("PASSWORD").SEND_KEYS("1234567")
        #DRIVER.FIND_ELEMENT_BY_ID("LOGINSYSTEM").CLICK()
        
    
    def test_(self):
        driver = self.driver
        driver.get("http://172.29.46.11/Reports/ReportsHistory")
        driver.find_element_by_id("FieldFilter").clear()
        while(not driver.find_elements_by_class_name("k-dropdown-wrap k-state-default k-state-focused k-state-active k-state-border-down")):
            element =driver.find_element_by_class_name("k-input")
            driver.execute_script("arguments[0].click();", element)
            driver.execute_script("arguments[0].click();", element)
       
            
            driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name("form-control").send_keys("0542255135")
        driver.find_element_by_class_name("//div[@id='grid']/div/div/div/div/span/span/span[2]/span").click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    REPORTS.PHONE = os.environ.get('TEST_PHONE', REPORTS.PHONE)    
    unittest.main()
