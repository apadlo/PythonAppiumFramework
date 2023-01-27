import unittest
import pytest
from pages.ContactUsFormPage import ContactForm
import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self. cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("App launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
