from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure


class CatalogPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators
    electronics = "//h3[contains(text(), 'Электроника')]"

    # Getters
    def get_electronics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.electronics)))

    # Actions
    def click_electronics(self):
        self.get_electronics().click()
        print("Выбран раздел 'Электроника'")

    # Methods
    """Вход в каталог 'Электроника'"""
    def choose_catalog(self):
        with allure.step("Choose catalog"):
            Logger.add_start_step(method='choose_catalog')
            self.get_current_url()
            self.assert_url("https://megamarket.ru/catalog/cnc/#?store=270618")
            self.click_electronics()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='choose_catalog')
