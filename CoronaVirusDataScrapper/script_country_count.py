from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
import re, urllib.request
from urllib.request import Request, urlopen
from datetime import datetime
import os


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#URL to get the Latest Numbers on Coronavirus
url="https://www.worldometers.info/coronavirus/"
#We need to provide headers, otherwise we might get a 403: Forbidden error
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
#Converting the data website into standard readable format
web_byte = urlopen(req).read()
html = web_byte.decode('utf-8')


#Parsing the html content and using lxml’s HTML parser
soup = BeautifulSoup(html, 'lxml')

table = soup.find("table", {'id' : 'main_table_countries_today'})
dict = {}

for row in table.findAll("a"):
    dict[row.text.lower().capitalize()] = row['href']
    
#for i in dict:
    #print(i, dict[i])

country_name = input("Enter the name of Country to get the stats for Coronavirus: ").lower().capitalize()

if country_name in dict:
    print("Country found in Coronavirus list")
    print(country_name)
else:
    print("\nPlease Enter country name from this list:")
    print(list(dict.keys()))
    exit()

country_url = url + dict[country_name]
print(country_url)


#We need to provide headers, otherwise we might get a 403: Forbidden error
req_country = Request(country_url, headers={'User-Agent': 'Mozilla/5.0'})
    
#Converting the data website into standard readable format
web_byte = urlopen(req_country).read()
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

print("Time:", datetime.now(), bcolors.OKGREEN,"\nCurrent Coronavirus stats for", country_name.upper(), "are: ")

print("Number of Cases:", cases, " Number of deaths:", deaths, " Number of recovered:", recovered, bcolors.ENDC)


flag = input("Do you wish to schedule a cron job : [Y/N] ")

if flag == 'N':
    print("Exiting")
    exit() 

print("Scheduling cron job for getting the data of the country", country_name.upper())    

file_name = "data_" + country_name + ".csv"
file_path = os.path.join("/home/hadoop/covid/", file_name)

if os.path.exists(file_path):
    print("File already exists at that path, so appending the data points")
else:
    print("File doesn't exist, so creating a new file.....")

myFileHandler = open(file_path,'a')
#We are appending the data of number of cases, deaths and recovered worldwide
#We are using ~ as the delimitier, since we are already having a comma in the number stats
myFileHandler.write('\n' + str(datetime.now()) + '~' + cases + '~' + deaths + '~' + recovered )
