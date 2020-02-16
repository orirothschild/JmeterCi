from selenium import webdriver


# def __init__(self):
#    self.chrome = "D:\drivers\chrome\chromedriver.exe"
#    self.firefox = "D:\drivers\geckodriver.exe"

def firefox(self):
    return "D:\drivers\geckodriver.exe"


def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    chrome_drive = webdriver.Chrome(executable_path="D:\drivers\chrome\chromedriver.exe", chrome_options=options)
    chrome_drive.implicitly_wait(3)
    chrome_drive.maximize_window()
    return chrome_drive


if __name__ == "__main__":
    driver = chrome()
    print(driver)
