from datetime import datetime
import os
from sys import argv
import shutil
import argparse

def check_arguments(args=None):
    parser = argparse.ArgumentParser(description="Reorganizer")
    parser.add_argument('-D', '--days', help='How much older files should be', default='5')
    parser.add_argument('-S', '--source', help='Path to folder', required='True')
    parser.add_argument('-R', '--size', help='Size of files in KB', default='10')
    parsed = parser.parse_args(args)
    return parsed.days, parsed.source, parsed.size


date, path, size = check_arguments(argv[1:])
size = int(size) * 1024
nowDateTime = datetime.today()
if not os.path.exists(path):
    print('Source not exists')
    exit()
if not os.path.isdir(path):
    print('Path isn\'t directory')
    exit()
os.chdir(path)
listOfFiles = os.listdir()
for i in listOfFiles:
    tempdt = datetime.fromtimestamp(os.path.getmtime(i))
    difference_days = (nowDateTime - tempdt).days
    if difference_days > int(date):
        if not os.path.exists('.\\Archive'):
            os.mkdir('.\\Archive')
        shutil.move(i, '.\\Archive\\')
        continue
    if os.path.getsize(i) < size:
        if not os.path.exists('.\\Small'):
            os.mkdir('.\\Small')
        shutil.move(i, '.\\Small\\')
        continue