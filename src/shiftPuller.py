from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getpass import getpass
import time
import datetime
import calendar

class shiftPuller:
    def __init__(self, username, password):
        self.username = username
        self.password = password
		
    def pullShifts(self):
        options = Options()
        options.headless = True
        client = webdriver.Chrome('C:\\Users\\Humza\\Desktop\\myTLC_client\\chromedriver.exe',
                            chrome_options=options)

        print("FETCHING_TLC: ")

        client.get('https://mytlc.bestbuy.com/')

        username = client.find_element_by_id("username")
        password = client.find_element_by_id("password")
        username.send_keys(self.username)
        password.send_keys(self.password)

        signOn = client.find_element_by_link_text("Sign On")
        signOn.click()

        print("RETRIEVING_SHIFTS: ")

        client.get('https://mytlc.bestbuy.com/mobility/app/Index.html#/schedule')

        time.sleep(2)

        shifts = client.find_elements_by_class_name("fc-content")
        dates = client.find_elements_by_class_name('fc-day-number')
        times = []

        x = 0
        for date in dates:
            if shifts[x].text == "Not scheduled":
                x += 1
                continue
            times.append(str(date.get_attribute('data-date')) + ' ' + str(shifts[x].text))
            x += 1
    
        return times