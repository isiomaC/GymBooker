from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    EMAIL = (By.ID, 'email_address')
    PASSWORD = (By.ID, 'password') 
    LOGIN_BUTTON = (By.NAME, 'log_in')
    BOOK_WORKOUT = (By.XPATH, "//a[@href='/myflye/book-workout']")
    PARENTDIV = (By.XPATH, "//div[@class='form__inner']")
    CHILDRENDIV = (By.XPATH, "//div[@class='form-group']")
    SELECTRIC_SCROLL_UL = (By.TAG_NAME, "ul")
    LOCATIONS_LI = (By.TAG_NAME, "li")
    SECTION_DIV = (By.CLASS_NAME, "section__body")
    BOOKING_DIVS = (By.CSS_SELECTOR, "div[class$='js-content-parent']")
    BLOCK_ACTION = (By.CLASS_NAME, "block__actions")

