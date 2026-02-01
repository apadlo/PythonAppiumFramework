# 🚀 Python Appium Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Appium](https://img.shields.io/badge/Appium-2.0-purple.svg)](https://appium.io/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-green.svg)](https://pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-red.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive, production-ready mobile test automation framework built with Python, Appium, and Pytest. This framework demonstrates best practices in mobile automation testing with support for both Android and iOS platforms, featuring Page Object Model (POM) design pattern, custom logging, and Allure reporting.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Test Execution](#-test-execution)
- [Reporting](#-reporting)
- [Framework Capabilities](#-framework-capabilities)
- [Contributing](#-contributing)

## ✨ Features

- **Cross-Platform Support**: Test automation for both Android and iOS applications
- **Page Object Model (POM)**: Clean, maintainable code structure with separation of concerns
- **Pytest Integration**: Leverage powerful pytest features including fixtures, markers, and parametrization
- **Custom Logging**: Built-in logging mechanism for better debugging and tracking
- **Allure Reports**: Beautiful, detailed test execution reports with screenshots
- **Reusable Components**: Base page with common methods for all page objects
- **Wait Strategies**: Intelligent wait mechanisms for stable test execution
- **Multiple Locator Support**: Support for ID, XPath, Text, Class Name, and more
- **Gesture Support**: Built-in methods for swipe, scroll, tap, drag and drop
- **Screenshot Capability**: Automatic screenshot capture on test failure
- **Real Device & Emulator Support**: Works with both emulators and physical devices

## 🏗 Architecture

This framework follows the **Page Object Model (POM)** design pattern, which provides:
- Better code reusability
- Easier maintenance
- Separation of test logic from page logic
- Improved readability

```
┌─────────────────┐
│   Test Cases    │  (tests/)
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Page Objects  │  (pages/)
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│   Base Page     │  (base/)
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Appium Driver  │
└─────────────────┘
```

## 🛠 Technology Stack

- **Python 3.8+** - Programming language
- **Appium** - Mobile automation framework
- **Selenium WebDriver** - Browser automation tool
- **Pytest** - Testing framework
- **Allure** - Test reporting framework
- **Android UIAutomator2** - Android automation driver
- **XCUITest** - iOS automation driver (for iOS testing)

## 📁 Project Structure

```
PythonAppiumFramework/
│
├── base/                          # Base classes for framework
│   ├── BasePage.py               # Base page with common methods
│   ├── DriverClass.py            # Appium driver initialization
│   └── __init__.py
│
├── pages/                         # Page Object Model classes
│   ├── LoginPage.py              # Login page objects and methods
│   ├── ContactUsFormPage.py      # Contact form page objects
│   └── __init__.py
│
├── tests/                         # Test cases
│   ├── conftest.py               # Pytest fixtures and setup
│   ├── LoginTest.py              # Login functionality tests
│   ├── ContactUsFormTest.py      # Contact form tests
│   ├── TestSuite.py              # Test suite configuration
│   └── __init__.py
│
├── utilities/                     # Utility functions
│   ├── CustomLogger.py           # Custom logging implementation
│   └── __init__.py
│
├── configurationfiles/            # Configuration files
│   └── __init__.py
│
├── reports/                       # Test execution reports
│   └── allurereports/            # Allure report data
│
├── screenshots/                   # Test execution screenshots
│
├── README.md                      # Project documentation
└── main.py                        # Entry point (optional)
```

## 📋 Prerequisites

Before running this framework, ensure you have the following installed:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **Node.js and npm** (for Appium)
   ```bash
   node --version
   npm --version
   ```

3. **Appium Server**
   ```bash
   npm install -g appium
   ```

4. **Appium Drivers**
   ```bash
   appium driver install uiautomator2    # For Android
   appium driver install xcuitest        # For iOS
   ```

5. **Java JDK** (for Android SDK)
   ```bash
   java --version
   ```

6. **Android SDK** (for Android testing)
   - Set `ANDROID_HOME` environment variable
   - Add platform-tools to PATH

7. **Xcode and Command Line Tools** (for iOS testing on macOS)
   ```bash
   xcode-select --install
   ```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/apadlo/PythonAppiumFramework.git
   cd PythonAppiumFramework
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install Appium-Python-Client
   pip install pytest
   pip install pytest-ordering
   pip install allure-pytest
   pip install selenium
   ```

4. **Install Allure Command Line** (for viewing reports)
   ```bash
   # On macOS
   brew install allure
   
   # On Windows (using Scoop)
   scoop install allure
   
   # On Linux
   # Download from https://github.com/allure-framework/allure2/releases
   ```

## ⚙ Configuration

1. **Update Device Configuration** in `base/DriverClass.py`:

   ```python
   desired_caps = {
       "platformName": "Android",
       "platformVersion": "12",          # Your device/emulator version
       "udid": "YOUR_DEVICE_UDID",      # Your device UDID
       "automationName": "UiAutomator2",
       "app": "path/to/your/app.apk",   # Path to your APK
       "appPackage": "com.your.app",    # Your app package
       "appActivity": "com.your.app.MainActivity"
   }
   ```

2. **Find Device UDID**:
   ```bash
   # For Android
   adb devices
   
   # For iOS
   idevice_id -l
   ```

3. **Start Appium Server**:
   ```bash
   appium --allow-cors
   ```

## 🎯 Usage

### Running Tests

1. **Run all tests**:
   ```bash
   pytest tests/
   ```

2. **Run specific test file**:
   ```bash
   pytest tests/LoginTest.py
   ```

3. **Run with test order**:
   ```bash
   pytest tests/ -v
   ```

4. **Run with Allure report generation**:
   ```bash
   pytest tests/ --alluredir=reports/allurereports
   ```

5. **Run specific test method**:
   ```bash
   pytest tests/LoginTest.py::LoginTest::test_openLoginScreen
   ```

## 📊 Test Execution

### Test Suite Execution

Execute the complete test suite:
```bash
pytest tests/TestSuite.py -v -s
```

### Parallel Execution

For faster execution, run tests in parallel:
```bash
pytest tests/ -n auto
```
*Note: Install pytest-xdist first: `pip install pytest-xdist`*

## 📈 Reporting

### Allure Reports

1. **Generate Allure report**:
   ```bash
   pytest tests/ --alluredir=reports/allurereports --clean-alluredir
   ```

2. **View Allure report**:
   ```bash
   allure serve reports/allurereports
   ```

The Allure report provides:
- ✅ Test execution overview and statistics
- 📊 Detailed test steps with screenshots
- 📝 Logs and stack traces for failures
- 📈 Trends and history of test execution
- 🏷 Test categorization and tagging

### Console Logs

Custom logging is implemented throughout the framework:
- Logs are saved in `reports/test.log`
- Console output shows real-time test execution
- Detailed step-by-step execution information

## 🎨 Framework Capabilities

### Appium & Mobile Testing
- ✅ Appium architecture and setup
- ✅ Appium Inspector integration
- ✅ Launch apps on Android and iOS (emulator & real devices)
- ✅ Support for hybrid app automation

### Locators
- ✅ ID locator
- ✅ Text locator
- ✅ Content description locator
- ✅ Index locator
- ✅ Class name locator
- ✅ XPath locator
- ✅ Multiple element finding (findElements)

### Wait Strategies
- ✅ Explicit waits with custom conditions
- ✅ Implicit waits configuration
- ✅ Fluent wait with polling frequency
- ✅ Wait for element visibility, clickability, etc.

### Device Methods
- ✅ Get current activity
- ✅ Get current context
- ✅ Check device orientation
- ✅ Check if device is locked
- ✅ Switch between contexts (Native/WebView)

### Actions & Interactions
- ✅ Android keycode actions (Back, Home, Enter, etc.)
- ✅ Element property checks (isDisplayed, isEnabled, isSelected)
- ✅ Element size and location retrieval
- ✅ Click actions
- ✅ Send text to elements
- ✅ Get text from elements
- ✅ Get content description

### Gestures
- ✅ Scroll actions
- ✅ Long click/tap
- ✅ Single and double tap
- ✅ Drag and drop
- ✅ Swipe gestures:
  - Left to Right
  - Right to Left
  - Top to Bottom
  - Bottom to Top

### Testing Features
- ✅ Pytest fixtures (setup/teardown)
- ✅ Test execution order control
- ✅ Conftest for shared fixtures
- ✅ Test method hierarchy
- ✅ Custom assertions and validations

### Logging & Reporting
- ✅ Python logging module integration
- ✅ Custom logger with different log levels
- ✅ Allure reporting with screenshots
- ✅ Step-by-step execution logs
- ✅ Automatic screenshot on failure

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For questions or feedback, please reach out through:
- GitHub Issues: [Create an issue](https://github.com/apadlo/PythonAppiumFramework/issues)
- GitHub Profile: [@apadlo](https://github.com/apadlo)

## 📝 License

This project is open source and available under the MIT License.

---

**⭐ If you find this framework helpful, please star the repository!**

*Built with ❤️ by apadlo*
