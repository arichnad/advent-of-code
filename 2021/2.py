#!/usr/bin/python3


data1='''
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data=[int(d) for d in data[0].split(',')]

x,y=0,0
for line in data:
	c,n = line.split(' ')
	if c == 'forward':
		x+=int(n)
	elif c == 'down':
		y+=int(n)
	elif c == 'up':
		y-=int(n)
print(x*y)




x,y,aim=0,0,0
for line in data:
	c,n = line.split(' ')
	if c == 'forward':
		x+=int(n)
		y+=int(n)*aim
	elif c == 'down':
		aim+=int(n)
	elif c == 'up':
		aim-=int(n)
print(x*y)






