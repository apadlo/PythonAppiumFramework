import unittest
import pytest
from pages.LoginPage import LoginPageTest
from base.BasePage import BasePage
import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=5)
    def test_enterDataInEditBox(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()


    @pytest.mark.run(order=4)
    def test_openLoginScreen(self):
        self.bp.keyCode(4)  # Back
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLogin()
        self.gt.verifyAdminScreen()

    @pytest.mark.run(order=3)
    def test_loginFailMethod(self):
        cl.allureLogs("App launched")
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickOnLogin()
        self.gt.verifyAdminScreen()
