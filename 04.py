import re
from os.path import exists, isfile

pathtofile = input('Введите путь к файлу\n')

if not exists(pathtofile):
	print('Файла не существует')
if not isfile(pathtofile):
	print('Файл - не файл')
try:
	file = open(pathtofile, 'rt')
except:
	print('Ой, эксепшн')
finally:
	strings = file.readlines()

for i in range(len(strings)):
	result = re.findall(':..?\)+', strings[i]) #Чёрная магия
	numbers = re.search(':..?\)+', strings[i])
	if numbers != None:
		print('В строке {}, в позиции {} найдена следующая подстрока: {}'.format(i, numbers.span(), result))