#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
from collections import defaultdict, deque, Counter

data1='''
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]






d={}
e={}
humn=0
for line in data:
	monk,prob=line.split(': ')
	if ' ' in prob:
		a,b,c=prob.split(' ')
		d[monk]=(a,b,c)
	else:
		e[monk]=int(prob)


#part one

#def rec(monk):
#	print(monk)
#	if monk in e:
#		return e[monk]
#	a,b,c=d[monk]
#	if b=='+':
#		return rec(a)+rec(c)
#	if b=='/':
#		return rec(a)//rec(c)
#	if b=='*':
#		return rec(a)*rec(c)
#	if b=='-':
#		return rec(a)-rec(c)
#print(rec('root'))


def rec(monk):
	if monk=='humn':
		return humn
	if monk in e:
		return e[monk]
	a,b,c=d[monk]
	if b=='+':
		return rec(a)+rec(c)
	if b=='/':
		return rec(a)/rec(c)
	if b=='*':
		return rec(a)*rec(c)
	if b=='-':
		return rec(a)-rec(c)





def go():
	#root: pppw = sjmn
	#return rec('pppw')-rec('sjmn')
	#root: lttc = pfjc
	return rec('lttc')-rec('pfjc')

start=-100000000000000000
end=-start

dist=(end-start)/2
middle=(start+end)//2

#when under pressure i forgot how to do a binary search
while True:
	if dist<0.001:
		break
	#left
	humn=middle-dist
	leftVal=go()
	#right
	humn=middle+dist
	rightVal=go()
	if abs(leftVal)<abs(rightVal):
		middle-=dist
		#print('left', middle, leftVal, rightVal)
	else:
		middle+=dist
		#print('right', middle, leftVal, rightVal)
	dist/=2

humn=round(middle)
print(humn, rec('lttc'), rec('pfjc'))

