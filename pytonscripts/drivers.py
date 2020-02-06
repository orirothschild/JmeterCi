from selenium import webdriver

#def __init__(self):
#    self.chrome = "D:\drivers\chrome\chromedriver.exe"
#    self.firefox = "D:\drivers\geckodriver.exe"

def firefox(self):
    return "D:\drivers\geckodriver.exe"

def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(executable_path="D:\drivers\chrome\chromedriver.exe",chrome_options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver



if __name__ == "__main__":
    driver =  chrome()    
    print(driver)