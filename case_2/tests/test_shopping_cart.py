import time

from ..base_objects.inventory import InventoryPage
from ..base_objects.shopping_cart import ShoppingCart


def test_item_in_cart(login):
    inv = InventoryPage(login)
    inv.add_to_cart()
    inv.click_on_shopping_cart()
    time.sleep(2)
    assert inv.driver.find_element(*inv.SOPPING_CART).is_displayed()


def test_continue_button(shopping_cart):
    shopping_cart.click_on_continue_shopping()
    assert shopping_cart.driver.current_url in "https://www.saucedemo.com/inventory.html"


def test_checkout_button(shopping_cart):
    shopping_cart.click_on_checkout()
    shopping_cart.driver.find_element(*shopping_cart.CHECKOUT_FORM).is_displayed()
    shopping_cart.fill_in_checkout_form()
    time.sleep(1)
    a = shopping_cart.driver.find_element(*shopping_cart.FIRST_NAME).get_attribute("value")
    b = shopping_cart.driver.find_element(*shopping_cart.LAST_NAME).get_attribute("value")
    c = shopping_cart.driver.find_element(*shopping_cart.POSTAL_CODE).get_attribute("value")
    assert (a, b, c) == ("Jeka", "Roberts", "18000")


def test_total_calculation(login):
    shopping_cart = ShoppingCart(login)
    shopping_cart.add_two_items()
    inventory = InventoryPage(shopping_cart.driver)
    inventory.click_on_shopping_cart()
    shopping_cart.click_on_checkout()
    shopping_cart.fill_in_checkout_form()
    shopping_cart.click_on_continue_shopping(shopping_cart.CONTINUE_INSIDE_FORM)
    total = shopping_cart.driver.find_element(*shopping_cart.PRICE_TOTAL).text
    assert "$25.90" in total


def test_checkout_complete(login):
    shopping_cart = ShoppingCart(login)
    shopping_cart.add_two_items()
    inventory = InventoryPage(shopping_cart.driver)
    inventory.click_on_shopping_cart()
    shopping_cart.click_on_checkout()
    shopping_cart.fill_in_checkout_form()
    shopping_cart.click_on_continue_shopping(shopping_cart.CONTINUE_INSIDE_FORM)
    shopping_cart.click_on_finish()
    time.sleep(2)
    assert shopping_cart.checkout_is_completed()
