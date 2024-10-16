# run_tests.py
import unittest
from HtmlTestRunner import HTMLTestRunner

# Import your test classes
from Form_validation_test import FormValidationTest
from Functional_tests import FunctionalTests
from Login_tests import LoginTests
from UI_test import UITests

# Create a test suite
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(FormValidationTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(FunctionalTests))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTests))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UITests))

# Define the report file
with open("test_report.html", "w") as report_file:  # Change "wb" to "w"

    # Create the test runner
    runner = HTMLTestRunner(stream=report_file)

    # Run the tests
    runner.run(suite)

# The report file is automatically closed after the with block
