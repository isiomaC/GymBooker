# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from GB.PageObjects.LoginPage import LoginPage
# from GB.PageObjects.BookingPage import BookingPage

# # //import pages

# def main():
#     driver = webdriver.Chrome()
#     driver.get("http://www.flyefit.ie")

#     driver.get("https://myflye.flyefit.ie/login")

#     driver.implicitly_wait(3)

#     loginp = LoginPage(driver)
#     loginp.fill_form_fields("isioma.chuck@gmail.com", "Pass_Flye99")
#     loginp.click_go_button()

#     bookingp = BookingPage(driver)
#     bookingp.click_book_a_workout()

#     bookingp.set_location("Tallaght")
#     bookingp.set_date("Tomorrow")

#     driver.close()
  
# if __name__=="__main__":
#     main()



# # assert "No results found." not in driver.page_source
