import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("https://my.zanichelli.it/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Bottone "Entra" è inesistente")
    finally: 
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("https://my.zanichelli.it/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Bottone "Entra" è inesistente")
    finally: 
        browser.quit()