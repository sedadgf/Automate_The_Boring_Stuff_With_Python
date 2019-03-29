# =============================================================================
#Checks if Amazon package is delivered to the mail box or to the door. 
# =============================================================================

#sendEmail(string,recipient) : Sends the notification to the specified recipient.
import sendemail
import time
from selenium import webdriver

browser=webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('https://www.amazon.co.uk')
time.sleep(10)
url=browser.find_element_by_id('nav-link-yourAccount')
url.click()
#Logs in to your amazon account
email=browser.find_element_by_id('ap_email')
email.send_keys('amazon_account_email_here')
password=browser.find_element_by_id('ap_password')
password.send_keys('your_password_here')
signin=browser.find_element_by_id('signInSubmit')
signin.click()
time.sleep(10)
accountpage=browser.find_element_by_id('nav-link-yourAccount')
accountpage.click()
time.sleep(10)
#Displays the orders page
orders=browser.find_element_by_class_name('ya-card__whole-card-link')
orders.click()
i=True
while(i==True):
        status=browser.find_element_by_id('Return-or-Replace-Items_1')
        if status.text=='Return or Replace Items':
            sendemail.sendGmail('Your last amazon order has been delivered',
                                'your_recipient_here')
            i==False            
        else:
            time.sleep(300)
            browser.refresh()
        


