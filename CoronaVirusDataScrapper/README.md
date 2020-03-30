## Corona Virus Data Scrapper

This is just an attempt to get the number of Coronavirus cases, number of people died and the number of people recovered across the world. 
I just created this project to see if I can use this data for predictive modeling at a later stage.

Currently I am collecting the data at an interval of every **10 minutes**. 
I am scrapping the data from [COVID-19 CORONAVIRUS PANDEMIC](https://www.worldometers.info/coronavirus/ "CoronaVirus Live Update")

I have written the script in Python 3 and you can scrap the data every 10 minutes using either the schedular approach or using a cron job, and then store the latest data into a csv file! 


#### How to run the script
1. By using the Python Scheduler:
The python scheduling code is in ```script.py```
```
jay@jay-remote-machine:~/CoronaVirusDataScrapper$ python script.py
```
The only change that you need to make in this script is the path to the store the data.
The disadvantage of using a Scheduler is that you need to always keep the terminal open, and also it's even more difficult if you are connected to a remote machine. 

2. By using a Cron Job:
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

#### Output
1. On Terminal (on Linux)

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
Data collected at: 2020-03-28 21:29:03.128473
Data collected at: 2020-03-28 21:39:04.755300
Data collected at: 2020-03-28 21:49:06.210028
```

2. Data stored in the data.csv: 
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
2020-03-28 21:29:03.128445~663,749~30,880~142,184
2020-03-28 21:39:04.755271~663,926~30,880~142,184
2020-03-28 21:49:06.210001~663,928~30,882~142,361
```
**Note**: I have used tilde(~) as the delimeter, since we have large numbers and they contain a comma! 

**Advantages:**
1. Data is stored in a csv file, so later can be used for data modeling and predictive analysis

2. Amount of space consumed by data is only 1 byte for every 10 min data interval. So that means we will be adding 144 bytes each day, or you can say, 1MB data in 1 week! We all have that much space on our disks :wink:

3. The scheduler automatically scraps the data at specified time interval without needing to monitor

#StaySafe #StayHome
