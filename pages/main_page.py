from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):

    url = "https://megamarket.ru/"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


# Locators
    catalog = "//div[contains(@class, 'header-catalog-menu__wrapper')]"
    supermarket = "//a[@href='/supermarket/']"

# Getters
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_supermarket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.supermarket)))

# Actions
    def click_catalog_button(self):
        self.get_catalog().click()
        print("Открыт каталог")

    def click_supermarket_button(self):
        self.get_supermarket().click()
        print("Вход в раздел 'Супермаркет'")


# Methods

    """Вход в раздел 'Супермаркет'"""
    def enter_supermarket(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_screenshot()
        self.click_catalog_button()
        self.click_supermarket_button()











