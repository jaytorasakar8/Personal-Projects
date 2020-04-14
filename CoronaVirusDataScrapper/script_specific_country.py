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

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Loading the latest list of countries affected from coronavirus
with open("/home/hadoop/covid/shared.json") as f:
    dict = json.load(f)

country_name = ''

#If no argument is passed, exit the program
#Our program needs atleast 1 argument to be passed
if len(sys.argv) <= 1:
    print (bcolors.FAIL+"[ERROR]: Incorrect arguments passed. Please enter the correct arguments", bcolors.ENDC)
    print (bcolors.WARNING+"[INFO]: If you want help please pass -h or --help as argument")
    print ("[INFO]: If you want to schedule a cron job, pass -c or --country and the name of the country", bcolors.ENDC)
    exit()

argumentList = sys.argv[1:] 
  
# Short options of 'help' and 'country' 
options = "hc:"
  
# Long options 
long_options = ["help","country="] 
  
try: 
    # Parsing argument 
    arguments, values = getopt.getopt(argumentList, options, long_options) 
    
    # checking each argument 
    for argument, value in arguments: 
        if argument in ("-c", "--country"): 
            country_name = value.lower().capitalize()
        elif argument in ("-h", "--help"): 
            print ("The script will get the current number Coronavirus cases, number of deaths and number of recovered for a user specified country.")
            print ("User can pass the argument '-c <Country Name>' or '--country <Country Name>'")
            print ("Sample program run: ", bcolors.BOLD, "\n\tpython script_specific_country.py -c India \n\tpython script_specific_country.py --country India", bcolors.ENDC)
            exit() 
    
except getopt.error as err: 
    # output error, and return with an error code 
    print (bcolors.FAIL+"[ERROR]: Error in arguments. Error message detail: ", str(err), bcolors.ENDC)
    exit()  


if country_name not in dict:
    print(bcolors.FAIL+"[ERROR]: Wrong Country name selected. Please select the name of the country from this list only")
    print(bcolors.BOLD, list(dict.keys()), bcolors.ENDC)
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

#Creating a custom file to store data based on the country name
file_name = "data_" + country_name + ".csv"
#Change the directory path as per your current system
file_path = os.path.join("/home/hadoop/covid/country_data/", file_name)

#Open the file if it's already present, otherwise create a new file for data points storing
myFileHandler = open(file_path,'a')
#We are appending the data of number of cases, deaths and recovered worldwide
#We are using ~ as the delimitier, since we are already having a comma in the number stats
myFileHandler.write('\n' + str(datetime.now()) + '~' + cases + '~' + deaths + '~' + recovered )
