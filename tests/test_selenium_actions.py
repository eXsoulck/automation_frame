import time

import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.first_part
def test_checkboxes(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[6]/a").click()
    time.sleep(1)
    checkbox_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]")
    checkbox_1.click()
    time.sleep(1)
    checkbox_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[2]")
    checkbox_2.click()
    assert checkbox_1.get_attribute("checked")
    assert not checkbox_2.get_attribute("checked")

@pytest.mark.first_part
def test_context_menu(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[7]/a").click()
    spot = driver.find_element(By.ID, "hot-spot")
    action = ActionChains(driver)
    time.sleep(1)
    # context click the item
    action.context_click(on_element=spot)
    # perform the operation
    action.perform()
    driver.switch_to.alert.accept()
    time.sleep(2)
    try:
        driver.switch_to.alert
    except NoAlertPresentException as e:
        assert e



@pytest.mark.first_part
def test_dropdown_list(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[11]/a").click()
    elem = Select(driver.find_element(By.ID, "dropdown"))
    time.sleep(1)
    elem.select_by_value("2")
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div/div/select/option[3]").is_selected()



@pytest.mark.first_part
def test_entry_ad(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[15]/a").click()
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer > p:nth-child(1)")))
    driver.find_element(By.CSS_SELECTOR, ".modal-footer > p:nth-child(1)").click()
    driver.find_element(By.ID, "restart-ad").click()


@pytest.mark.first_part
def test_authentication(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[21]/a").click()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button").click()
    flash = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in flash


@pytest.mark.second_part
def test_frame(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[22]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[2]/a").click()
    driver.switch_to.frame(0)
    your_text = driver.find_element(By.XPATH, "//*[@id='tinymce']")
    your_text.click()
    your_text.clear()
    your_text.send_keys("Your text here !")

@pytest.mark.second_part
def test_horizontal_slider(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[24]/a").click()
    slider = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/input")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider, 75, 0).perform()
    action.send_keys(Keys.ARROW_LEFT * 3).perform()
    result = driver.find_element(By.XPATH, "//*[@id='range']").text
    assert result == "3"

@pytest.mark.second_part
def test_hover(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[25]/a").click()
    hover = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]")
    action = ActionChains(driver)
    time.sleep(1)
    action.move_to_element(hover).click(driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/a")).perform()
    time.sleep(2)
    site_text = driver.find_element(By.XPATH, "/html/body/h1").text
    assert site_text == "Not Found"

@pytest.mark.second_part
def test_input(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[27]/a").click()
    driver.find_element(By.CSS_SELECTOR, ".example > input:nth-child(2)").send_keys("23842")
    time.sleep(2)
    value = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/input").get_attribute("value")
    assert value == "23842"


@pytest.mark.second_part
def test_key_press(driver):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[31]/a").click()
    driver.find_element(By.ID, "target").send_keys(Keys.ARROW_LEFT)
    result = driver.find_element(By.ID, "result").text
    assert "LEFT" in result