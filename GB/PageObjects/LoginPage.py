
from .BasePage import BasePage
from .Locators.locators import MainPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import traceback
import logging

class LoginPage(BasePage):
    """Login page for flyefit"""

    def fill_form_fields(self, email, password):
        """Fill in form field details, email-addresss and password"""

        try:
            emailField = self.driver.find_element(*MainPageLocators.EMAIL)
            emailField.clear()
            emailField.send_keys(email)
            print("set email ")

            passwordField = self.driver.find_element(*MainPageLocators.PASSWORD)
            passwordField.clear()
            passwordField.send_keys(password)
            print("set password ")

        except Exception as e:
            print("Error Occured when filling forms", e.with_traceback)
            logging.error(traceback.format_exc())
        


    def click_go_button(self):
        """Triggers the search"""
        try:
            
            element = self.wait.until(EC.element_to_be_clickable((By.NAME, MainPageLocators.LOGIN_BUTTON[1])))
            # element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
            
            element.click()
        except Exception as e: 
            print("Error Occured while clicking login button", e.with_traceback)
            logging.error(traceback.format_exc())
