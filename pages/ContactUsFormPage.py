from base.BasePage import BasePage
import utilities.CustomLogger as cl


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _contactFormButton = "com.skill2lead.appiumdemo:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFormButton, "id")
        cl.allureLogs("Clicked on Contact Us Form Button")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
        cl.allureLogs("Contact us Form page opened")

    def enterName(self):
        self.sendText("Code2Lead",self._enterName,"text")
        cl.allureLogs("Entered name")

    def enterEmail(self):
        self.sendText("abc@gmail.com",self._enterEmail,"text")
        cl.allureLogs("Entered email")

    def enterAddress(self):
        self.sendText("India",self._enterAddress,"text")
        cl.allureLogs("Entered address")

    def enterNumber(self):
        self.sendText("987654210",self._enterMobileNumber,"index")
        cl.allureLogs("Entered mobile number")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Clicked on submit button")
