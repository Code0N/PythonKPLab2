import re

userInput = input('Введите свою бесполезную строку\n').split(' ')

for i in range(len(userInput)):
	print(re.findall('[A-ZА-Я].*\d{2,4}', userInput[i]))