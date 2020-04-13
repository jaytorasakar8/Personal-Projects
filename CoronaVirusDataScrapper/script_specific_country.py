#!/usr/bin/python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import time
import re, urllib.request
from urllib.request import Request, urlopen
from datetime import datetime
import os
import json
import getopt, sys 


with open("/home/hadoop/covid/shared.json") as f:
    dict = json.load(f)

country_name = ''

if len(sys.argv) <= 1:
    print ("Error: Please enter the correct argument")
    print ("If you want help please pass -h or --help as argument")
    print ("if you want to schedule a cron job, pass -c or --country and the name of the country")
    exit()

argumentList = sys.argv[1:] 
  
# Options 
options = "hc:"
  
# Long options 
long_options = ["help","country="] 
  
try: 
    # Parsing argument 
    arguments, values = getopt.getopt(argumentList, options, long_options) 
    
    # checking each argument 
    for currentArgument, currentValue in arguments: 
        if currentArgument in ("-c", "--country"): 
            country_name = currentValue.lower().capitalize()
        elif currentArgument in ("-h", "--help"): 
            print ("Diplaying Help")
            exit() 
    
except getopt.error as err: 
    # output error, and return with an error code 
    print ("Error in arguments. Error message detail: ", str(err))
    exit()    
if country_name not in dict:
    print("Please select the name of the country from this list only")
    print(list(dict.keys()))
    exit()

#URL to get the Latest Numbers on Coronavirus
url="https://www.worldometers.info/coronavirus/"

#Custom URL for the user provided country
country_url = url + dict[country_name]

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

file_name = "data_" + country_name + ".csv"
file_path = os.path.join("/home/hadoop/covid/country_data/", file_name)

# if os.path.exists(file_path):
#     print("File already exists at that path, so appending the data points")
# else:
#     print("File doesn't exist, so creating a new file.....")

myFileHandler = open(file_path,'a')
#We are appending the data of number of cases, deaths and recovered worldwide
#We are using ~ as the delimitier, since we are already having a comma in the number stats
myFileHandler.write('\n' + str(datetime.now()) + '~' + cases + '~' + deaths + '~' + recovered )
