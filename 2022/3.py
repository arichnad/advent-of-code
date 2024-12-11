#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#t=0
#for line in data:
#	first,second=line[:len(line)//2],line[len(line)//2:]
#	print(first,second)
#	for f in first:
#		if f in second:
#			if ord(f)>=ord('a') and ord(f)<=ord('z'):
#				t+=(ord(f)-ord('a')+1)
#			else:
#				t+=(ord(f)-ord('A')+27)
#			break
#print(t)


t=0
for l in range(len(data)//3):
	first=set(i for i in data[l*3]).intersection(i for i in data[l*3+1]).intersection(i for i in data[l*3+2])
	f=list(first)[0]
	print(first, f)
	if ord(f)>=ord('a') and ord(f)<=ord('z'):
		t+=(ord(f)-ord('a')+1)
	else:
		t+=(ord(f)-ord('A')+27)
print(t)

