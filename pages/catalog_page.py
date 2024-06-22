from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


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
        self.get_current_url()
        self.assert_url("https://megamarket.ru/catalog/cnc/#?store=270618")
        self.get_screenshot()
        self.click_electronics()
