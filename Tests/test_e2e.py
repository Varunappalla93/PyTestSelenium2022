from selenium.webdriver.common.by import By
from Pages.ConfirmPage import ConfirmPage
from Pages.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from Pages.ConfirmPage import ConfirmPage
from Pages.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getlogger()

        hp = HomePage(self.driver)
        checkoutpage = hp.shopItems()  # Use object chaining

        log.info("Getting card titles")

        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

        # cp = CheckoutPage(self.driver)
        # getproducttitles = cp.getproducts()
        # # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        getproducttitles = checkoutpage.getproducts()
        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        for product in getproducttitles:
            productName = checkoutpage.getproductname(product).text
            log.info(productName)
            if productName == "Blackberry":
                checkoutpage.addprodtocart(product)

                # Add item into cart
                # product.find_element_by_xpath("div/button").click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        # checkoutpage.clickcheckOutButton().click()

        checkoutpage.clickcheckOutButton()

        # Object chaining
        confirmPage = ConfirmPage(self.driver)
        purchasepage = confirmPage.Checkoutandbuydevice()

        log.info("Entering country name")
        purchasepage.enterpartialcountrytext("ind")

        # b=BaseClass
        # b.verifyLinkPresence(self,"India")

        # or
        self.verifyLinkPresence("India")

        purchasepage.clickonelement(By.LINK_TEXT, "India").click()
        purchasepage.clickontermscheckbox().click()
        purchasepage.clickonsubmit().click()
        success_text = purchasepage.asserttext().text
        log.info("text is" + success_text)

        assert "Success! Thank you!" in success_text

        # self.driver.get_screenshot_as_file("screen.png")
        purchasepage.get_screenshot()
