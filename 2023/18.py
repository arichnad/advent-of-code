#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(30000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line.split(' ')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)



# minX,minY,maxX,maxY=min(i for i in range(W) for j in range(H) if m[j][i]!=0),min(j for i in range(W) for j in range(H) if m[j][i]!=0),max(i for i in range(W) for j in range(H) if m[j][i]!=0),max(j for i in range(W) for j in range(H) if m[j][i]!=0)
minX,minY=0,0

horizontals,verticals=[],[]
horizontalPositions,verticalPositions={}, {}
x,y=0,0
for line in data:
	hex=line[2].replace('(#','').replace(')','')
	dir,dist=int(hex[-1]),int(hex[:-1], 16)
	# dir = "rdlu".find(dir.lower())
	dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
	x0,y0=x,y
	x+=dx*dist
	y+=dy*dist
	line=vertical = (x0, y0, x, y)
	if x0==x:
		verticals.append(line)
		if x not in verticalPositions:
			verticalPositions[x]=[]
		verticalPositions[x].append(line)
	else:
		horizontals.append(line)
		if y not in horizontalPositions:
			horizontalPositions[y]=[]
		horizontalPositions[y].append(line)

verticals = sorted(verticals, key=lambda a:(min(a[0],a[2]),max(a[0],a[2])))
horizontals = sorted(horizontals, key=lambda a:(min(a[1],a[3]),max(a[1],a[3])))


horizontalUncounted=set()
verticalUncounted=set()
uncounted=set()
pointCounted=set()
def findSquares(startX, startY, endX, endY):
	width = endX-startX
	height = endY-startY
	# print(startX - minX, startY - minY, width, height)

	if (startX, endX, startY) in horizontalUncounted:
		horizontalUncounted.remove((startX, endX, startY))
	horizontalUncounted.add((startX, endX, endY))
	if (startY, endY, startX) in verticalUncounted:
		verticalUncounted.remove((startY, endY, startX))
	verticalUncounted.add((startY, endY, endX))

	pointCounted.add((startX, startY))
	# for yt in range(startY,startY+height):
	# 	for xt in range(startX,startX+width):
	# 		m[yt][xt]+=2

	return width*height

answer=0

lastX=None
for curX in sorted(verticalPositions.keys()):
	if lastX is None:
		lastX=curX
		continue

	lastY=None
	on = False
	for curY in sorted(horizontalPositions.keys()):
		if lastY is not None:
			for line in horizontalPositions[lastY]:
				if min(line[0],line[2]) <= lastX < max(line[0],line[2]):
					on = not on
					break


		if lastY is not None and on:
			out=findSquares(lastX, lastY, curX, curY)
			answer+=out

		lastY=curY

	lastX=curX


# print('v',[(c[0]-minY, c[1]-minY, c[2]-minX) for c in verticalUncounted])
# print('h',[(c[0]-minX, c[1]-minX, c[2]-minY) for c in horizontalUncounted])


for v in verticalUncounted:
	uncounted.add((v[2],v[0]))
	uncounted.add((v[2], v[1]))
	# for yt in range(v[0]+1,v[1]):
	# 	m[yt][v[2]]+=2
	answer+=v[1]-v[0]-1

for h in horizontalUncounted:
	uncounted.add((h[0], h[2]))
	uncounted.add((h[1], h[2]))
	# for xt in range(h[0]+1,h[1]):
	# 	m[h[2]][xt]+=2
	answer+=h[1]-h[0]-1

for (x,y) in uncounted:
	if (x,y) in pointCounted: continue
	# m[y][x]+=2
	answer+=1

# for j in range(minY-1,maxY+2):
# 	print(''.join(str(x) for x in m[j][minX-1:maxX+2]))

print(answer)



# W,H=900,900
# m=[[0 for i in range(W)] for j in range(H)]
# a=[(0,0)]
# x,y=W//2,H//2
# for line in data:
# 	dir,dist=line[0],int(line[1])
# 	dir = "rdlu".find(dir.lower())
# 	dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
# 	for i in range(dist):
# 		m[y][x]=1
# 		x+=dx
# 		y+=dy
# while len(a)>0:
# 	b=[]
# 	for thing in a:
# 		(x,y)=thing
# 		if x<0 or y<0 or x>=W or y>=H or m[y][x]!=0:
# 			continue
# 		m[y][x]=2
# 		b.append((x+1,y))
# 		b.append((x - 1, y))
# 		b.append((x, y+1))
# 		b.append((x, y-1))
# 	a=b
# for j in range(H):
# 	for i in range(W):
# 		m[j][i]=1 if m[j][i] != 2 else 0
#
# ans=0
# for j in range(H):
# 	for i in range(W):
# 		ans+=m[j][i]
# print(ans)
#
# minX,minY,maxX,maxY=min(i for i in range(W) for j in range(H) if m[j][i]!=0),min(j for i in range(W) for j in range(H) if m[j][i]!=0),max(i for i in range(W) for j in range(H) if m[j][i]!=0),max(j for i in range(W) for j in range(H) if m[j][i]!=0)
