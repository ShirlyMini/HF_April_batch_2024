from time import sleep
import pytest
from PageObjects.LoginPageObj import LoginPage
from PageObjects.RecuritmentPageobj import Recruitment
from Utilities.ReadCommonData import ReadProperty
from Utilities.CustomLogger import Logger


class Test_Suite_Recuritment:
    logg=Logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_verify_Recuirtment_basic(self, launch_browser):
        driver = launch_browser
        login_obj = LoginPage(driver)
        login_obj.SetEmail(ReadProperty.GetUsername())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        sleep(5)
        self.logg.info("OrangeHRM Application logged in successfully..")

        rec_obj = Recruitment(driver)
        rec_obj.recruitment_clk()
        rec_obj.add_click()
        rec_obj.firstname("shirly")
        rec_obj.lastname("J")
        rec_obj.email("abc@gmail.com")
        rec_obj.save()
        sleep(10)
        status = rec_obj.verify_recruitment_application("shirly", "J")
        if status!=True:
            self.logg.error("TC:test_verify_Recuirtment_basic = FAIL")
            driver.save_screenshot(r"..\ScreenShot\test_verify_Recuirtment_basic.png")
            assert False
        else:
            self.logg.info("TC:test_verify_Recuirtment_basic = PASS")
            assert True



