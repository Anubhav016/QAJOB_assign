from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def open_website(self):
        self.driver.get("https://www.inmotionhosting.com/")

    def test_login_button(self):  # Ensure this starts with 'test_'
        self.open_website()
        try:
            login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-login")))
            assert login_button, "Login button is not found."
            assert login_button.get_attribute("title") == "AMP Login", "Login button title is incorrect."
            assert login_button.get_attribute("aria-label") == "Login", "Login button aria-label is incorrect."
            assert login_button.is_enabled(), "Login button should be enabled."

            self.driver.execute_script("arguments[0].scrollIntoView();", login_button)
            self.driver.execute_script("arguments[0].click();", login_button)

            self.wait.until(EC.url_contains("secure1.inmotionhosting.com"))
            assert "secure1.inmotionhosting.com" in self.driver.current_url, "Navigation to login page failed."

            print("Login button test passed successfully!")

        except AssertionError as e:
            print(f"Login button test failed: {e}")

if __name__ == "__main__":
    unittest.main()
