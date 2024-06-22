import time

import options
import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from base.base_class import Base
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.choose_supermarket_page import ChooseSupermarketPage
from pages.electronics_page import ElectronicsPage
from pages.main_page import MainPage



def test_buy_product():
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'  # Не ждет прогрузки страницы
    options.add_argument("--disable-notifications")
    g = Service('C:\\Users\\HUAWEI\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    #driver = webdriver.Chrome(options=options, service=g)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(driver)
    main_page.enter_supermarket() # Отрыть раздел 'Супермаркет'

    csp = ChooseSupermarketPage(driver)
    csp.enter_auchan() # Выбрать магазин 'Ашан'

    cp = CatalogPage(driver)
    cp.click_electronics() # Выбрать раздел 'Электроника'

    ep = ElectronicsPage(driver)
    ep.check_open_catalog_electronica() # Проверить, что произошел переход в раздел "Электроника"
    ep.choose_photo_video_cameras_filter() # Отфильтровать товар по "фото -видео камеры"
    ep.choose_click_range_slider_right_filter() # Отфильтровать по цене с помощью ползунка
    ep.choose_click_high_rating_filter() # Отфильтровать по "Высокий рейтинг"
    ep.choose_brand_smart_buy_filter() # Отфильтровать по бренду "SmartBuy"
    ep.choose_sort_cheaper() # Отфильтровать по "Сначала дешевле"
    ep.choose_product_1() # Добавить товар в корзину, проверить корректность добавление товара в корзину

    crtp = CartPage(driver)
    crtp.add_product_1()  # Увеличить количество товара до суммы доставки, перейти к оформлению заказа
    crtp.checkout()








