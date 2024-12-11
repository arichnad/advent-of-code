#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

#R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83
data1='''
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#a=set()
#
#x,y=0,0
#for line in data[0].split(','):
#	v,dist=line[0],int(line[1:])
#	for i in range(dist):
#		if v=='U':
#			y-=1
#		elif v=='D':
#			y+=1
#		elif v=='L':
#			x-=1
#		elif v=='R':
#			x+=1
#		a.add((x,y))
#
#x,y=0,0
#best=100000000
#for line in data[1].split(','):
#	v,dist=line[0],int(line[1:])
#	for i in range(dist):
#		if v=='U':
#			y-=1
#		elif v=='D':
#			y+=1
#		elif v=='L':
#			x-=1
#		elif v=='R':
#			x+=1
#		if (x,y) in a:
#			best=min(best, abs(y)+abs(x))
#			print(best)
#print(best)
a=dict()

x,y,time=0,0,0
for line in data[0].split(','):
	v,dist=line[0],int(line[1:])
	for i in range(dist):
		if v=='U':
			y-=1
		elif v=='D':
			y+=1
		elif v=='L':
			x-=1
		elif v=='R':
			x+=1
		time+=1
		a[(x,y)]=time

x,y,time=0,0,0
best=100000000
for line in data[1].split(','):
	v,dist=line[0],int(line[1:])
	for i in range(dist):
		if v=='U':
			y-=1
		elif v=='D':
			y+=1
		elif v=='L':
			x-=1
		elif v=='R':
			x+=1
		time+=1
		if (x,y) in a.keys():
			best=min(best, time+a[(x,y)])
print(best)
