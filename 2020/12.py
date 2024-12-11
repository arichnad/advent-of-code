#!/usr/bin/python3


data='''
F10
N3
F7
R90
F11
'''.strip().splitlines()
data='''
'''.strip().splitlines()

direction=90
x,y=0,0
for line in data:
	order, num = line[0], line[1:]
	dist = int(num)
	if order == 'N':
		y+=dist
	elif order == 'S':
		y-=dist
	elif order == 'E':
		x+=dist
	elif order == 'W':
		x-=dist
	elif order == 'L':
		direction-=dist
		direction = (direction + 360) % 360
	elif order == 'R':
		direction+=dist
		direction = (direction + 360) % 360
	elif order == 'F':
		direction = (direction + 360) % 360
		direction2 = direction // 90
		if direction2 == 0:
			y+=dist
		elif direction2 == 1:
			x+=dist
		elif direction2 == 2:
			y-=dist
		elif direction2 == 3:
			x-=dist

print(abs(x)+abs(y))

direction=90
x,y=10,1
shipX,shipY=0,0
for line in data:
	order, num = line[0], line[1:]
	dist = int(num)
	if order == 'N':
		y+=dist
	elif order == 'S':
		y-=dist
	elif order == 'E':
		x+=dist
	elif order == 'W':
		x-=dist
	elif order == 'L':
		direction = (-dist + 360) % 360
		direction2 = direction // 90
		if direction2 == 0:
			True
		elif direction2 == 1:
			x,y=y,-x
		elif direction2 == 2:
			x,y=-x,-y
		elif direction2 == 3:
			x,y=-y,x

	elif order == 'R':
		direction = (dist + 360) % 360
		direction2 = direction // 90
		if direction2 == 0:
			True
		elif direction2 == 1:
			x,y=y,-x
		elif direction2 == 2:
			x,y=-x,-y
		elif direction2 == 3:
			x,y=-y,x
	elif order == 'F':
		shipX+=x*dist
		shipY+=y*dist

print(abs(shipX)+abs(shipY))

