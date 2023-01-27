from appium import webdriver


class Driver:

    def getDriverMethod(self):

        desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "udid": "R5CN60FN18E",
            "automationName": "UiAutomator2",
            "app": "D:\\Python\\Automation\\Android_Appium_Demo.apk",
            "appPackage": "com.skill2lead.appiumdemo",
            "appActivity": "com.skill2lead.appiumdemo.MainActivity",
            "uiautomator2ServerLaunchTimeout": "90000"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

"""
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "avd": "appium",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "app": "D:\\Python\\Automation\\Android_Appium_Demo.apk",
        "appPackage": "com.skill2lead.appiumdemo",
        "appActivity": "com.skill2lead.appiumdemo.MainActivity"
    }

    desired_caps = {
        "platformName": "Android",
        "platformVersion": "12",
        "udid": "R5CN60FN18E",
        "automationName": "UiAutomator2",
        "app": "D:\\Python\\Automation\\Android_Appium_Demo.apk",
        "appPackage": "com.skill2lead.appiumdemo",
        "appActivity": "com.skill2lead.appiumdemo.MainActivity"
    }

"""