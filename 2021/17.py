#!/usr/bin/python3


data1='''
target area: x=20..30, y=-10..-5
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

#for line in data:

dummy,a=data[0].split(': ')
xN,yN=a.split(', ')
xN=xN.replace('x=','')
yN=yN.replace('y=','')
xStart,xEnd=xN.split('..')
yStart,yEnd=yN.split('..')
xStart,yStart,xEnd,yEnd=int(xStart),int(yStart),int(xEnd),int(yEnd)

bestY=-1
answer=0
for startDx in range(1,300):
	for startDy in range(-300,300):
		x,y,maxY=0,0,-1
		dx,dy=startDx,startDy
		for step in range(500):
			x+=dx
			y+=dy
			#if dy<0 and maxY<bestY:
			#	break
			if y>maxY:
				maxY=y
			if dx!=0:
				dx+=-1 if dx>0 else 1
			dy-=1
			if x>=xStart and y>=yStart and x<=xEnd and y<=yEnd:
				#print(startDx, startDy, step)
				answer+=1
				if maxY>bestY:
					bestY=maxY
				break

print(answer)
print(bestY)

