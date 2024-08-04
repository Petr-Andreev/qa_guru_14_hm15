import pytest
from selene import browser
from pages.auth_page import auth_page


def test_sign_in(setup_browser):
    auth_page.sign_in_desktop()


def test_sign_in_desktop(setup_browser):
    if setup_browser == 'mobile':
        pytest.skip(reason='Разрешение экрана - для мобильной версии, поэтому тест пропущен.')
    auth_page.sign_in_desktop()


def test_sign_in_mobile(setup_browser):
    if setup_browser == 'desktop':
        pytest.skip(reason='Разрешение экрана - для десктопной версии, поэтому тест пропущен.')
    auth_page.sign_in_mobile()


@pytest.mark.parametrize("setup_browser", [(1920, 1080), (430, 932)], indirect=True)
def test_sign_in_indirect(setup_browser):
    browser.open('/')
    if setup_browser == 'desktop':
        auth_page.sign_in_desktop()
    else:
        auth_page.sign_in_mobile()


def test_github_desktop(setup_browser_desktop):
    auth_page.sign_in_desktop()


def test_github_mobile2(setup_browser_mobile):
    auth_page.sign_in_mobile()
