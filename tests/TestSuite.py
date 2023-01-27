# 1. Import the files
import unittest
from tests.LoginTest import LoginTest
from tests.ContactUsFormTest import ContactFormTest


# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf,gt])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)