import os
import sys
import argparse

from crontab import CronTab
from settings import BASE_DIR


def sanitize(jb):
        jb = jb.strip()
        return jb[:-3] if jb[-3:] == '.py' else jb


"""
    Function expects the job .py file exists in project root
    Hence the check
"""


def run_cron(job_name):
    """
    :param job_name: name of .py file that used as a job
    :return: None
    :caveats: The command attribute of cron.new() requires absolute path of the .py file
    """

    cron = CronTab(user='rohit')
    job = cron.new(command=f'python {BASE_DIR}/jobs/{job_name}.py')

    job.minute.every(1)
    cron.write()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("job_name")
    args = parser.parse_args()

    run_job = sanitize(args.job_name)

    if not os.path.exists(f'jobs/{run_job}.py'):
        sys.exit(f'{run_job}.py does not exist in jobs/')

    print(f'Running cron job - {run_job} \n')

    run_cron(run_job)
