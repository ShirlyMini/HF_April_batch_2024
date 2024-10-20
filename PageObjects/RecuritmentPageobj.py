from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Recruitment:

    ## Steps
    ## Locators

    xpath_Recruitment="//span[text()='Recruitment']"
    add_button="//button[normalize-space( )='Add']"
    Fname_xpath="//input[@name='firstName']"
    Mname_xpath="//input[@name='middleName']"
    Lname_xpath="//input[@name='lastName']"
    email_type="(//input[@placeholder='Type here'])[1]"
    contact_type="(//input[@placeholder='Type here'])[2]"
    Browse="//div[contains(text(),'Browse')]"
    keywords_xpath="//input[@placeholder='Enter comma seperated words...']"
    date_xpath="//input[@placeholder='yyyy-dd-mm']"
    notes_xpath="(//textarea[@placeholder='Type here'])[1]"
    keep_data="//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
    save_button="//button[normalize-space()='Save']"
    ##select vacancy
    vacancy_xpath=" (//label[normalize-space()='Vacancy']//following::i)[1]"
    select_CFO_position="// div[contains(text(), 'CFO Position')]"
    # verify_name = "//p[text()={fname} {mname} {lname}]"


    ## Constructor
    def __init__(self,driver):
        self.driver=driver

    # def _wait_for_is_displayed(self, by, value, timeout):
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         wait.until(expected_conditions.visibility_of_element_located((by, value)))
    #     except TimeoutException:
    #         return False
    #     return True
    ## Steps

    def recruitment_clk(self):
        #self._wait_for_is_displayed(By.XPATH, self.xpath_Recruitment, 10)
        self.driver.find_element(By.XPATH, self.xpath_Recruitment).click()

    def add_click(self):
        self.driver.find_element(By.XPATH,self.add_button).click()

    def firstname(self,Fname):
        self.driver.find_element(By.XPATH,self.Fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.Fname_xpath).send_keys(Fname)

    def middlename(self, Mname):
        self.driver.find_element(By.XPATH, self.Mname_xpath).clear()
        self.driver.find_element(By.XPATH, self.Mname_xpath).send_keys(Mname)

    def lastname(self, Lname):
        self.driver.find_element(By.XPATH, self.Lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.Lname_xpath).send_keys(Lname)

    def vacancy(self):
        self.driver.find_element(By.XPATH,self.vacancy_xpath).click()

        self.driver.find_element(By.XPATH,self.select_CFO_position)

    def email(self,email):
        self.driver.find_element(By.XPATH,self.email_type).clear()
        self.driver.find_element(By.XPATH, self.email_type).send_keys(email)


    def contact_no(self,number):
        self.driver.find_element(By.XPATH,self.contact_type).clear()
        self.driver.find_element(By.XPATH, self.contact_type).send_keys(number)


    # def browse(self):
    #     self.driver.find_element(By.XPATH,self.Browse)
    ## Need to as harshal how to make it

    def keywords(self,keywords):
        self.driver.find_element(By.XPATH,self.keywords_xpath).clear()
        self.driver.find_element(By.XPATH, self.keywords_xpath).send_keys(keywords)

    def date(self,Date):
        self.driver.find_element(By.XPATH,self.date_xpath).send_keys(Date)

    def notes(self,Notes):
        self.driver.find_element(By.XPATH,self.notes_xpath).clear()
        self.driver.find_element(By.XPATH, self.notes_xpath).send_keys(Notes)

    def keepdata(self):
        self.driver.find_element(By.XPATH,self.keep_data).click()

    def save(self):
        self.driver.find_element(By.XPATH,self.save_button).click()

    def verify_recruitment_application(self, fname, lname, mname=""):
        return self.driver.find_element(By.XPATH, f"//p[text()='{fname} {mname} {lname}']").is_displayed()




