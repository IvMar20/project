from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.choose_supermarket_page import ChooseSupermarketPageA
from pages.electronics_page import ElectronicsPageA
from pages.main_page import MainPageA
import allure


@allure.description("Test buy product")
def test_buy_product():
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    options.add_argument("--disable-notifications")
    g = Service('C:\\Users\\HUAWEI\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    #service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=g)

    url = "https://megamarket.ru/"


    main_page = MainPageA(driver)
    main_page.enter_supermarket()  # Отрыть раздел 'Супермаркет'

    csp = ChooseSupermarketPageA(driver)
    csp.enter_auchan()  # Выбрать магазин 'Ашан'

    cp = CatalogPage(driver)
    cp.click_electronics()  # Выбрать раздел 'Электроника'

    ep = ElectronicsPageA(driver)
    ep.check_open_catalog_electronica()  # Проверить, что произошел переход в раздел "Электроника"
    ep.choose_photo_video_cameras_filter()  # Отфильтровать товар по "фото -видео камеры"
    ep.choose_click_range_slider_right_filter()  # Отфильтровать по цене с помощью ползунка
    ep.choose_click_high_rating_filter()  # Отфильтровать по "Высокий рейтинг"
    ep.choose_brand_smart_buy_filter()  # Отфильтровать по бренду "SmartBuy"
    ep.choose_sort_cheaper()  # Отфильтровать по "Сначала дешевле"
    ep.choose_product_1()  # Добавить товар в корзину, проверить корректность добавление товара в корзину

    crtp = CartPage(driver)
    crtp.add_product_1()  # Увеличить количество товара до суммы доставки, перейти к оформлению заказа
    crtp.checkout()










