from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    FILETER = (By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")
    ITEMS_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEMS_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    SOPPING_CART_VALUE = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")
    ADD_TO_CARD_BUTTON = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    MENU = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver):
        self.driver = driver

    def sorting_a_to_z(self):
        element = Select(self.driver.find_element(*self.FILETER))
        element.select_by_value("az")

    def sorting_z_to_a(self):
        element = Select(self.driver.find_element(*self.FILETER))
        element.select_by_value("za")

    def price_low_to_h(self):
        element = Select(self.driver.find_element(*self.FILETER))
        element.select_by_value("lohi")

    def price_hig_to_low(self):
        element = Select(self.driver.find_element(*self.FILETER))
        element.select_by_value("hilo")

    def get_items_manes(self):
        items = self.driver.find_elements(*self.ITEMS_NAMES)
        items_title = [t.text for t in items]
        return items_title

    def get_items_price(self):
        prices = self.driver.find_elements(*self.ITEMS_PRICES)
        price = [float(t.text.replace("$", "")) for t in prices]
        return price

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CARD_BUTTON).click()

    def shopping_cart_value(self):
        value = self.driver.find_element(*self.SOPPING_CART_VALUE).text
        return value

    def menu_button_click(self):
        self.driver.find_element(*self.MENU).click()
        value = self.driver.find_element(By.CLASS_NAME, "bm-menu-wrap").get_attribute("aria-hidden")
        return value

    def click_on_shopping_cart(self):
        self.driver.find_element(*self.SOPPING_CART).click()
