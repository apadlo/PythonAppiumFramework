import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl
import time


class BasePage:

    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorValue))
            return element
        elif locatorType == "description":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator(f'UiSelector().description("{locatorValue}")'))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator(f'text("{locatorValue}")'))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath(f"{locatorValue}"))
            return element
        else:
            self.log.info(f"Locator value {locatorValue} not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info(
                f"Element found with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
        except:
            self.log.info(
                f"Element not found with LocatorType: {locatorType} and LocatorValue: {locatorValue}")

            return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                f"Clicked on element with LocatorType: '{locatorType}' and LocatorValue: '{locatorValue}'")
        except:
            self.log.info(
                f"Unable to click on element with LocatorType: '{locatorType}' and LocatorValue: '{locatorValue}'")
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                f"Sent text to element with LocatorType: '{locatorType}' and LocatorValue: '{locatorValue}'")
        except:
            self.log.info(
                f"Unable to send text to element with LocatorType: '{locatorType}' and LocatorValue: '{locatorValue}'")
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                f"Element with LocatorType: '{locatorType}' and LocatorValue: '{locatorValue}' is displayed")
            return True
        except:
            self.log.info(
                f"Element with LocatorType: '{locatorType}' and LocatorValue: '{locatorValue}' is not displayed")
            self.takeScreenshot(locatorType)
            return False


    def screenShot(self,screenshotName):
        fileName = f'{screenshotName}_{time.strftime("%Y%m%d-%H%M%S")}.png'
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info(f"Screenshot saved as '{fileName}'")
        except:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Failed to save screenshot")

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)


