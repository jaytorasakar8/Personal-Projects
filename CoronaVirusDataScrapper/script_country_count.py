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
from crontab import CronTab

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    #URL to get the Latest Numbers on Coronavirus
    url="https://www.worldometers.info/coronavirus/"
    #We need to provide headers, otherwise we might get a 403: Forbidden error
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    #Converting the data website into standard readable format
    web_byte = urlopen(req).read()
    html = web_byte.decode('utf-8')


    #Parsing the html content and using lxml’s HTML parser
    soup = BeautifulSoup(html, 'lxml')
    #Getting a list of all countries who have coronavirus cases 
    table = soup.find("table", {'id' : 'main_table_countries_today'})
    dict = {}

    #Dictonary contains key:value pair of Country Name and it's corresponding URL
    for row in table.findAll("a"):
        dict[row.text.lower().capitalize()] = row['href']

    country_name = input("Enter the name of Country to get the stats for Coronavirus: ").lower().capitalize()

    #If the user entered country is in our list then we continue, otherwise we give all the list of country names we support
    if country_name in dict:
        print("Country found in Coronavirus list")
        print(country_name)
    else:
        print("\nPlease Enter country name from this list:")
        print(list(dict.keys()))
        exit()

    #Each country has got it's own URL. Getting the country specific URL 
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

    #Print the current data stats for user entered country
    print("Time:", datetime.now(), bcolors.OKGREEN,"\nCurrent Coronavirus stats for", country_name.upper(), "are: ")

    print("Number of Cases:", cases, " Number of deaths:", deaths, " Number of recovered:", recovered, bcolors.ENDC)

    #Check if the user is interested to schedule a Cron Job for data collection of that country
    flag = input("Do you wish to schedule a cron job : [Y/N] ")
    
    #User may enter N or n, then exit
    if flag == 'N' or flag == 'n':
        print("Exiting")
        exit()

    print("Scheduling cron job for getting the data of the country", country_name.upper())
    
    #Cron Job 
    cron = CronTab(user=True)

    #Command to run the cron job for user specified country
    #There is another script "script_specific_country", which is used to schedule cron job based on country name
    command_cron = 'python /home/hadoop/covid/script_specific_country.py -c ' + country_name
    #Prefered to give the full path of the script file to be run
    job = cron.new(command=command_cron)
    #Run the script every 30 minutes
    job.minute.every(30)

    cron.write()


if __name__ == "__main__" or __name__ == "temp":
    main()
