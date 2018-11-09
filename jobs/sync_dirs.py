import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# folder to back up
sync_folder = f'{BASE_DIR}/stuff1'
# backup file
backup_folder = f'{BASE_DIR}/stuff2'

cmd = f'/usr/bin/rsync {sync_folder}/* {backup_folder}/'

p = subprocess.Popen(cmd, shell=True).wait()
