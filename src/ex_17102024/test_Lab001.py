from selenium import webdriver
import time
import allure
import pytest
import requests

@allure.title("Test Case to Open App.Vwo.com TC#1")
@allure.description("To verify th Current Url")
@pytest.mark.smoke
def test_open_vwo_login():
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    title = driver.title
    print("Title:\t", title)
    assert driver.current_url == "https://app.vwo.com/#/login", "The given URL is not Matching"
    assert driver.title == "Login - VWO"
    time.sleep(12)
    driver.quit()

@allure.title("Test Case to Open https://katalon-demo-cura.herokuapp.com TC#2")
@allure.description("To verify th Current Url and verify the text from the Page_source")
@pytest.mark.smoke
def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(3)
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    time.sleep(3)
    driver.quit()

