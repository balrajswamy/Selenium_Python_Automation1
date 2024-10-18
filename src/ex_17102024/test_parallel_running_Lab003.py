from selenium import webdriver
import time
import allure
import pytest
import requests

@allure.title("Test Case to Open App.Vwo.com TC#1")
@allure.description("To verify th Current Url with Chrome browser")
@pytest.mark.smoke
def test_current_url_verification_chrome():
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    title = driver.title
    print("Title:\t", title)
    assert driver.current_url == "https://app.vwo.com/#/login", "The given URL is not Matching"
    assert driver.title == "Login - VWO"
    time.sleep(3)
    driver.quit()


@allure.title("Test Case to Open App.Vwo.com TC#2")
@allure.description("To verify th Current Url with Edge browser")
@pytest.mark.smoke
def test_current_url_verification_edge():
    driver = webdriver.Edge()
    time.sleep(1)
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    title = driver.title
    print("Title:\t", title)
    assert driver.current_url == "https://app.vwo.com/#/login", "The given URL is not Matching"
    assert driver.title == "Login - VWO"
    time.sleep(3)
    driver.quit()

@allure.title("Test Case to Open App.Vwo.com TC#3")
@allure.description("To verify th Current Url with Firefox browser")
@pytest.mark.smoke
def test_current_url_verification_firefox():
    driver = webdriver.Firefox()
    time.sleep(1)
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    title = driver.title
    print("Title:\t", title)
    assert driver.current_url == "https://app.vwo.com/#/login", "The given URL is not Matching"
    assert driver.title == "Login - VWO"
    time.sleep(3)
    driver.quit()