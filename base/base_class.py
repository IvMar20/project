import datetime

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver
        # super().__init__(driver)



    """Метод для проверки текущей url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий url: {get_url}')

    """Метод для проверки текста"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Значение текста корректно: {value_word}")

    """Метод для проверки URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("URL корректен")

    """Метод для проверки активности фильтра"""
    def assert_selected_filter(self, selected_checkbox, result):
        assert selected_checkbox.text == result
        print(f"Фильтр '{result}' активен")


    """Метод для проверки сортировки"""
    def assert_current_option(self, click_sort_button, option_current, word):
        try:
            click_sort_button()
        except TypeError:
            assert option_current.text == word
            print(f"Товары корректно отсортированы по {word}")


    """Метод для проверки количества товаров в корзине из формы каталога товаров"""
    def assert_goods_count(self, goods_count, amount):
        assert goods_count.text == amount
        print(f"Отображение количества товара в корзине корректно: {amount}")



    """Метод для проверки корректности цены товара в корзине"""
    def assert_price(self, price_before_cart, price_cart):
        assert price_before_cart == price_cart
        print(f"Цены в каталоге и корзине совпадают: цена в каталоге {price_before_cart}, цена в корзине {price_cart}")

    """Метод для проверки корректности наименования товара в корзине"""
    def assert_name(self, name_before_cart, name_cart):
        assert name_before_cart == name_cart
        print(f"Наименования в каталоге и корзине совпадают: наименование в каталоге {name_before_cart}, наименование в корзине {name_cart}")



    """Метод для сохранения скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot = "screenshot " + str(now_date) + '.png'
        self.driver.save_screenshot("C:\\Users\\HUAWEI\\PycharmProjects\\mailProject\\pytest_megamarket\\screen\\" + screenshot)
        print(f"Скрин {screenshot}")








