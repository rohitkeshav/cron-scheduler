from crontab import CronTab
from settings import BASE_DIR

my_cron = CronTab(user='rohit')
job = my_cron.new(command=f'python {BASE_DIR}/schedule_cron.py')
job.minute.every(1)

my_cron.write()
