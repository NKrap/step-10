from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_language_link(browser):
    browser.get(link)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    if 'fr' in curr_language:
        time.sleep(30)
    button1 = browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(button1) > 0, 'Не найдена кнопка добавления в корзину'
    assert len(button1) < 2, 'Кнопка добавления в корзину не уникальна'