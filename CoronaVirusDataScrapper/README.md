## Corona Virus Data Scrapper

This is just an attempt to get the number of Coronavirus cases, number of deaths and the number of people recovered across the world. 
I just created this project to see if I can use this data for predictive modeling at a later stage.

Currently, I am collecting the data of number of cases in the world, at an interval of every **10 minutes**.
Also I have included scripts to get data for a specific country in the world, and can collect the data for that specific country at an interval of every **30 minutes**
I am scrapping the data from [COVID-19 CORONAVIRUS PANDEMIC](https://www.worldometers.info/coronavirus/ "CoronaVirus Live Update")

I have written the script in Python 3 and you can scrap the data (every 10 minutes for the cases worldwide using either the schedular approach or using a cron job AND using a cron job for every 30 minutes for any user specified country), and then store the latest data into a csv file! 


#### How to run the script
1. By using the Python Scheduler(for getting the data for the World cases):
The python scheduling code is in ```script.py```
```
jay@jay-remote-machine:~/CoronaVirusDataScrapper$ python script.py
```
The only change that you need to make in this script is the path to the store the data.
The disadvantage of using a Scheduler is that you need to always keep the terminal open, and also it's even more difficult if you are connected to a remote machine. 

2. By using a Cron Job (for getting the data for the World cases):
For running the Cron job, we have two files. The ```scheduleCron.py``` and ```script_for_cron.py```. 
* In ```script_for_cron.py```, change the path where you wish to the store the data. 
* In ```scheduleCron.py```, update the path of the script for cron job, based on your local directory path. 
Then run the cron job scheduler using: 
```
jay@jay-remote-machine:~/CoronaVirusDataScrapper$ python scheduleCron.py 
```

* How to check if Cron Job is running (on Linux machine):
```
$ crontab -l
* * * * * python /home/hadoop/CoronaVirusDataScrapper/script_for_cron.py
```

3. If you want to run the python script in the background, then use: 
```
$ python scheduleCron.py &
```
Also if you want to run the python script and want to logout from the session/terminal(if you have script running on remote machine), you can use nohup(No Hangup signal) as follows(redirecting any errors to the log file): 
```
$ nohup python scheduleCron.py > output.log &
```

4. By getting the current stats (for a specific country):
For getting the current data for specific country, we have two files. The ```script_country_count.py``` and ```script_specific_country.py```. 
* In ```script_country_count.py```, change the command to run the cron job based on your local system path.
* In ```script_specific_country.py```, update the path where you wish to store your data for the country. 

We can schedule a Cron Job after we get the current stats for a specific country.

Then run the script and you can set the cron job as well using: 
```
jay@jay-remote-machine:~/CoronaVirusDataScrapper$ python script_country_count.py 
Enter the name of Country to get the stats for Coronavirus: india
Country found in Coronavirus list
India
https://www.worldometers.info/coronavirus/country/india/
Time: 2020-04-13 01:15:50.854069  
Current Coronavirus stats for INDIA are: 
Number of Cases: 9,240  Number of deaths: 331  Number of recovered: 1,096 
Do you wish to schedule a cron job : [Y/N] Y
Scheduling cron job for getting the data of the country INDIA 
```

5. Directly setting up a Cron Job (for getting the data for a specific country):
You can directly setup the cron job by editing the crontab using(this works in Linux): 
```
jay@jay-remote-machine:~/CoronaVirusDataScrapper$ crontab -e
```
Then you can add a cronjob in that file.
For example, I want to add a Cron Job for collecting the data of the country of "**Australia**" and I want my data to be collected at every 30 minutes interval, then add the following: 
```
*/30 * * * * python /home/hadoop/CoronaVirusDataScrapper/script_specific_country.py -c Australia
```
While adding the cronjob, you need to make sure that you pass the full path of the script file(as per your local machine path), since Cron Job fails sometimes if you don't pass the full path.



#### Output
1. On Terminal (on Linux), running the Python Scheduler (for getting the number of cases across the world): 

```
jay@jay-remote-machine:~/CoronaVirusDataScrapper$ python script.py

Starting Coronavirus data statistics collection......
Data collected at: 2020-03-28 20:08:51.154894
Data collected at: 2020-03-28 20:18:52.576481
Data collected at: 2020-03-28 20:28:54.154215
Data collected at: 2020-03-28 20:38:55.479815
Data collected at: 2020-03-28 20:48:57.158249
Data collected at: 2020-03-28 20:58:58.488289
Data collected at: 2020-03-28 21:08:59.960473
Data collected at: 2020-03-28 21:19:01.597552
```

2. Data stored in ```data.csv``` file: 
```
Timestamp,Cases,Deaths,Recovered

2020-03-28 20:08:51.154871~663,740~30,879~142,183
2020-03-28 20:18:52.576458~663,740~30,879~142,183
2020-03-28 20:28:54.154074~663,740~30,879~142,183
2020-03-28 20:38:55.479785~663,740~30,879~142,183
2020-03-28 20:48:57.158223~663,740~30,879~142,183
2020-03-28 20:58:58.488262~663,741~30,880~142,183
2020-03-28 21:08:59.960433~663,748~30,880~142,184
2020-03-28 21:19:01.597520~663,748~30,880~142,184
```

3. Data stored for a specific country:
Example: The data for the country "**Usa**" will be stored in ```data_Usa.csv``` file:
```
2020-04-13 19:30:01.955445~586,941~23,640~36,948
2020-04-13 20:00:01.815218~586,941~23,640~36,948
2020-04-13 20:30:05.071170~587,155~23,644~36,948
2020-04-13 21:00:03.861060~587,155~23,644~36,948
2020-04-13 21:30:03.409108~587,155~23,644~36,948
2020-04-13 22:00:02.237219~587,155~23,644~36,948
2020-04-13 22:30:02.745279~587,155~23,644~36,948
```


**Note**: I have used tilde(~) as the delimeter, since we have large numbers and they contain a comma! 

**Advantages:**
1. Data is stored in a csv file, so later can be used for data modeling and predictive analysis

2. Amount of space consumed by data is only 1 byte for every 10 min data interval. So that means we will be adding 144 bytes each day, or you can say, 1MB data in 1 week! We all have that much space on our disks :wink:

3. The scheduler automatically scraps the data at specified time interval without needing to monitor

4. You can get store the Data of multiple countries by scheduling multiple Cron Jobs, subject to space availability on your disk :wink:

#StaySafe #StayHome
