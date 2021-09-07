import os
import subprocess
from getpass import getpass

# SELECT HOST INI HERE
FILE_PATH = 'opsta-host/monitoring.ini'
"""
# information inside file format
any ansible_user=xxxx ansible_host=xxxx
"""

root_path = os.getcwd()
inventories_folder = os.path.join(root_path, 'inventories')
inventories_file = os.path.join(inventories_folder, os.path.normpath(FILE_PATH))

password = getpass('Enter password for all remote host: ')

with open(inventories_file) as f:
    for line in f.readlines():
        if 'ansible_user' in line and 'ansible_host' in line:
            split_text = line.split()
            ansible_user = [select_text for select_text in split_text if 'ansible_user' in select_text][0].split('=')[1]
            ansible_host = [select_text for select_text in split_text if 'ansible_host' in select_text][0].split('=')[1]
            subprocess.call(f"sshpass -p {password} ssh-copy-id {ansible_user}@{ansible_host}", shell=True)
