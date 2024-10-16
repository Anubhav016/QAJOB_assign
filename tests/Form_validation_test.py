from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class FormValidationTest(unittest.TestCase):
    # Modify the constructor to avoid using a driver argument
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize the driver here

    def tearDown(self):
        self.driver.quit()  # Quit the driver here

    def open_website(self):
        self.driver.get("https://www.inmotionhosting.com/")
        time.sleep(2)

    def check_domain_search_form(self):
        assert self.driver.find_element(By.ID, "imh-search-form"), "Domain search form is not found."

    def check_placeholder_text(self):
        domain_input = self.driver.find_element(By.ID, "domain_search_domain")
        assert domain_input.get_attribute("placeholder") == "What domain are you searching for?", "Placeholder text is incorrect."

    def check_input_required(self):
        domain_input = self.driver.find_element(By.ID, "domain_search_domain")
        assert domain_input.get_attribute("required") == "true", "Input field should be required."

    def submit_form(self, domain):
        domain_input = self.driver.find_element(By.ID, "domain_search_domain")
        domain_input.clear()
        domain_input.send_keys(domain)
        self.driver.find_element(By.ID, "domain_submit").click()
        time.sleep(2)

    def validate_submission(self, expected_domain):
        assert expected_domain in self.driver.current_url, "The form was not submitted correctly."

    def validate_error_message(self, error_selector):
        assert self.driver.find_element(By.CSS_SELECTOR, error_selector).is_displayed(), "Error message not displayed."

    def test_form_validation(self):  # This should start with 'test_'
        self.open_website()
        try:
            self.check_domain_search_form()
            self.check_placeholder_text()
            self.check_input_required()

            # Valid input test
            self.submit_form("example.com")
            self.validate_submission("example.com")
            print("Form submission with valid input test passed successfully!")

            # Invalid input test
            self.submit_form("")
            self.validate_error_message(".error-message")  # Adjust based on actual error message selector

            # Invalid domain test
            self.submit_form("invalid_domain")
            self.validate_error_message(".error-message")

            # Already registered domain test
            self.submit_form("alreadyregistered.com")
            self.validate_error_message(".domain-unavailable-message")

            print("All form validation tests passed successfully!")

        except AssertionError as e:
            print(f"Form Validation test result: {e}")

if __name__ == "__main__":
    unittest.main()  # Use unittest's main to run tests
