from sys import argv
from os.path import exists

if len(argv) == 1:
	print('������� ���� ��� ���������')
	exit()
if exists(argv[1]) == False:
	print('���� �� ����������')
	exit()
	
file = open(argv[1] 'rt')
alltextfiltered = ''
tuplealphabet = ()
for line in file:
	for i in line:
		if i.isalpha():
			alltextfiltered += i #Because Duke say's Fuck you optimization

