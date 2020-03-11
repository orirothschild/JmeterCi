import time
import pytest
from pytest import mark
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Excel.Compare.test_ExcelCompare import excelCompare
from selenium.webdriver.common.keys import Keys
import functools


def check_time_for_entire_execution(check_time):  # פונקצית עיצוב
    def decorator(func):
        @functools.wraps(func)
        def take_time(*args, **kwargs):  # לוגיקת המעצב
            if check_time:
                before = time.time()
                raise ZeroDivisionError(before)
                returned_func = func(*args, **kwargs)
                after = time.time()
                print(f'elepsed {after - before}')
            return returned_func

        return take_time  # החזרת המעצב הרלוונטי

    return decorator


# מציינים כמה דוחות שונים אנחנו חשוקים לבדוק
relevant_report = [('דוח היסטוריית מסגרת הזמנה', False)
                   # ,
                   #                ('דוח פירוט הפצות להזמנה', True),
                   #                ('דוח הזמנה', True),
                   #                ('דוח פעילות תווים', True)
                   ]

counter = 0


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
    # פעולה המבצעת את כול התהליכים הקשורים ללחיצה על הקנדו בתהליך דרופדאון
    def execute_drop_down(self, driver, dbc, additional_information_required):
        # מבצע פעולות שקשורות לקנדו המסריח שלא מקליק כמו שצריך
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
        self.additional_information_is_required(driver, additional_information_required, dbc)
        return

    def execute_reports_by_parameter(self, driver,
                                     relevant_report, additional_information_required, dbc):

        # # הערכים DROPDOWN,DRIVER מייצגים את הדרייבר המריץ את סלניום ואת הערך של הדוח הרלוונטי
        # # קוד המריץ דוח, ממודה שהדוח לוחץ על ה קנדו ובודק את כול הרשומות עבור חברה גנרית, למשל א.ב הובלות בעמ
        element = driver.find_element_by_xpath("//ul/li[3]/span")
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.LINK_TEXT, f'{relevant_report}')))
        WebDriverWait(driver, 50).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
        time.sleep(2)
        driver.find_element_by_link_text(f'{relevant_report}').click()
        WebDriverWait(driver, 50).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-image")))
        time.sleep(2)
        driver.find_element_by_class_name('k-input')
        self.execute_drop_down(driver, dbc, additional_information_required)
        driver.find_element_by_link_text(u"יצוא לאקסל").click()
        WebDriverWait(driver, 120).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-mask")))
        time.sleep(2)
        global counter
        counter += 1
        return True

    # פעולה שקוראת כאשר דוח מסוים זקוק למידה נוסף לארגון בלבד, כמו מסםר הזמנה
    def additional_information_is_required(self, driver, additional_information_required, dbc):
        if additional_information_required:
            element = driver.find_elements_by_xpath("//div[""2]/div/input")
            if isinstance(element, list):
                element = driver.find_element_by_xpath("//div[2]/span/span/span[1]")
                driver.execute_script("arguments[0].click();", element)
                time.sleep(0.2)
                WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[3]")))
                dbc.execute(
                    f'select top 1 ShufersalOrderId FROM Orders where CustomerId = 32002 and ShufersalOrderId is not '
                    f'null order by NEWID()')
                shufersal_order = dbc.fetchall()
                shufersal_order = str([x[0] for x in shufersal_order][0])
                driver.find_element_by_xpath("//div[4]/div/span/input").send_keys(shufersal_order)
                actions = ActionChains(driver)
                actions.send_keys(Keys.DOWN).perform()
                WebDriverWait(driver, 100).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "k-loading-mask")))
        return

    @pytest.mark.usefixtures("shufersal_chrome_login")
    @mark.parametrize('relevant_report, additional_information_required', relevant_report)
    @pytest.mark.dependency(name="a")
    # הטסט הראשון שרץ, קורה לפונקצית הניהול של התחברות לשופרסל ולאחר מכן מושף ממנו את הדרייבר,חיבור דאטאבייס ומעביר
    # את חיפוש הדוחות לפונקציה הבאה
    @check_time_for_entire_execution(True)
    def test_tavim_reports_as_excpected(self, shufersal_chrome_login,
                                        relevant_report, additional_information_required):
        driver = shufersal_chrome_login[0]
        driver.get(shufersal_chrome_login[4])
        dbc = shufersal_chrome_login[3]
        driver.find_element_by_id("FieldFilter").clear()
        self.execute_reports_by_parameter(driver, relevant_report, additional_information_required, dbc)
        # check_for_diffrence_in_reports_from_excel_file(relevant_report, shufersal_chrome_login[5])
