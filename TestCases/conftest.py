from time import sleep

import pytest
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.edge.service import Service as edge_service
from selenium.webdriver.firefox.service import Service as firefox_service
from Utilities.ReadCommonData import ReadProperty
from Utilities.CustomLogger import Logger
log = Logger()
@pytest.fixture()
def launch_browser(request):
    browser = request.config.getoption("--browser")
    if browser=="chrome":
        ch_service_obj = chrome_service(ReadProperty.GetChromeDriver())
        driver = uc.Chrome(service=ch_service_obj)
    elif browser=="edge":
        #ms_service_obj = edge_service(ReadProperty.GetEdgeDriver())
        ms_service_obj = edge_service()
        driver = webdriver.Edge(service=ms_service_obj)
    elif browser=="firefox":
        ff_service_obj = firefox_service(ReadProperty.GetFirefoxDriver())
        driver = webdriver.Firefox(service=ff_service_obj)
    else:
        ch_service_obj = chrome_service(ReadProperty.GetChromeDriver())
        driver = webdriver.Chrome(service=ch_service_obj)

    driver.get(ReadProperty.GetUrl())
    driver.maximize_window()
    driver.implicitly_wait(10)
    #sleep(180)
    log.info("NopCommerce Application launched successfully..")
    yield driver
    driver.quit()

def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: this is a tag name for smoke test cases")
    config.addinivalue_line("markers", "sanity: this is a tag name for Sanity test cases")
    config.addinivalue_line("markers", "regression: this is a tag name for Regression test cases")
