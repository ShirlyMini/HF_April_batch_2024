from selenium.webdriver.common.by import By


class LoginPage:
    # steps
    # locator
    xpath_email="//input[@name='username']"
    xpath_pswd="//input[@name='password']"
    xpath_login = "//button[@type='submit']"
    xpath_dashbord_title="//h6"

    # constructor
    def __init__(self, driver):
        self.driver=driver


    # create steps
    def SetEmail(self, email):
        self.driver.find_element(By.XPATH, self.xpath_email).clear()
        self.driver.find_element(By.XPATH, self.xpath_email).send_keys(email)

    def SetPassword(self, pswd):
        self.driver.find_element(By.XPATH, self.xpath_pswd).clear()
        self.driver.find_element(By.XPATH, self.xpath_pswd).send_keys(pswd)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()

    def Get_DashbordTitle(self):
        try:
            return self.driver.find_element(By.XPATH, self.xpath_dashbord_title).text
        except:
            return False
