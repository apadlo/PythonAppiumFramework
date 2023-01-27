import pytest
import time
from base.DriverClass import Driver


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print('After Class')
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
