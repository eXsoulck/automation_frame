import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    d = webdriver.Firefox()
    d.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    return d
