from selene import browser, be


class AuthPage:

    def __init__(self):
        self.header_menu = browser.element(".HeaderMenu-link--sign-in")
        self.sign_in_button = browser.element('//h1[.="Sign in to GitHub"]')
        self.sign_in_button_mobile = browser.element('.HeaderMenu-button.d-inline-flex')
        self.button_label = browser.element('.Button-label')

    def sign_in_desktop(self):
        browser.open('/')
        self.header_menu.click()
        self.sign_in_button.should(be.visible)

    def sign_in_mobile(self):
        browser.open('/')
        self.button_label.click()
        self.sign_in_button_mobile.click()
        self.sign_in_button.should(be.visible)


auth_page = AuthPage()

