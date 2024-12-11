#!/usr/bin/python3

data='''
'''.strip().splitlines()

count = 0
for line in data:
	specs, password = line.split(': ')
	rangeValues, letter = specs.split(' ')
	minimum, maximum = (int(value) for value in rangeValues.split('-'))

	count += minimum <= password.count(letter) <= maximum
print(count)

count = 0
for line in data:
	specs, password = line.split(': ')
	rangeValues, letter = specs.split(' ')
	yes, no = (int(value) for value in rangeValues.split('-'))

	count += (password[yes-1] == letter) ^ (password[no-1] == letter)
print(count)

