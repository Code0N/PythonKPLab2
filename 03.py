import os
from sys import argv

if len(argv) == 1:
	print('Укажите папку для обработки')
	exit()
if os.path.exists(argv[1]) == False:
	print('Папка не существует')
	exit()
if not os.path.isdir(argv[1]):
	print('Папка не является папкой')
	exit()

file = open(os.path.join(argv[1], 'list.txt'), 'rt')
nameslist = file.read().splitlines()

listdir = os.listdir(argv[1])

for i in listdir:
	for j in nameslist:
	#print(j[4:len(j)-8])
		if i[:len(i)-4] == j[4:len(j)-7]:
			print('Файл {} переименовывается в {}.mp3'.format(i, j[:len(j)-7]))
			os.rename(os.path.join(argv[1], i), os.path.join(argv[1], j[:len(j)-7])+'.mp3')

#for i in listdir:
#	print(i[:len(i)-4])
#
#print('\n')
#
#for i in nameslist:
#	print(i[4:len(i)-7])