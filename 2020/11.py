#!/usr/bin/python3


data='''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''.strip().splitlines()
data='''
'''.strip().splitlines()

data=[[character for character in line] for line in data]

#changes=True
#while changes:
#	changes=False
#	newData=[[character for character in line] for line in data]
#	for y in range(len(data)):
#		for x in range(len(data[0])):
#			people=0
#			for dy in range(-1,2):
#				for dx in range(-1,2):
#					if dy==0 and dx==0: continue
#					if y+dy < 0 or y+dy >= len(data) or x+dx < 0 or x+dx >= len(data[0]): continue
#					if data[y+dy][x+dx] == '#': people+=1
#			if data[y][x]=='L' and people==0:
#				newData[y][x]='#'
#				changes=True
#			elif data[y][x]=='#' and people>=4:
#				newData[y][x]='L'
#				changes=True
#	data=newData
#
#print(sum([sum([character == '#' for character in line]) for line in data]))
#position=[[character for character in line] for line in data]
#for y in range(len(data)):
#	for x in range(len(data[0])):
#		for dy1 in range(-1,2):
#			for dx1 in range(-1,2):
#				for distance in range(1, 1000):
#					dy=dy1*distance
#					dx=dx1*distance
#					if dy==0 and dx==0:
#						position[y][x]=None
#						break
#					if y+dy < 0 or y+dy >= len(data) or x+dx < 0 or x+dx >= len(data[0]):
#						position[y][x]=None
#						break
#					if data[y+dy][x+dx] == 'L':
#						position[y][x]=
#						break

changes=True
while changes:
	changes=False
	newData=[[character for character in line] for line in data]
	for y in range(len(data)):
		for x in range(len(data[0])):
			people=0
			for dy1 in range(-1,2):
				for dx1 in range(-1,2):
					for distance in range(1, 1000):
						dy=dy1*distance
						dx=dx1*distance
						if dy==0 and dx==0: break
						if y+dy < 0 or y+dy >= len(data) or x+dx < 0 or x+dx >= len(data[0]): break
						if data[y+dy][x+dx] == '#':
							people+=1
							break
						if data[y+dy][x+dx] == 'L':
							break
			
			if data[y][x]=='L' and people==0:
				newData[y][x]='#'
				changes=True
			elif data[y][x]=='#' and people>=5:
				newData[y][x]='L'
				changes=True
	print('.')
	data=newData

print(sum([sum([character == '#' for character in line]) for line in data]))

