from base.BasePage import BasePage
import utilities.CustomLogger as cl


class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _loginbutton = "com.skill2lead.appiumdemo:id/Login"  # id
    _enterEmail = "com.skill2lead.appiumdemo:id/Et4"  # id
    _enterPassword = "com.skill2lead.appiumdemo:id/Et5"   # id
    _clickloginButton = "com.skill2lead.appiumdemo:id/Btn3"  # id
    _wrongCredentials = "Wrong Credentials"  # text
    _pageTitle = "Enter Admin"  # text
    _enterText = "com.skill2lead.appiumdemo:id/Edt_admin"  # id
    _submitButton = "com.skill2lead.appiumdemo:id/Btn_admin_sub"  # id

    def clickLoginButton(self):
        self.clickElement(self._loginbutton, "id")
        cl.allureLogs("Click on Login Button")

    def enterEmail(self):
        self.sendText("admin@gmail.com", self._enterEmail, "id")
        cl.allureLogs("Entered email")

    def enterPassword(self):
        self.sendText("admin123", self._enterPassword, "id")
        cl.allureLogs("Entered password")

    def enterPassword2(self):
        self.sendText("wrongpw", self._enterPassword, "id")
        cl.allureLogs("Entered password")

    def clickOnLogin(self):
        self.clickElement(self._clickloginButton, "id")
        cl.allureLogs("Clicked login button")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle, "text")
        assert adminScreen
        cl.allureLogs("Opened admin screen")

    def enterText(self):
        self.sendText("Code2Lead", self._enterText, "id")
        cl.allureLogs("Entered text")

    def clickOnSubmit(self):
        self.clickElement(self._submitButton, "id")
        cl.allureLogs("Clicked on Submit button")
