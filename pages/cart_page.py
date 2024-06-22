import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
from pages.electronics_page import ElectronicsPage




class CartPage(Base):



    def __init__(self, driver):
        self.driver = driver
        self.cart_url = "https://megamarket.ru/multicart/"
        super().__init__(driver)


# Locators

    add_product_button = "//button[@class='switch-button plus']"
    price_product_1 = "//div[@class='good__bottom']//span[@class='price']"
    total_price = "//span[@class ='cart-summary-redesign__total-price-value']"
    checkout_button = "//span[contains(text(), 'Оформить заказ')]"
    product_amount = "//div[@class='cart-summary-redesign__common-info-with-sub-title']"


 # Getters
    def get_add_product_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.add_product_button)))


    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_product_amount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_amount)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))



    # Actions

    """Метод для увеличения количества товаров в корзине"""
    def click_add_product_button(self, price_product_cart):
        total_price_float = float(self.get_total_price().text[:-2])
        price_product_float = float(price_product_cart.text[:-2])
        print(price_product_float)
        print(total_price_float)
        while total_price_float < 2000:
            self.get_add_product_button().click()
            total_price_float = total_price_float + price_product_float
            print(total_price_float)


    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Оформить заказ")


    def assert_product_amount(self):
        self.get_product_amount()
        print(self.get_product_amount().text)





# Methods

    def add_product_1(self):
        time.sleep(3)
        self.assert_url(self.cart_url)
        self.click_add_product_button(self.get_price_product_1())


    def checkout(self):
        time.sleep(5)
        self.assert_product_amount()
        self.click_checkout_button()
        time.sleep(3)
        self.get_screenshot()



