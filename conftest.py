import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720), (390, 844), (360, 740)],
                ids=['Full HD', 'HD', 'IPhone 12 Pro', 'Galaxy S8+'])
def setup_browser_management(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    driver_options.page_load_strategy = 'eager'

    if width >= 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(scope='function', params=[(430, 932), (390, 844), (360, 740)],
                ids=['IPhone 14 Pro Max', 'IPhone 12 Pro', 'Galaxy S8+'])
def setup_browser_mobile(request):
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    driver_options.page_load_strategy = 'eager'

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1080, 720), (1920, 1080), (2560, 1440)],
                ids=['HD', 'Full HD', 'QHD'])
def setup_browser_desktop(request):
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    driver_options.page_load_strategy = 'eager'

    yield

    browser.quit()
