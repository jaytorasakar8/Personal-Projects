#!/usr/bin/python

from crontab import CronTab

cron = CronTab(user=True)

#Command to run the cron job
#NOTE: Need to give full path of the script file to be run
job = cron.new(command='python /home/hadoop/CoronaVirusDataScrapper/script_for_cron.py')

#Run the script every 10 minutes, which will get us the live stats
job.minute.every(10)

cron.write()
