import argparse
from sys import argv
import os
import hashlib

hashdict = {}

def parse_arguments(args=None):
	argparser = argparse.ArgumentParser(description='DupFinder command line parametrs')
	argparser.add_argument('-P', '--path', help='Path to folder for comparation', required=True)
	parsed = argparser.parse_args(args)
	return parsed.path
	
pathtowork = parse_arguments(argv[1:])

def get_md5(file):
	with open(file, 'rb') as f:
		m = hashlib.md5()
		while True:
			data = f.read(8192)
			if not data:
				break
			m.update(data)
		return m.hexdigest()

def compare_files(path):
	dir_iterator = os.walk(path)
	for fd in dir_iterator:
		root, dirs, files = fd #Так ведь можно, да?
		for i in files:
			hashdict[os.path.join(root, i)] = get_md5(os.path.join(root, i))
	#Дальше сам компаратор
	for i in hashdict.keys():
		print('Файлу {} соответствуют следующие файлы:\n'.format(i))
		for j in hashdict.keys():
			if hashdict[i] == hashdict[j]:
				print('-->{}\n'.format(j))

if not os.path.exists(pathtowork):
	print('Папки не существует')
elif not os.path.isdir(pathtowork):
	print('Папка не является папкой')
else:
	compare_files(pathtowork)