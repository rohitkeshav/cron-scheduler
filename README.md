# Cron Scheduler

A python wrapper that can be used as boilerplate to setup python scripts as cron jobs
Written in a python 3.6 environment.
Feel free to play around with the sample scripts as cron jobs.

## Quick start

To setup the scheduler follow - 
    1. Clone the repository - git clone link
    2. run ``` pip install requirements ```
    3. Create a python script that needs to be set as cron job
    4. Store this script under jobs or change the path as seen fit
    5. To start the cron job run - 
            
        ```
            python schedule_cron.py <name of python script>
        ``` 
        
To check all the cron jobs running, run -
        ```
            crontab -l
        ```
To stop the cron jobs running, run -
        ```
            crontab -r
        ```

## Possible Caveats
As of now 
   - Does not seem to work with iterm on Mac OSX, script needs to be run using the regular terminal
   