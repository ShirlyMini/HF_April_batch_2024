from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPageObj import LoginPage
from Utilities.ReadCommonData import ReadProperty
from Utilities.CustomLogger import Logger
from TestData import load_data


class Test_Suite_DDT:
    logg=Logger()
    xlpath = r"..\TestData\LoginData.xlsx"

    @pytest.mark.regression
    @pytest.mark.parametrize("user, pswd, expected", load_data.load_td_from_xl(xlpath, "Sheet1"))
    def test_verify_dashboardpage_ddt(self, launch_browser, user, pswd, expected):
        driver = launch_browser
        login_obj = LoginPage(driver)
        login_obj.SetEmail(user)
        login_obj.SetPassword(pswd)
        login_obj.ClickLogin()
        sleep(5)
        self.logg.info("OrangeHRM Application logged in successfully..")
        title = login_obj.Get_DashbordTitle()
        self.logg.info(title)
        if title!="Dashboard" and expected=="Fail":
            self.logg.info("TC:test_verify_dashboardpage_ddt = PASS")
            assert True
        elif title=="Dashboard" and expected=="Pass":
            self.logg.info("TC:test_verify_dashboardpage_ddt = PASS")
            assert True
        else:
            self.logg.error("TC:test_verify_dashboardpage_ddt = FAIL")
            driver.save_screenshot(r"..\ScreenShot\test_verify_dashboardpage_ddt.png")
            assert False

