from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        if login_link:
            login_link.click()
        else:
            raise Exception("Login link not found on the page.")
