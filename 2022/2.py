#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
A Y
B X
C Z
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
#	f,s=line.split(' ')
#	if f=='A':
#		if s=='X':
#			t+=1+3
#		elif s=='Y':
#			t+=2+6
#		elif s=='Z':
#			t+=3+0
#	elif f=='B':
#		if s=='X':
#			t+=1+0
#		elif s=='Y':
#			t+=2+3
#		elif s=='Z':
#			t+=3+6
#	elif f=='C':
#		if s=='X':
#			t+=1+6
#		elif s=='Y':
#			t+=2+0
#		elif s=='Z':
#			t+=3+3
#		
#	print(t)

t=0
for line in data:
	f,s=line.split(' ')
	if f=='A':
		if s=='Y':
			t+=1+3
		elif s=='Z':
			t+=2+6
		elif s=='X':
			t+=3+0
	elif f=='B':
		if s=='X':
			t+=1+0
		elif s=='Y':
			t+=2+3
		elif s=='Z':
			t+=3+6
	elif f=='C':
		if s=='Z':
			t+=1+6
		elif s=='X':
			t+=2+0
		elif s=='Y':
			t+=3+3
		
	print(t)

