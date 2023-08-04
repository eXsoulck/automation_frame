import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def base_driver():
    base_driver = webdriver.Firefox()
    yield base_driver
    base_driver.quit()

@pytest.fixture
def driver(base_driver):
    base_driver.get("http://the-internet.herokuapp.com")
    return base_driver
