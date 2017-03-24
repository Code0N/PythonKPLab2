from sys import argv
from os.path import exists

if len(argv) == 1:
	print('Укажите файл для обработки')
	exit()
if exists(argv[1]) == False:
	print('Файл не существует')
	exit()
	
try:
	file = open(argv[1], 'rt', 512, 'utf-8')
except:
	print('Эксепшн')
finally:
	file.close()

alltextfiltered = ''
for line in file:
	for i in line:
		if i.isalpha():
			alltextfiltered += i #Because Duke say's Fuck you optimization
file.close()

letters = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'.upper() #Не будем заморачиваться
alltextfiltered = alltextfiltered.upper()

resultstring = ''

for i in letters:
	numcount = alltextfiltered.count(i)
	if numcount != 0:
		print("Буква {} встречается в тексте {} раз".format(i, numcount))
		#resultstring += ' |{} : {}|\n '.format(i, numcount)

#print(resultstring)