import pytest
from pages.auth_page import auth_page


def test_sign_in_desktop(setup_browser_management):
    if setup_browser_management == 'mobile':
        pytest.skip(reason='Разрешение экрана - для мобильной версии, поэтому тест пропущен.')
    auth_page.sign_in_desktop()


def test_sign_in_mobile(setup_browser_management):
    if setup_browser_management == 'desktop':
        pytest.skip(reason='Разрешение экрана - для десктопной версии, поэтому тест пропущен.')
    auth_page.sign_in_mobile()


def test_github_desktop(setup_browser_desktop):
    auth_page.sign_in_desktop()


def test_github_mobile(setup_browser_mobile):
    auth_page.sign_in_mobile()
