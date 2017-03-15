from sys import argv
from os.path import exists

if len(argv) == 1:
	print('Укажите файл для обработки')
	exit()
if exists(argv[1]) == False:
	print('Файл не существует')
	exit()
	
file = open(argv[1] 'rt')
alltextfiltered = ''
tuplealphabet = ()
for line in file:
	for i in line:
		if i.isalpha():
			alltextfiltered += i #Because Duke say's Fuck you optimization

