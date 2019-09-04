from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains, keys
import time
from datetime import datetime

# Path for the chromedriver.exe file
# I am running the script on Windows, hence my path string contains backslash
driver = webdriver.Chrome('<Drive Name>:\\<Folder>\\chromedriver_win32\\chromedriver')

# Open Whatsapp Web page
driver.get("https://web.whatsapp.com/")
# If there is no response for 600 secs, the operation times out and we throw an exception
wait = WebDriverWait(driver, 600)

# Person or Group name whom you wish to send the whatsapp messsage
target = input('Enter the name of user or group : ')

# The message you wish to send to the user/group
string = input('Enter your message : ')

# Number of times you want to send the message
count = int(input('Enter the count : '))

# This ensures that we are not executing any further steps until the Whatsapp QR code is scanned and login is successful
# If we don't scan QR code, and continue to execute the next statements, they will give an exception
input('Enter anything after scanning QR code: ')

# We are trying to find the target user/group name in the HTML Page Source code using Xpath
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
user.click()
print("Specified user selected ")

# The message box element's class may be updated in the future!
# In case the script gives an error here, then go to the Whatsapp Web page and Right click on any chat's message and do Inspect Element, and get the div class element (Refer Readme's image)
msg_box = driver.find_element_by_class_name('_13mgZ')
print("Message box of user selected")

# Send n number of messages to the user
for i in range(count):
    msg_box.send_keys(string)
    # The button element's class may be updated in the future, similar to the message box mentioned above
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    print("Messsage sent to user successfully")

