from case_2.base_objects.login_objects import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_credentials()
    login_page.click_login_button()
    home_page = driver.current_url

    assert home_page in "https://www.saucedemo.com/inventory.html"

