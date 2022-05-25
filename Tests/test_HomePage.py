import pytest
from selenium.webdriver.support.select import Select

from Pages.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData


@pytest.mark.usefixtures("getdata")
class Test_HomePage(BaseClass):
    def test_homepage(self, getdata):
        hp = HomePage(self.driver)

        # from tuple
        # hp.getname().send_keys(getdata[0])
        # hp.getemail().send_keys(getdata[1])

        # from dict
        hp.getname().send_keys(getdata[0]["firstname"])
        hp.getemail().send_keys(getdata[0]["email"])

        hp.getcheckbox().click()

        # self.SelectByOption(hp.getgender(), getdata[2])
        self.SelectByOption(hp.getgender(), getdata[0]["gender"])

        hp.submitform().click()
        successtext = hp.getSuccessMessage().text
        print(successtext)

        assert "Success!" in successtext
        self.driver.refresh()

    # from tuple
    # @pytest.fixture(params=[("Varun", "an.varun@gmail.com", "Male"),
    #                         ("Narasimha", "narasimha@gmail.com", "Male")])
    # def getdata(self, request):
    #     return request.param

    # from dict, get test data from HomePageData file
    # @pytest.fixture(params=HomePageData.test_Homepagedata)
    # def getdata(self, request):
    #     return request.param

    # from excel sheet, get test data from HomePageData file
    @pytest.fixture(params=[HomePageData.getexceldata("varun"), HomePageData.getexceldata("narasimha")])
    def getdata(self, request):
        print(request.param)
        return request.param
