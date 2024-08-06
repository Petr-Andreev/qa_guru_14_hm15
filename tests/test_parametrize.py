import pytest
from pages.auth_page import auth_page

desktop_only = pytest.mark.parametrize("setup_browser_management",
                                       [(1080, 720), (1920, 1080), (2560, 1440)],
                                       indirect=True,
                                       ids=['HD', 'Full HD', 'QHD'])
mobile_only = pytest.mark.parametrize("setup_browser_management",
                                      [(430, 932), (390, 844), (360, 740)],
                                      indirect=True,
                                      ids=['IPhone 14 Pro Max', 'IPhone 12 Pro', 'Galaxy S8+'])


@desktop_only
def test_github_desktop(setup_browser_management):
    auth_page.sign_in_desktop()


@mobile_only
def test_github_mobile(setup_browser_management):
    auth_page.sign_in_mobile()
