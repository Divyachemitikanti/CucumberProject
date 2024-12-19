POM1
----

#launch the url 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators for the registration form
    first_name = (By.ID, "input-firstname")
    last_name = (By.ID, "input-lastname")
    email = (By.ID, "input-email")
    telephone = (By.ID, "input-telephone")
    password = (By.ID, "input-password")
    confirm_password = (By.ID, "input-confirm")
    newsletter_yes = (By.XPATH, "//input[@name='newsletter'][@value='1']")
    privacy_policy = (By.XPATH, "//input[@name='agree']")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    warning_message = (By.CSS_SELECTOR, ".alert-danger")
    success_message = (By.CSS_SELECTOR, ".alert-success")
    # Method to fill in personal details
    def fill_personal_details(self, first_name_val, last_name_val, email_val, telephone_val):
        self.driver.find_element(*self.first_name).send_keys(first_name_val)
        self.driver.find_element(*self.last_name).send_keys(last_name_val)
        self.driver.find_element(*self.email).send_keys(email_val)
        self.driver.find_element(*self.telephone).send_keys(telephone_val)
    # Method to enter password and confirm password
    def enter_password(self, password_val):
        self.driver.find_element(*self.password).send_keys(password_val)
        self.driver.find_element(*self.confirm_password).send_keys(password_val)
    # Method to agree to the privacy policy
    def agree_to_privacy_policy(self):
        self.driver.find_element(*self.privacy_policy).click()
    # Method to click on 'Continue'
    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
    # Method to verify the warning message
    def get_warning_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.warning_message))
        return self.driver.find_element(*self.warning_message).text
    # Method to verify the success message
    def get_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message))
        return self.driver.find_element(*self.success_message).text

POM2
----
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class AccountPage:
    def __init__(self, driver):
        self.driver = driver
    # Locator for the 'View your Order history' link
    order_history_link = (By.LINK_TEXT, "View your order history")
    def click_order_history(self):
        self.driver.find_element(*self.order_history_link).click()
code
----
import time
from selenium import webdriver
from Open_Cart_POM1 import RegistrationPage  # Import the RegistrationPage class
from Open_Cart_POM2 import AccountPage  # Import the AccountPage class
from selenium.webdriver.common.by import By
class TestOpencartRegistration:
    def setup_method(self):
        # Step 1: Launch the browser and open the website
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.opencart.com.gr/")
        self.driver.maximize_window()
    def teardown_method(self):
        # Step 8: Close the browser after the test
        self.driver.quit()
    def test_registration(self):
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        registration_page = RegistrationPage(self.driver)
        # Step2: Verify the title (Page heading)
        assert self.driver.title == "Register Account"
        # Step3: Fill in the registration details
        registration_page.fill_personal_details("Divya", "Ch", "divyachemitikanti24@gmail.com", "9177583383")
        # Step4: Enter valid password
        registration_page.enter_password("Divya@1124")
        # Step5: Agree to the privacy policy
        registration_page.agree_to_privacy_policy()
        # Step6: Click 'Continue'
        registration_page.click_continue()
        # Step7: Check if the "Privacy Policy" warning appears
        warning_msg = registration_page.get_warning_message()
        assert "Warning: You must agree to the Privacy Policy!" in warning_msg
        # Step8: Agree to privacy policy, re-submit and check if account is created
        registration_page.agree_to_privacy_policy()
        registration_page.click_continue()
        time.sleep(2)  # Wait for the page to load
        # Step9: Verify success message
        success_msg = registration_page.get_success_message()
        assert "Your Account Has Been Created!" in success_msg
        # Step10: After account creation, view order history
        account_page = AccountPage(self.driver)
        account_page.click_order_history()
        time.sleep(2) # Wait for the page to load
