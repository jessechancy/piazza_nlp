"""
Dependencies:
Download Selenium at https://sites.google.com/a/chromium.org/chromedriver/home
"""

import selenium
from selenium import webdriver
import time
from time import sleep
import csv
import json
from authentication import USERNAME, PASSWORD


def gather_posts(post_length):
    ## Authentication
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path = '/Users/jessechan/Desktop/15-112/piazza_nlp/chromedriver', 
                            options = chrome_options)
    browser.get('https://piazza.com/')
    
    log_in_button = browser.find_element_by_xpath('//*[@id="login_button"]')
    log_in_button.click()
    time.sleep(1)
    
    username = browser.find_element_by_id("email_field")
    username.send_keys(USERNAME)
    time.sleep(1)
    
    password = browser.find_element_by_id("password_field")
    password.send_keys(PASSWORD)
    time.sleep(1)
    
    login_button = browser.find_element_by_xpath('//*[@id="modal_login_button"]')
    login_button.click()
    time.sleep(1)
    
    ## Looking at Posts
    
    load_all_button = browser.find_element_by_xpath('//*[@id="loadMoreButton"]')
    load_all_button.click()
    time.sleep(1)
    
    post_count = int(browser.find_element_by_xpath('//*[@id="total_posts_count"]').text)
    
    posts = dict()
    #loops through all posts
    for i in range(post_count, post_count-post_length, -1): #loops from most recent backwards
        try:
            posts[f"{i}"] = dict()
            browser.get(f"https://piazza.com/class/jz16gkwriwo4vr?cid={i}")
            time.sleep(0.5)
            #post question text contents
            posts[f"{i}"]["heading"] = browser.find_element_by_xpath('//*[@id="view_quesiton_note"]/h1').text
            posts[f"{i}"]["body"] = browser.find_element_by_xpath('//*[@id="questionText"]').text
            posts[f"{i}"]["answered"] = True
            posts[f"{i}"]["answer"] = browser.find_element_by_xpath('//*[@id="i_answer"]/div[3]/div[1]').text
            posts[f"{i}"]["answered"] = False if posts[f"{i}"]["answer"] == "" else True
                
        except Exception as e:
            print(e)
    
    with open('data.txt', 'a+') as outfile:
        json.dump(posts, outfile)
    browser.close()
    return posts