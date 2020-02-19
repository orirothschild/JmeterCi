import time
import pytest
from pytest import mark
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Excel.Compare.test_ExcelCompare import excelCompare
from selenium.webdriver.common.keys import Keys

relevant_report = ['דוח היסטוריית מסגרת הזמנה']
counter = 0


def instances(name, params):
    def vstr(val):
        if isinstance(val, (list, tuple)):
            return "-".join([str(v) for v in val])
        else:
            return str(val)

    return ["%s[%s]" % (name, vstr(v)) for v in params]


# this class oprates all the reports for shufersal from the reports dropdown bar
def check_for_diffrence_in_reports_from_excel_file(report_name, sum_of_all_envs):
    global counter
    if counter == sum_of_all_envs:
        excelCompare(f"{report_name}")
        counter = 0
        assert True
    return


@mark.smoke
@mark.reports
@pytest.mark.usefixtures("shufersal_chrome_login")
class Reports_Tests:
    def execute_reports_by_parameter(self, driver,
                                     relevant_report):

        # # הערכים DROPDOWN,DRIVER מייצגים את הדרייבר המריץ את סלניום ואת הערך של הדוח הרלוונטי
        # # קוד המריץ דוח, ממודה שהדוח לוחץ על ה קנדו ובודק את כול הרשומות עבור חברה גנרית, למשל א.ב הובלות בעמ
        element = driver.find_element_by_xpath("/html/body/div[2]/nav/div/ul/li[3]/span")
        driver.execute_script("arguments[0].click();", element)
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, f'{relevant_report}')))
        element = WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
        time.sleep(2)
        driver.find_element_by_link_text(f'{relevant_report}').click()
        element = WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
        time.sleep(2)
        element = driver.find_element_by_class_name('k-input')
        sent_keys_flag = True
        while len(driver.find_elements_by_class_name("k-state-border-down")) == 0 and sent_keys_flag:
            driver.execute_script("arguments[0].click();", element)
            if len(driver.find_elements_by_class_name("k-state-border-down")) != 0:
                driver.find_element_by_xpath("/html/body/div[3]/div/span/input").clear()
                if len(driver.find_elements_by_class_name("k-state-border-down")) != 0:
                    time.sleep(1)
                    if len(driver.find_elements_by_class_name("k-state-border-down")) != 0:
                        driver.find_element_by_xpath("/html/body/div[3]/div/span/input").send_keys("א.ב")
                    else:
                        continue
                else:
                    continue
                time.sleep(1)
                actions = ActionChains(driver)
                actions.send_keys(Keys.ENTER).perform()
                if driver.find_element_by_xpath("//span/span/span[1]").text != 'בחר ארגון...':
                    sent_keys_flag = False
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div[1]/div/div/div[2]/div/span['
                                     '2]/button').click()
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
        time.sleep(2)
        global counter
        counter += 1
        return True

    @pytest.mark.usefixtures("shufersal_chrome_login")
    @mark.parametrize('relevant_report', relevant_report)
    # הטסט הראשון שרץ, קורה לפונקצית הניהול של התחברות לשופרסל ולאחר מכן מושף ממנו את הדרייבר,חיבור דאטאבייס ומעביר
    # את חיפוש הדוחות לפונקציה הבאה
    @pytest.mark.dependency(name="a")
    def test_tavim_reports_as_excpected(self, shufersal_chrome_login,
                                        relevant_report):
        driver = shufersal_chrome_login[0]
        verificationErrors = shufersal_chrome_login[1]
        accept_next_alert = shufersal_chrome_login[2]
        dbc = shufersal_chrome_login[3]
        driver.get(shufersal_chrome_login[4])
        driver.find_element_by_id("FieldFilter").clear()
        self.execute_reports_by_parameter(driver, relevant_report)
        check_for_diffrence_in_reports_from_excel_file(relevant_report, shufersal_chrome_login[5])

    # @mark.parametrize('report_name', ['דוח פירוט הפצות להזמנה'])
    # def test_tevim_excel_as_expected(self, report_name, shufersal_chrome_login):
    #     global counter
    #     if counter == shufersal_chrome_login[5]:
    #         excelCompare(f"{report_name}")
    #         counter = 0
    #     assert True
