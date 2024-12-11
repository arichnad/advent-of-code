#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

b=[]
for line in data:
	if line=='':
		break
	b.append([column for column in line])
W=len(b[0])
H=len(b)
y=0
for i in range(W):
	if b[y][i]=='.':
		x=i
		break







#ok, i SHOULD have cleaned up the input.  that was a big mistake
#anywhere you see len(...) that was because i was dumb and didn't clean up the input

#aaalso, with my method for pt2, i couldn't use the sample data, all of my debugging was on the real thing





number=''
p=data[-1]
dx,dy=1,0

def u(newX, newY):
	move(newX, newY, -dx, -dy)
def left(newX, newY):
	move(newX, newY, dy, -dx)
def right(newX, newY):
	move(newX, newY, -dy, dx)

def move(newX, newY, tDx, tDy):
	global x,y,dx,dy
	if tDx!=0:
		for i in (range(len(b[newY])) if tDx==1 else reversed(range(len(b[newY])))):
			if b[newY][i]=='#':
				break
			if b[newY][i]=='.':
				x,y=i,newY
				dx,dy=tDx,tDy
				break
	if tDy!=0:
		for i in (range(H) if tDy==1 else reversed(range(H))):
			if newX>len(b[i]):
				continue
			if b[i][newX]=='#':
				break
			if b[i][newX]=='.':
				x,y=newX,i
				dx,dy=tDx,tDy
				break

def goNumber(number):
	global x,y,dx,dy
	number=int(number)
	for n in range(number):
#		#pt1
#		if dx!=0:
#			if x+dx<0 or x+dx>=len(b[y+dy]) or (b[y+dy][x+dx]==' '):
#				for i in (range(len(b[y])) if dx==1 else reversed(range(len(b[y])))):
#					if b[y][i]=='#':
#						break
#					if b[y][i]=='.':
#						x=i
#						break
#				continue
#		if dy!=0:
#			if y+dy==H or y+dy<0 or x+dx>=len(b[y+dy]) or b[y+dy][x+dx]==' ':
#				for i in (range(H) if dy==1 else reversed(range(H))):
#					if x>len(b[i]):
#						continue
#					if b[i][x]=='#':
#						break
#					if b[i][x]=='.':
#						y=i
#						break
#				continue
				
		if dx==1:
			if x+dx<0 or x+dx>=len(b[y+dy]) or (b[y+dy][x+dx]==' '):
				if y>=0 and y<50:
					u(x-50, 149-y)
				elif y>=50 and y<100:
					left(y+50, x-50) #right(y+50, x-50)
				elif y>=100 and y<150:
					u(x+50, 149-y)
				else:
					left(y-100, x+100) #right(y-100, x+100)
				continue
		elif dx==-1:
			if x+dx<0 or x+dx>=len(b[y+dy]) or (b[y+dy][x+dx]==' '):
				if y>=0 and y<50:
					u(x-50, 149-y)
				elif y>=50 and y<100:
					left(y-50, x+50) #right(y-50, x+50)
				elif y>=100 and y<150:
					u(x+50, 149-y)
				else:
					left(y-100, x) #right(y, x+100)
				continue
		elif dy==1:
			if y+dy==H or y+dy<0 or x+dx>=len(b[y+dy]) or b[y+dy][x+dx]==' ':
				if x>=0 and x<50:
					move(x+100, 199-y, dx, dy) #move(x-100, 199-y, dx, dy)
				elif x>=50 and x<100:
					right(y-100, x+100) #p
				else:
					right(y+50, x-50) #p
				continue
		elif dy==-1:
			if y+dy==H or y+dy<0 or x+dx>=len(b[y+dy]) or b[y+dy][x+dx]==' ':
				if x>=0 and x<50:
					right(y-50, x+50) #p
				elif x>=50 and x<100:
					right(y, x+100) #p
				else:
					move(x-100, 199-y, dx, dy) #p
				continue



		if b[y+dy][x+dx]=='#':
			break
		x+=dx
		y+=dy
	
	def dirChar(): return ('<' if dx==-1 else '>') if dx!=0 else ('^' if dy==-1 else 'v')
	#for r,l in enumerate(b): print(''.join([val if r!=y or c!=x else dirChar() for c,val in enumerate(l)]))

for ch in p:
	if ch=='L' or ch=='R':
		goNumber(number)
		number=''

		if ch=='R':
			dy,dx=dx,-dy
		else:
			dy,dx=-dx,dy
	else:
		number+=ch
goNumber(number)

r=0
if dx==1:
	r=0
if dx==-1:
	r=2
if dy==1:
	r=1
if dy==-1:
	r=3
print((y+1)*1000+4*(x+1)+r) #200200 too high

