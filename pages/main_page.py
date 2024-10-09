from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure



class MainPageA(Base):

    url = "https://megamarket.ru/"



# Locators


    catalog_a = "//div[contains(@class, 'header-catalog-menu__wrapper')]"
    supermarket_a = "//a[@href='/supermarket/']"

    catalog_b = "//div[@class='navigation-tabs__item navigation-tabs__item-catalog']"
    supermarket_b = "//div[@class='catalog-menu-redesign__wrapper menu-wrap']//a[@href='/supermarket/']"




# Getters



    def get_catalog_a(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_a)))

    def get_catalog_b(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_b)))


    def get_supermarket_a(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.supermarket_a)))

    def get_supermarket_b(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.supermarket_b)))

# Actions
    def click_catalog_button(self, get_catalog):
        get_catalog.click()
        print("Открыт каталог")

    def click_supermarket_button(self, get_supermarket):
        get_supermarket.click()
        print("Вход в раздел 'Супермаркет'")


# Methods

    """Вход в раздел 'Супермаркет'"""

    def enter_supermarket(self):
        with allure.step("Enter supermarket"):
            Logger.add_start_step(method='enter_supermarket')
            self.driver.get(self.url)
            self.driver.maximize_window()
            if Base.A_B_test(self, "//span[@class='trigger-text']", "Каталог", ) == "A":
                self.get_screenshot()
                self.click_catalog_button(self.get_catalog_a())
                self.click_supermarket_button(self.get_supermarket_a())
            # elif Base.A_B_test(self, "//p[@class='layout-onboarding__second-row']", "Теперь поиск внизу" ) == "B":
            #     self.get_screenshot()
            #     self.click_catalog_button(self.get_catalog_b())
            #     self.click_supermarket_button(self.get_supermarket_b())
            Logger.add_end_step(url=self.driver.current_url, method='enter_supermarket')







