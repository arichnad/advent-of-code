#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''.splitlines()
data2='''

'''.splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

row=0
d=[]
for line in data[1:]:
	if line[1]=='1': break
	print(line)
	for i in range(len(line)//4+1):
		col=line[i*4+1]
		print(i, row, col)
		if i==len(d):
			d.append([])
		d[i].append(col)
	row+=1

d=[list(reversed(l)) for l in d]
d=[[i for i in l if i != ' '] for l in d]
print(d)

for line in data[row+3:]:
	dummy,num,dummy,f,dummy,to=line.split(' ')
	num,f,to=int(num),int(f)-1,int(to)-1
	for n in range(num):
		d[to].append(d[f].pop())
	print(d)

print(''.join([l[-1] for l in d]))

row=0
d=[]
for line in data[1:]:
	if line[1]=='1': break
	print(line)
	for i in range(len(line)//4+1):
		col=line[i*4+1]
		print(i, row, col)
		if i==len(d):
			d.append([])
		d[i].append(col)
	row+=1

d=[list(reversed(l)) for l in d]
d=[[i for i in l if i != ' '] for l in d]
print(d)

for line in data[row+3:]:
	dummy,num,dummy,f,dummy,to=line.split(' ')
	num,f,to=int(num),int(f)-1,int(to)-1
	a=[]
	for n in range(num):
		a.append(d[f].pop())
	d[to].extend(reversed(a))
	print(d)

print(''.join([l[-1] for l in d]))

