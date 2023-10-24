import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
class TestMainPage1():

    def check_the_cart(self, browser):
        browser.get(link)
        button = browser.find_element(By.ID, "#add_to_basket_form")
        button.click()
        print("\nButton found, clicked")
        time.sleep(15)
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
        welcome_text = welcome_text_elt.text
        assert "Coders at Work был добавлен в вашу корзину." == welcome_text, "not passed"
        print("Subj was added to the cart succesfully")
