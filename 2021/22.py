#!/usr/bin/python3

#top of first star
data0='''
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
'''.strip().splitlines()
#bottom of first star, trimmed
data1='''
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
'''.strip().splitlines()
#second star, trimmed
data2='''

'''.strip().splitlines()

#0: 39:  27, 46, 38, 39
#1: 590784
#2: 474140
#3: 2758514936282235
data=data4

#data = [int(line) for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

##d=[[[False for i in range(101)] for j in range(101)] for k in range(101)]

def size(input):
	(xStart,xEnd,yStart,yEnd,zStart,zEnd,on)=input
	if xEnd<xStart or yEnd<yStart or zEnd<zStart: return 0
	answer=(xEnd-xStart+1)*(yEnd-yStart+1)*(zEnd-zStart+1)
	return answer if on else -answer

def intersection(a, b):
	if a is None:
		return b
	if b is None:
		return a
	(xStart1,xEnd1,yStart1,yEnd1,zStart1,zEnd1,on1)=a
	(xStart2,xEnd2,yStart2,yEnd2,zStart2,zEnd2,on2)=b
	#TODO:  on1 is weird here.  order matters.
	return (max(xStart1,xStart2),min(xEnd1,xEnd2),max(yStart1,yStart2),min(yEnd1,yEnd2),max(zStart1,zStart2),min(zEnd1,zEnd2), on1)

def negative(input):
	(xStart,xEnd,yStart,yEnd,zStart,zEnd,on)=input
	return (xStart,xEnd,yStart,yEnd,zStart,zEnd,not on)

def add(d, input, currentState, remaining=None):
	if len(d)==0:
		if input[6]!=currentState:
			d+=[(input, [])]
		return
	
	remaining=intersection(input, remaining)
	
	subtractNodes=[]
	for current in d:
		currentRemaining=intersection(remaining, current[0])
		if size(currentRemaining)==0:
			continue
		add(current[1], currentRemaining, not currentState, currentRemaining)
		#TODO for subtract nodes we might need to recurse too
		newSubtractNode=(negative(currentRemaining), [])
		subtractNodes+=[newSubtractNode]
	
	if currentState!=input[6]:
		newNode=(input, subtractNodes)
		d+=[newNode]


def answer(d):
	return sum(size(current[0])+answer(current[1]) for current in d)
	

d=[]
count=0
for line in data:
	on,coords=line.split(' ')
	on = True if on == 'on' else False
	x,y,z=coords.split(',')
	dummy,x=x.split('=')
	dummy,y=y.split('=')
	dummy,z=z.split('=')
	xStart,xEnd=[int(a) for a in x.split('..')]
	yStart,yEnd=[int(a) for a in y.split('..')]
	zStart,zEnd=[int(a) for a in z.split('..')]
	#TODO:  at the highest level ignore offs, or add a dummy root node?
	add(d, (xStart,xEnd,yStart,yEnd,zStart,zEnd,on), False)
	total=answer(d)
	print(len(d), line, total)

				
	#for x in range(xStart, xEnd+1):
	#	for y in range(yStart, yEnd+1):
	#		for z in range(zStart, zEnd+1):
	#			d[z+50][y+50][x+50]=on





