from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class UITests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def open_website(self):
        self.driver.get("https://www.inmotionhosting.com/")

    def test_ui_elements(self):  # Ensure this starts with 'test_'
        self.open_website()
        try:
            header = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.hero-title")))
            assert header.is_displayed(), "Header is not displayed."
            assert header.text == "Fast, Scalable Web Hosting and Server Solutions", "Header text is incorrect."
            assert header.value_of_css_property("font-size") == "32px", "Header font size is incorrect."

            print("Header UI test passed successfully!")

            button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.ppb-button.btn-primary")))
            assert button.is_displayed(), "Button is not displayed."
            assert button.text == "See Dedicated Servers", "Button text is incorrect."
            assert button.get_attribute("href") == "https://www.inmotionhosting.com/dedicated-servers", "Button link is incorrect."

            print("Button UI test passed successfully!")

        except AssertionError as e:
            print(f"UI test failed: {e}")

if __name__ == "__main__":
    unittest.main()
