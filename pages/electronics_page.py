import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base



class ElectronicsPage(Base):


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    price_value_electronics_1 = ''
    price_value_cart_1 = ''
    name_value_electronics_1 = ''
    name_value_cart_1 = ''


    # Locators

    open_category_filter = "//span[@class ='catalog-collections-selector-item__button-more-text']"
    photo_video_cameras_filter = "//span[contains(text(), 'Фото- и видеокамеры')]"
    range_slider_right_filter = "//button[@class='range-ctrl range-ctrl-right']"
    high_rating_filter = "//div[@class='filters-desktop__filter-item-wrapper solo'][3]//div[@class='pui-toggle-control']"
    brand_smartbuy_filter = "//span[@title='SmartBuy']"
    buy_button_product_1 = "//button[@data-test='buy-button']"
    sort_button = "//div[@class='input text-input size']"
    sort_choose_cheaper = "//li[contains(text(), 'Сначала дешевле')]"
    cart = "//div[@class='mini-cart__info']"
    catalog_name_electronica = "//span[@class='catalog-header__category-name']"
    selected_price_checkbox = "//span[contains(text(), 'Цена') and @class='checkbox-text']"
    selected_brand_checkbox = "//span[contains(text(), 'Бренд') and @class='checkbox-text']"
    selected_high_rating_checkbox = "//span[contains(text(), 'Высокий рейтинг') and @class='checkbox-text']"
    option_current = "//li[@class = 'option current']"
    goods_count_cart_icon = "//span[@class = 'goods-count']"  # Отображение количества товара в корзине
    show_more_brand = "//div[ @class ='filter__show-more']" # Развернуть фильтр по Бренду
    price_product_electronics_1 = "//div[@id='600004955630']//div[@data-test='product-price']"
    price_product_cart_1 = "//span[@class='price']"
    name_product_electronics_1 = "//a[@title = 'Карта памяти MicroSD 16GB Smart Buy Class 10 +SD адаптер']"
    name_product_cart_1 = "//span[@class = 'title']"


    # Getters
    def get_open_category_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_category_filter)))

    def get_photo_video_cameras_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.photo_video_cameras_filter)))

    def get_range_slider_right_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.range_slider_right_filter)))

    def get_high_rating_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.high_rating_filter)))

    def get_brand_smartbuy_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_smartbuy_filter)))

    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_button)))

    def get_sort_choose_cheaper(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_choose_cheaper)))

    def get_buy_button_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_catalog_name_electronica(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_name_electronica)))

    def get_selected_price_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_price_checkbox)))

    def get_selected_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_brand_checkbox)))

    def get_selected_high_rating_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_high_rating_checkbox)))

    def get_option_current(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.option_current)))

    def get_goods_count_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.goods_count_cart_icon)))

    def get_show_more_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_more_brand)))

    def get_price_product_electronics_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_electronics_1)))

    def get_price_product_cart_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_cart_1)))

    def get_name_product_electronics_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_electronics_1)))

    def get_name_product_cart_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_cart_1)))

    # Actions
    def click_open_category_filter(self):
        self.get_open_category_filter().click()
        print("Раскрыт фильтр по категориям")

    def click_photo_video_cameras_filter(self):
        self.get_photo_video_cameras_filter().click()
        print("Выбрана категория 'Фото- и видеокамеры'")

    def click_range_slider_right_filter(self, x, y):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_range_slider_right_filter()).move_by_offset(x, y).release().perform()
        print("Ползунок цены передвинут влево")

    def click_high_rating_filter(self):
        self.get_high_rating_filter().click()
        print("Выбран фильтр 'Высокий рейтинг'")

    def click_brand_smartbuy_filter(self):
        self.get_brand_smartbuy_filter().click()
        print("Выбран бренд 'Kodak'")

    def click_sort_button(self):
        self.get_sort_button().click()
        print("Открыт фильтр сортировки товара")

    def click_buy_button(self, buy_button):
        buy_button.click()
        print("Товар добавлен в корзину")

    def click_sort_choose_cheaper(self):
        self.get_sort_choose_cheaper().click()
        print("Товары отсортированы по 'Сначала дешевле'")

    def click_cart(self):
        self.get_cart().click()
        print("Вход в корзину")

    def click_show_more_brand(self):
        self.get_show_more_brand().click()
        print("Раскрыт фильтр по бренду 'Показать больше'")


    """Сохранение цены товара в каталоге"""
    def save_price_electronics(self):
        global price_value_electronics_1
        price_electronics = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_electronics_1)))
        price_value_electronics_1 = price_electronics.text
        print(price_value_electronics_1)
        return price_value_electronics_1


    "Сохранение цены товара в корзине"
    def save_price_cart(self):
        global price_value_cart_1
        price_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_cart_1)))
        price_value_cart_1 = price_cart.text
        print(price_value_cart_1)
        return price_value_cart_1

    """Сохранение наименования товара в каталоге"""
    def save_name_electronics(self):
        global name_value_electronics_1
        name_electronics = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_electronics_1)))
        name_value_electronics_1 = name_electronics.text
        print(name_value_electronics_1)
        return name_value_electronics_1

    """Сохранение наименования товара в каталоге"""

    def save_name_cart(self):
        global name_value_cart_1
        name_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_cart_1)))
        name_value_cart_1 = name_cart.text
        print(name_value_cart_1)
        return name_value_cart_1




