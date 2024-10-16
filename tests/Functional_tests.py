from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def open_website(self):
        self.driver.get("https://www.inmotionhosting.com/")
        time.sleep(2)

    def test_domain_search_form(self):  # Ensure this starts with 'test_'
        self.open_website()
        try:
            assert self.driver.find_element(By.ID, "imh-search-form"), "Domain search form is not found."
            domain_input = self.driver.find_element(By.ID, "domain_search_domain")
            assert domain_input.get_attribute("placeholder") == "What domain are you searching for?", "Placeholder text is incorrect."
            assert domain_input.get_attribute("required") == "true", "Input field should be required."

            self.submit_form("example.com")
            assert "example.com" in self.driver.current_url, "The form was not submitted correctly."

            self.submit_form("")
            self.validate_error_message(".error-message")  # Adjust based on actual error message selector

            self.submit_form("invalid_domain")
            self.validate_error_message(".error-message")

            self.submit_form("alreadyregistered.com")
            self.validate_error_message(".domain-unavailable-message")

            print("Domain search form tests passed successfully!")

        except AssertionError as e:
            print(f"Domain search form test: {e}")

    def test_chat_button(self):  # Ensure this starts with 'test_'
        self.open_website()
        try:
            chat_button = self.driver.find_element(By.CSS_SELECTOR, ".chat-btn-popup")
            assert chat_button, "Chat button is not found."
            assert chat_button.get_attribute("aria-label") == "Chat with us 1", "Chat button aria-label is incorrect."
            assert chat_button.is_enabled(), "Chat button should be enabled."

            chat_button.click()
            time.sleep(2)
            assert self.driver.find_element(By.CSS_SELECTOR, ".chat-popup").is_displayed(), "Chat popup did not appear after clicking the button."

            print("Chat functionality test passed successfully!")

        except AssertionError as e:
            print(f"Chat functionality test: {e}")

    def submit_form(self, domain):
        domain_input = self.driver.find_element(By.ID, "domain_search_domain")
        domain_input.clear()
        domain_input.send_keys(domain)
        self.driver.find_element(By.ID, "domain_submit").click()
        time.sleep(2)

    def validate_error_message(self, error_selector):
        assert self.driver.find_element(By.CSS_SELECTOR, error_selector).is_displayed(), "Error message not displayed."

if __name__ == "__main__":
    unittest.main()
