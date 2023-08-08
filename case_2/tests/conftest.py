import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from case_2.base_objects.inventory import InventoryPage
from case_2.base_objects.login_objects import LoginPage
from case_2.base_objects.shopping_cart import ShoppingCart


@pytest.fixture
def driver():
    base_driver = webdriver.Firefox()
    yield base_driver
    base_driver.quit()


@pytest.fixture()
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_credentials()
    login_page.click_login_button()
    return driver

@pytest.fixture
def inventory_page(login):
    return InventoryPage(login)


@pytest.fixture
def shopping_cart(login):
    login.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    return ShoppingCart(login)
