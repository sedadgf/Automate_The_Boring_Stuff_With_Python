# =============================================================================
# Sends a new e-mail from a Gmail account. 
# =============================================================================
import time
from selenium import webdriver

def sendGmail(string,recipient):
    browser=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    browser.get('https://gmail.com')
    #Logs in to your gmail account
    email=browser.find_element_by_id('identifierId')
    email.send_keys('your_email_here')
    emailNext=browser.find_element_by_id('identifierNext')
    emailNext.click()
    password=browser.find_element_by_name('password')
    time.sleep(5)
    password.send_keys('your_password_here')
    passNext=browser.find_element_by_id('passwordNext')
    passNext.click()
    time.sleep(5)
    #Composes a new e-mail.
    compose=browser.find_element_by_class_name('z0')
    compose.click()
    time.sleep(5)
    to=browser.find_element_by_id(':p2')
    to.send_keys(recipient)
    subject=browser.find_element_by_id(':ok')
    subject.send_keys('This is an automatic message')
    msg=browser.find_element_by_id(':pp')
    msg.send_keys(string)
    send=browser.find_element_by_id(':oa')
    send.click()
    
