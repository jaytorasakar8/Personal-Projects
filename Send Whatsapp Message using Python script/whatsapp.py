from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains, keys
import time
from datetime import datetime

#Path for the chromedriver.exe file
driver = webdriver.Chrome('F:\\<Folder>\\chromedriver_win32\\chromedriver')

#Website which you want to open using script
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600) #if nothing works then throw exception in 600 secs

#Person or Group name whom you wish to send the whatsapp messsage
target = "Test" 

# Replace the below string with your own message
string = "You are being sent a message from a script!!!"

input('Enter anything after scanning QR code')


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
user.click()
print("Specified user selected ")

msg_box = driver.find_element_by_class_name('_13mgZ')
print("Message box of user selected")

#Send n number of messages to the user 
for i in range(2):
    msg_box.send_keys(string)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    print("Messsage sent to user successfully")

