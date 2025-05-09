# Ticket.py

import time
import json
import html
import logging
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


WEBSITE_URL = "https://kktix.com/"
TARGET_EVENT_NAME = "some_sample_event"
TARGET_EVENT_CATEGORY = "Entertainment"
TARGET_TICKET_PRICES = ["800", "3,200"]
TARGET_TICKET_TYPE = "B1"
TARGET_BUY_PRICE = "800"
TARGET_TICKET_QTY = "2"
PAGE_REFRESH_INTERVAL_SECOND = 1
TICKET_SEARCH_WAITING_TIME_SECOND = 900
WEBSITE_USERNAME = "your_username_here"
WEBSITE_PASSWORD = "your_password_here"
CHROME_DRIVER_PATH = "chromedriver.exe"


logger = logging.getLogger()
fileHandler = logging.FileHandler("logfile.log")
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

logger.setLevel("INFO")


class TicketBot:
    _slot_ = ['driver']
    def _init_(self, driver):
        self.driver = driver

    def search_event(self):
        logger.info("Searhing event {} ...".format(TARGET_EVENT_NAME))
        category_page = self.driver.find_element(By.LINK_TEXT, TARGET_EVENT_CATEGORY)
        category_page.click()

        search_tex_field = self.driver.find_element(By.ID, "search_form_search")

        search_tex_field.send_keys(TARGET_EVENT_NAME)
        search_tex_field.send_keys(Keys.RETURN)

    def navigate_to_event(self):
        try:
            search_result = self.driver.find_element(
                By.XPATH, '//div[@data-react-class="SearchWrapper"]'
            )
            
            events = json.loads(search_result.get_attribute("data-react-props"))["data"]

            if events is not None:
                for event in events:
                    event_name = html.unescape(event["name"]).strip()
                    logger.info("Found target event {} !".format(event_name))
                    if TARGET_EVENT_NAME == event_name:
                        event_page = self.driver.find_element(
                            By.XPATH, '//a[@href="{}"]'.format(event["public_url"])
                        )
                        event_page.click()

                        next_step = self.driver.find_element(By.LINK_TEXT, "Next Step")
                        next_step.click()
            else:
                logger.error("Event name might be incorrect.")
        except:
            raise Exception("Event not found!")


    def signing_in(self):
        sign_in = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Sign In"))
        )
        sign_in.click()

        insert_username = WebDriverWait(self.driver, 1).until(
            ec.presence_of_element_located((By.XPATH, "//input[@id='user_login']"))
        )
        insert_username.send_keys(WEBSITE_USERNAME)

        insert_password = self.driver.find_element(
            By.XPATH, "//input[@id='user_password']"
        )
        insert_password.send_keys(WEBSITE_PASSWORD)

        submit_login = self.driver.find_element(By.XPATH, "//input[@value='Sign In']")
        submit_login.click()

    # def buy_ticket_in_multiple_prices(self):
    #     ticket_table = self.driver.find_element(By.CLASS_NAME ,"display-table")
    #     ticket_list = []
    #     for i in ticket_table:
    #         ticket_list.append(i.get_attribute("id"))

    #     for price in TARGET_TICKET_PRICES:
    #         print("Start buying {}".format(price))
    #         for x in ticket_list:
    #             print("Checking ticket type of {}".format(x))
    #             try:
    #                 ticket_price = self.driver.find_element_by_xpath(
    #                     "//div[@id='{}']//span[contains(@class,'ticket-price')]//span[contains(@class,'ng-binding ng-scope')
