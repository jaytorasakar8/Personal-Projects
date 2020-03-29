from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
import re, urllib.request
from urllib.request import Request, urlopen
from datetime import datetime

def scripting():
     #URL to get the Latest Numbers on Coronavirus
     url="https://www.worldometers.info/coronavirus/"
     #We need to provide headers, otherwise we might get a 403: Forbidden error
     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
     #Converting the data website into standard readable format
     web_byte = urlopen(req).read()
     html = web_byte.decode('utf-8')
 
     #Parsing the html content and using lxml’s HTML parser
     soup = BeautifulSoup(html, 'lxml')

     #Obtain all the div tags which have class of 'maincounter-number'
     #Currently on that page, the data is stored in div tag with class 'maincounter-number'
     #There is a possibility that the class will be changed in the future
     divTag = soup.find_all("div", {"class": "maincounter-number"})
    
     #We strip all the whitespaces from the values
     cases = divTag[0].find('span').text.strip()
     deaths = divTag[1].find('span').text.strip()
     recovered = divTag[2].find('span').text.strip()

     #Location of the file where we want to store the data
     #NOTE: Update the data file location based on your local machine path
     myFile = open('/home/hadoop/CoronaVirusDataScrapper/data.csv','a') 
     
     #We are appending the data of number of cases, deaths and recovered worldwide
     #We are using ~ as the delimitier, since we are already having a comma in the number stats
     myFile.write('\n' + str(datetime.now()) + '~' + cases + '~' + deaths + '~' + recovered )
     #Giving a console output so that we know about the data collection
     print('Data collected at: ' + str(datetime.now()))


print('Starting Coronavirus data statistics collection......')
#Call the scripting function every 10 mins
#You change the data polling interval
schedule.every(10).minutes.do(scripting)

#Needed to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(.100) #Sleep interval is set to 100 milliseconds
    
