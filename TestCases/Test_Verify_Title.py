from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPageObj import LoginPage
from Utilities.ReadCommonData import ReadProperty
from Utilities.CustomLogger import Logger


class Test_Suite_Title:
    logg=Logger()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_verify_loginpage_title(self,launch_browser):
        driver = launch_browser
        self.logg.info(driver.title)
        if driver.title!="OrangeHRM":
            self.logg.error("TC:test_verify_loginpage_title = FAIL")
            driver.save_screenshot(r"..\ScreenShot\test_verify_loginpage_title.png")
            assert False
        else:
            self.logg.info("TC:test_verify_loginpage_title = PASS")
            assert True

    @pytest.mark.regression
    def test_verify_dashboardpage(self, launch_browser):
        driver = launch_browser
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        sleep(5)
        self.logg.info("OrangeHRM Application logged in successfully..")
        title = login_obj.Get_DashbordTitle()
        self.logg.info(title)
        if title!="Dashboard":
            self.logg.error("TC:test_verify_dashboardpage = FAIL")
            driver.save_screenshot(r"..\ScreenShot\test_verify_dashboardpage.png")
            assert False
        else:
            self.logg.info("TC:test_verify_dashboardpage = PASS")
            assert True

