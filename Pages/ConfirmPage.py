from selenium.webdriver.common.by import By

from Pages.PurchasePage import PurchasePage


class ConfirmPage():
    def __init__(self,driver):
        self.driver=driver

    Checkoutandbuydevicebtn=(By.XPATH,"//button[@class='btn btn-success']")

    def Checkoutandbuydevice(self):
        self.driver.find_element(*ConfirmPage.Checkoutandbuydevicebtn).click()
        purchasepage=PurchasePage(self.driver)
        return purchasepage