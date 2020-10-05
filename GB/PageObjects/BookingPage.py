from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .Locators.locators import MainPageLocators
from .Times import PreferredTime

import traceback
import logging
import time

class BookingPage(BasePage):
    """Search results page action methods come here"""

    # def __init__(self):
    #     self.availablebookings = []
    #     self.bookedtimes = []
    #     self.bookingChoice = ''

    availablebookings = []
    bookedtimes = []
    bookingChoice = ''

    def click_book_a_workout(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, MainPageLocators.BOOK_WORKOUT[1])))
            element.click()
        
        except Exception as e:
            print("Book a workout failed", e.with_traceback)
            logging.error(traceback.format_exc())

    def set_location(self, location):
        try:
            # // index 1, second dropdown for location
            self.click_dropdown(1, location)

        except Exception as e:
            print("Book a workout failed", e.with_traceback)
            logging.error(traceback.format_exc())


    def set_date(self, date):
        try:
            # //index 2, the date dropdown
            self.click_dropdown(2, date)
        
        except Exception as e:
            print("Error setting date", e.with_traceback)
            logging.error(traceback.format_exc())


    def click_book(self, daterange):
        try:
            section = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, MainPageLocators.SECTION_DIV[1])))

            bookings = section.find_elements(*MainPageLocators.BOOKING_DIVS)

            count = len(bookings)

            DisabledBookings = 0
            ActiveBookings = 0

            print(bookings[0].get_attribute('innerHTML'))

            for idx, item in enumerate(bookings):
                
                bookDate = item.find_element(By.TAG_NAME, "h2")

                bookBtn = item.find_element(*MainPageLocators.BLOCK_ACTION)

                cleanBtnText = bookBtn.text.replace("#", "").strip()
                # print(bookBtn.get_attribute('innerHTML'))
                # print(bookBtn.text.replace("#", "").strip())

                if cleanBtnText == "Not Yet Open" :
                    print("In not open block")
                    if idx == count - 1:
                        # End of file, no bookings found
                        print("Not Yet Open, END")
                
                elif cleanBtnText == "Fully Booked" :
                    print("Fully booked")

                    DisabledBookings += 1
                    self.bookedtimes.append(bookDate.text)
                    if idx == count - 1:
                        # End of file, no bookings found
                        print("Fully Booked, try again later, END")

                    continue
                elif cleanBtnText == "Book":
                    print(bookDate.text+" == "+ daterange.value)
                    ActiveBookings += 1
                    if bookDate.text == daterange.value :
                        print("found match")
                        bookBtn.click()
                        self.bookingChoice = bookDate.text
                        time.sleep(10)
                        break

                    else :
                        # Found available time not wanted, wanted pass as suggestion, store in list for transfer
                        self.availablebookings.append(bookDate.text)
                        

            print('\n')
            print("Available booking",len(self.availablebookings))


            print('\n')
            print("booked times",len(self.bookedtimes))
            print('\n')
                
        except Exception as e:
            print("Error in click book", e.with_traceback)
            logging.error(traceback.format_exc())


    def is_booking_found(self):
        # logic to check if booking was found
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    
    



    # Helper functions
    def click_dropdown(self, index, value):

        parentDiv = self.wait.until(EC.visibility_of_element_located((By.XPATH, MainPageLocators.PARENTDIV[1])))

        childrenDiv = parentDiv.find_elements(*MainPageLocators.CHILDRENDIV) 

        childrenDiv[index].click()

        # ul = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, MainPageLocators.SELECTRIC_SCROLL_UL[1])))
        ul = childrenDiv[index].find_element(*MainPageLocators.SELECTRIC_SCROLL_UL)

        self.driver.implicitly_wait(3)

        liS = ul.find_elements(*MainPageLocators.LOCATIONS_LI)

        for idx, item in enumerate(liS) :
            print(idx)
            if item.text == value :
                print (item.text + " == " + value)
                item.click()
                break