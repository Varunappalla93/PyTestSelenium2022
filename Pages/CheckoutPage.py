from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productname = (By.XPATH, "div/h4/a")
    addproduct=(By.XPATH,"div/button")

    def getproducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getproductname(self, product):
        return product.find_element(*CheckoutPage.productname)

    def addprodtocart(self,product):
        return product.find_element(*CheckoutPage.addproduct)


    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def clickcheckOutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutBtn).click()




