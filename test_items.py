import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
class TestMainPage1():

    def test_check_the_cart(self, browser):
        browser.get(link)
        print("Got link")
        time.sleep(30)
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form")
        welcome_text = welcome_text_elt.text
        assert "Ajouter au panier" == welcome_text, "not passed"
        print("Button looks good")
