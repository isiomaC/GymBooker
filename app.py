# from GB.Locators.locators import MainPageLocators
from GB import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GB.PageObjects.LoginPage import LoginPage
from GB.PageObjects.BookingPage import BookingPage
from GB.PageObjects.Times.PreferredTime import PreferredTime

# //import pages

def main():
    driver = webdriver.Chrome()

    driver.get(config.url)

    driver.implicitly_wait(3)

    login = LoginPage(driver)
    login.fill_form_fields(config.email_address, config.password)
    login.click_go_button()

    booking = BookingPage(driver)
    booking.click_book_a_workout()

    booking.set_location("Liffey Valley")

    booking.set_date("Today")

    driver.implicitly_wait(5)

    booking.click_book(PreferredTime.TEST)

    driver.close() 
  
if __name__=="__main__":
    print("WAS MAIN")
    main()



# assert "No results found." not in driver.page_source
