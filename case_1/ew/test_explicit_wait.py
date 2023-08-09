from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alert(driver):
    driver.find_element(By.ID, "alert").click()
    assert WebDriverWait(driver, 6).until(EC.alert_is_present())


def test_text_change(driver):
    driver.find_element(By.ID, "populate-text").click()
    WebDriverWait(driver, 11).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#h2"), "Selenium Webdriver"))
    result = driver.find_element(By.CLASS_NAME, "target-text").text
    assert result == "Selenium Webdriver"


def test_display_button(driver):
    driver.find_element(By.ID, "display-other-button").click()
    assert WebDriverWait(driver, 11).until(EC.element_to_be_clickable((By.ID, "hidden")))


def test_button(driver):
    driver.find_element(By.ID, "enable-button").click()
    assert WebDriverWait(driver, 11).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#disable")))


def test_checkbox(driver):
    driver.find_element(By.ID, "checkbox").click()
    assert WebDriverWait(driver, 11).until(EC.element_located_to_be_selected((By.ID, "ch")))
