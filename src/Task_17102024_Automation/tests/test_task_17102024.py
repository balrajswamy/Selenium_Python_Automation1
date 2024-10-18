import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestMakeAppointment():

    @allure.title('CURA Healthcare Service')
    @allure.description('Make an appointment')
    @allure.step("Open the website and click on Make Appointment")
    @pytest.mark.smoke
    def test_make_appointment(self):
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        # Step 1: Open the URL
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(1)
        #<a id="btn-make-appointment" href="./index.php#appointment" class="btn btn-dark btn-lg">Make Appointment</a>
        page_source_data = driver.page_source
        assert "Make Appointment" in page_source_data, "Not Found 'Make Appointment'"
        # Step 2: Click on the "Make Appointment" button
        make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
        time.sleep(1)
        make_appointment_button.click()

        # Step 3: Verify the URL is correct
        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", \
            f"URL did not match, found {driver.current_url}"

        # Step 4: Find the username and password input fields and enter the credentials
        username_field = driver.find_element(By.ID, "txt-username")
        time.sleep(1)
        password_field = driver.find_element(By.ID, "txt-password")

        username_field.send_keys("John Doe")
        time.sleep(1)
        password_field.send_keys("ThisIsNotAPassword")
        time.sleep(1)

        # Step 5: Click on the "Submit" button
        login_button = driver.find_element(By.ID, "btn-login")
        login_button.click()
        time.sleep(1)
        # Step 6: Verify that the URL has changed after logging in
        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", \
            f"Login URL did not match, found {driver.current_url}"

        driver.quit()
