from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PurchasePage():
    def __init__(self, driver):
        self.driver = driver

    countryname = (By.ID, "country")
    termscheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitbutton = (By.CSS_SELECTOR, "[type='submit']")
    successtext = (By.CLASS_NAME, "alert-success")

    def enterpartialcountrytext(self, countrytext):
        return self.driver.find_element(*PurchasePage.countryname).send_keys(countrytext)


    # comes from Baseclass
    # def waitforanelement(self,ele_text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located((By.LINK_TEXT, ele_text)))

    def clickonelement(self, element, text):
        return self.driver.find_element(element, text)

    def clickontermscheckbox(self):
        return self.driver.find_element(*PurchasePage.termscheckbox)

    def clickonsubmit(self):
        return self.driver.find_element(*PurchasePage.submitbutton)

    def asserttext(self):
        return self.driver.find_element(*PurchasePage.successtext)

    def get_screenshot(self):
        self.driver.get_screenshot_as_file("screen2.png")
