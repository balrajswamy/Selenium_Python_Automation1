from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import pytest
import time

@allure.title("Test Case to Check ChromeOptions TC#1")
@allure.description("To verify th Current Url with cognito mode")
@pytest.mark.bala
def test_check_chrome_options1():
    chrome_options = Options()
    #chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--start_maximized")
    #chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    time.sleep(1)
    #driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    title = driver.title
    print("Title:\t", title)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/", "The given URL is not Matching"

    time.sleep(3)
    driver.quit()

@allure.title("Test Case to Check ChromeOptions TC#2")
@allure.description("To verify th Current Url with Headless or No UI visible")
@pytest.mark.bala
def test_check_chrome_options2():
    chrome_options = Options()
    #chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--start_maximized")
    #chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    time.sleep(1)
    #driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    title = driver.title
    print("Title:\t", title)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/", "The given URL is not Matching"

    time.sleep(3)
    driver.quit()