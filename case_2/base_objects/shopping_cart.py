from selenium.webdriver.common.by import By


class ShoppingCart:
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CONTINUE_INSIDE_FORM = (By.ID, "continue")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CHECKOUT_FORM = (By.CLASS_NAME, "checkout_info")
    CART_ITEM1 = (By.CLASS_NAME, "cart_item")
    ADD_ITEM1 = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_ITEM2 = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    PRICE_TOTAL = (By.CSS_SELECTOR, "div.summary_info_label:nth-child(8)")
    FINISH_BUTTON = (By.ID, "finish")
    CHECKOUT_COMPLIT = (By.ID, "checkout_complete_container")

    def __init__(self, driver):
        self.driver = driver

    def click_on_remove(self):
        self.driver.find_element(*self.CART_ITEM1).find_element(By.TAG_NAME, "button").click()

    def click_on_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def click_on_continue_shopping(self, bt):
        self.driver.find_element(*bt).click()

    def fill_in_checkout_form(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys("Jeka")
        self.driver.find_element(*self.LAST_NAME).send_keys("Roberts")
        self.driver.find_element(*self.POSTAL_CODE).send_keys("18000")

    def add_two_items(self):
        self.driver.find_element(*self.ADD_ITEM1).click()
        self.driver.find_element(*self.ADD_ITEM2).click()

    def click_on_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def checkout_is_completed(self):
        return self.driver.find_element(*self.CHECKOUT_COMPLIT).is_displayed()
