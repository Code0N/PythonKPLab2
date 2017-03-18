import argparse
from sys import argv
import os
import hashlib

def parse_arguments(args=None):
	argparser = argparse.ArgumentParser(description='DupFinder command line parametrs')
	argparser.add_argument('-P', '--path', help='Path to folder for comparation', required=True)
	parsed = argparser.parse_args(args)
	return parsed.path
	
pathtowork = parse_arguments(argv[1:])

def compare_files(path):
	dir_iterator = os.walk(path)
	
	

if not os.path.exists(pathtowork):
	print('Папки не существует')
elif not os.path.isdir(pathtowork):
	print('Папка не является папкой')
else:
	compare_files(pathtowork)