import datetime


# if used as cron job, creates in /home
with open('dateInfo.txt', 'a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))
