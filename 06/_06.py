from datetime import datetime
import os
from sys import argv
import shutil
import argparse

def check_arguments(args=None):
    parser = argparse.ArgumentParser(description="Reorganizer")
    parser.add_argument('-D', '--days', help='Last modification date of file in formad dd.mm.yyyy', default='01.01.1997')
    parser.add_argument('-P', '--path', help='Path to folder', required='True')
    parser.add_argument('-S', '--size', help='Size of files in MB', default='10')
    parsed = parser.parse_args(args)
    return parsed.days, parsed.path, parsed.size

def processFile(file):
    tempdt = datetime.fromtimestamp(os.path.getmtime(file))
    if tempdt < standardDateTime:
        if not os.path.exists('Archive'):
            os.mkdir('Archive')
            shutil.move(file, '.\\Archive')


date, path, size = check_arguments(argv[1:])
standardDateTime = datetime.strptime(date, '%d.%m.%Y')
os.chdir(path)
listOfFiles = os.listdir()
for i in listOfFiles:
    processFile(i)