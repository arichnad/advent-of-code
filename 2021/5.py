#!/usr/bin/python3


data1='''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data=[int(d) for d in data[0].split(',')]

#for line in data:
#	a,b = line.split(' -> ')
#	x0,y0=[int(i) for i in a.split(',')]
#	x1,y1=[int(i) for i in b.split(',')]
#	x0,x1=min(x0, x1),max(x0,x1)
#	y0,y1=min(y0, y1),max(y0,y1)
#
#	if x0!=x1 and y0!=y1:
#		continue
#	for x in range(x0,x1+1):
#		for y in range(y0,y1+1):
#			print(x, y)


for line in data:
	a,b = line.split(' -> ')
	x0,y0=[int(i) for i in a.split(',')]
	x1,y1=[int(i) for i in b.split(',')]
	dx=x1-x0
	if dx!=0:
		dx=1 if dx>0 else -1
	dy=y1-y0
	if dy!=0:
		dy=1 if dy>0 else -1

	x,y=x0,y0
	while y!=y1 or x!=x1:
		print(x, y)
		y+=dy
		x+=dx
	print(x, y)

