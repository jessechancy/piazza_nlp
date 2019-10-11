import selenium
from selenium import webdriver
import time
from time import sleep
import csv

USERNAME = "jessec1@andrew.cmu.edu"
PASSWORD = ""

## Authentication

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path = './chromedriver', 
                           options = chrome_options)
browser.get('https://piazza.com/')

log_in = browser.find_element_by_xpath('//*[@id="login_button"]')
log_in.click()
time.sleep(4)

username = browser.find_element_by_id("email_field")
username.send_keys(USERNAME)
time.sleep(1)

password = browser.find_element_by_id("password_field")
password.send_keys(PASSWORD)
time.sleep(1)

login = browser.find_element_by_xpath('//*[@id="modal_login_button"]')
login.click()
time.sleep(4)

#saves old tab title
window_previous = browser.window_handles[0]

#opens new tab
survey_results = browser.find_element_by_xpath('//*[@id="_ctl0_lnkSeeResults"]')
survey_results.click()
time.sleep(4)


browser.close()
browser.switch_to_window(window_previous)
browser.close()