# Methods

    """Метод проверки нахождения в разделе 'Электроника'"""
    def check_open_catalog_electronica(self):
        time.sleep(3)
        self.get_screenshot()
        self.get_current_url()
        time.sleep(3)
        self.assert_url("https://megamarket.ru/catalog/cnc/#?cat=X12011&store=270618")
        self.assert_word(self.get_catalog_name_electronica(), 'Электроника')

    """Метод выбора фильтра по фото -видео камерами"""
    def choose_photo_video_cameras_filter(self):
        self.click_open_category_filter()
        time.sleep(3)
        self.click_photo_video_cameras_filter()
        time.sleep(5)
        self.assert_url("https://megamarket.ru/catalog/cnc/#?cat=X12020&store=270618")

    """Метод для выбора диапазона цены с помощью ползунка"""
    def choose_click_range_slider_right_filter(self):
        self.click_range_slider_right_filter(-100, 0)
        self.assert_selected_filter(self.get_selected_price_checkbox(), "Цена")

    """Метод для фильтрации по 'Высокий рейтинг'"""
    def choose_click_high_rating_filter(self):
        self.click_high_rating_filter()
        self.assert_selected_filter(self.get_selected_high_rating_checkbox(), "Высокий рейтинг")
        time.sleep(3)


    """Метод для фильтрации по бренду 'Кодак'"""
    def choose_brand_smart_buy_filter(self):
        self.click_show_more_brand()
        time.sleep(3)
        self.click_brand_smartbuy_filter()
        self.assert_selected_filter(self.get_selected_brand_checkbox(), "Бренд: SmartBuy")
        time.sleep(3)


    """Метод для сортировки по 'Сначала дешевле'"""
    def choose_sort_cheaper(self):
        self.click_sort_button()
        self.click_sort_choose_cheaper()
        time.sleep(3)
        self.assert_current_option(self.click_sort_button(), self.get_option_current(), "Сначала дешевле")


    """Метод добавления товара в корзину, проверки количества товара в корзине, цены в товара в каталоге и корзине"""
    def choose_product_1(self):
        time.sleep(5)
        self.get_screenshot()
        self.click_buy_button(self.get_buy_button_product_1())
        self.assert_goods_count(self.get_goods_count_cart_icon(), "1")
        self.save_price_electronics()
        self.save_name_electronics()
        self.click_cart()
        self.save_price_cart()
        self.save_name_cart()
        self.assert_price(price_value_electronics_1, price_value_cart_1)
        self.assert_name(name_value_electronics_1, name_value_cart_1)
        self.get_screenshot()









