import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure


class ChooseSupermarketPageA(Base):

    def __init__(self, driver):
        self.driver = driver
        self.address = "Москва, Авиамоторная улица, 12"
        super().__init__(driver)

# Locators

    auchan = "//div[@class='supermarket__content'][1]//span[contains(text(), 'АШАН - Купер')]"
    address_field = "//input[@placeholder='Город, улица, номер дома']"
    choose_address_list = "//a[@href='#']"
    confirm_address_button = "//button[@class='profile-address-create__search-btn btn sm']"
    supermarket_word = "//h1[contains(text(), 'Супермаркет')]"
    selected_delivery_address_a = "//span[@class='header-user-address-button__label']"

# Getters
    def get_auchan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.auchan)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_choose_address_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_address_list)))

    def get_confirm_address_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_address_button)))

    def get_supermarket_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.supermarket_word)))

    def get_selected_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_delivery_address_a)))

# Actions
    def click_auchan(self):
        self.get_auchan().click()
        print("Клик на супермаркет Ашан")

    def input_address_field(self, address):
        self.get_address_field().send_keys(address)
        print("Введен адрес доставки")

    def click_choose_address_list(self):
        self.get_choose_address_list().click()
        print("Выбран адрес доставки из выпадающего списка")

    def click_confirm_address_button(self):
        self.get_confirm_address_button().click()
        print("Адрес подтвержден")


# Methods

    """Выбрать супермаркет АШАН, ввести адрес доставки"""
    def enter_auchan(self):
        with allure.step("Enter auchan"):
            Logger.add_start_step(method='enter_auchan')
            self.get_current_url()
            time.sleep(5)
            self.assert_url("https://megamarket.ru/supermarket/")  # Проверка перехода в раздел "Супермаркет" по URL
            self.assert_word(self.get_supermarket_word(), "Супермаркет")  # Проверка перехода в раздел "Супермаркет" по названию раздела
            self.get_screenshot()
            self.click_auchan()
            time.sleep(3)
            self.input_address_field(self.address)
            self.get_screenshot()
            self.click_choose_address_list()
            self.click_confirm_address_button()
            self.assert_word(self.get_selected_delivery_address(), self.address)
            self.click_auchan()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='enter_auchan')





