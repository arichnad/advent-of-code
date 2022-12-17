#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

shapes=['''
####
'''.strip().splitlines(),
'''
.#.
###
.#.
'''.strip().splitlines(),
'''
..#
..#
###
'''.strip().splitlines(),
'''
#
#
#
#
'''.strip().splitlines(),
'''
##
##
'''.strip().splitlines()]

data1='''
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''.strip().splitlines()
data2=open('d', 'r').read().strip().splitlines()
data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data=data[0]


#for line in data:

F=1000000000000
H=400000
W=7


def doPlace(x, y, piece):
	h=len(piece)
	for j in range(len(piece)):
		for i in range(len(piece[j])):
			if piece[j][i]=='#':
				b[y+(h-1)-j][i+x]=True
def clean(x, y, piece):
	h=len(piece)
	w=len(piece[0])
	if x+w-1>=W or x<0:
		return False
	if y<0:
		return False
	for j in range(len(piece)):
		for i in range(len(piece[j])):
			if piece[j][i]=='#' and b[y+(h-1)-j][i+x]:
				return False
	return True
def lowest():
	for j, row in enumerate(b):
		rowEmpty=True
		for i, col in enumerate(row):
			if col:
				rowEmpty=False
				break
		if rowEmpty:
			return j
def getFloor():
	start=lowest()-1
	floor=[]
	for i in range(W):
		j=start
		while j>=0 and not b[j][i]:
			j-=1
		floor.append(start-j)
	return tuple(floor)
def shift(n):
	total=0
	while n>0:
		n//=2
		total+=1
	return total-1

b=[[False for x in range(W)] for y in range(H)]
n=0
curX,curY=2,3
placed=0
piece=0
while True:
	
	dx=1 if data[n%len(data)]=='>' else -1
	dy=-1

	if clean(curX+dx, curY, shapes[piece]):
		curX+=dx
	if clean(curX, curY+dy, shapes[piece]):
		curY+=dy
	else:
		doPlace(curX, curY, shapes[piece])
		piece=(piece+1)%5
		curX=2
		curY=3+lowest()
		placed+=1
		if placed==2022: break
	n+=1
print(lowest())

b=[[False for x in range(W)] for y in range(H)]
placed=0
piece=0
oldLowest=0
oldFloor=getFloor()
save={}
curX,curY=2,3
L=len(data)
mod=0
firstMod=0

while True:
	
	nextMod=(mod+1)%L
	dx=1 if data[mod]=='>' else -1
	dy=-1

	if clean(curX+dx, curY, shapes[piece]):
		curX+=dx
	if clean(curX, curY+dy, shapes[piece]):
		curY+=dy
	else:
		doPlace(curX, curY, shapes[piece])
		newFloor=getFloor()
		newLowest=lowest()
		nextPiece=(piece+1)%5
		save[(oldFloor, firstMod, piece)]=[(newFloor, newLowest-oldLowest, nextMod, nextPiece)]
		oldFloor=newFloor
		oldLowest=newLowest
		firstMod=nextMod
		#for row in reversed(b):
		#	print(''.join(['#' if i else '.' for i in row]))
		placed+=1
		if (placed%100)==0:
			print(placed, len(set(floor for (floor,mod,piece) in save.keys())))
		#if placed==2022: break
		
		curX=2
		curY=3+lowest()
		piece=nextPiece
		
		if (oldFloor, firstMod, piece) in save:
			for i in range(40):
				for firstKey in save.keys():
					(floor, change1, mod, piece)=save[firstKey][i]
					(floor, change2, mod, piece)=save[(floor, mod, piece)][i]
					save[firstKey].append((floor, change1+change2, mod, piece))

			left=F-placed
			floor=oldFloor
			mod=firstMod
			piece=nextPiece
			while left>0:
				(floor, change, mod, piece)=save[(floor, mod, piece)][shift(left)]
				newLowest+=change
				left-=1<<shift(left)

			print(newLowest)
			break


	#print(curX, curY, data[mod], dx)


	mod=nextMod
#print('old', lowest())

