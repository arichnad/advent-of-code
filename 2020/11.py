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
LLLLLLLLL.L.LLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLL..LLLLLL.LLLLLLLL.LLLLL.LL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLL..LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL..LL.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLL..LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLL.LLLLL.LLLLLLLLLL..LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLL.LLLL.LLLLLLLLLL..LLLL.L.LLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LL.LLLLLL.LLLLLL.LLLLLLLLLLL.LLLLLLLLLL.L.LLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LL.L.LLLL.L.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL
......L.L.L....LL.L.L..L.L..LL...L......LL..L.....L.LL.LLLL.LL.L..LL........L..LL.LLL.L..L.LL.L..L
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLL.L.LLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLL.L.LL.LLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLL.LLL.LLLLL.LL.LLLLLLLLL.LLLLLL.LLL..LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.L.LLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLLL.L...LLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLL..LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLL.LLLLLLLLLLLLL.L
LLLLLLLL..LL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLL.LLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLL.LLLL.LL.LLLLLLLLLLLLLLLLLLLL
LL..L.....L..L.L...LL...........LLL.L.L..L.L.....LL....LL....L...L...L..LL.L...LL.LL.LLL.L.L.LL.L.
LLLLLLL.L.LLLLLL.LLL.LLLLLLLLLLLLLLLLLL.LLLL.LL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLL.LL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLL.LL.LLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLLLLLL.LLL.LLLLLLL
.LLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLL.LL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLL.LLL.LLLLL.LLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.L.LL.LLLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL..LLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.L.LL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LL.LLL.LLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL..LLLLLLL.LLLL.LLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
.L..L..L..........L...L.LL..L...LL....LL..LL..L...L.LL.L.L..LLLL..L.L....L.......LL........L.L..L.
LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLL.LLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLL.LL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLL.L.LLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL..LLL.LLLL.LLLLLLLLLLL.LLL.LLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LL.LL.LLL.LLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLL.LL.LLLLLLLLLLLL
LLLLLLL.L.LLL..LL.LLLLLLLLLLLL.LLLLLLLLL.LLL.LLLL.LLLLL..LLLL..LLLL.L.LLLLLLL.LLLLLL.LL.LLLLLLLLLL
L.LL...L..L..L.....L...L..LL...L..LL.L.....LL.LL.L...LL.LL...L....LLL.L..LL.L.L.LL..L..LL.L.L.L..L
LLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLL..LLLLLL.LLLL.LLLLLLLL.LL.LLLLL.LLLL.LL.L.LLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.L.LLL.LLLL
LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLLLL..LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL..LLL.LL..L.L.LLL.LLL.LLLLLLLLL.LLLLLLLLLL
L...LLL.L......LL....L.......L..L.LLL..LL.LL.L.....LL.LL.L....L.L....LL....L....LL...L.L.....L....
LLLLLLLLL.LLLLLL.L.LL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LL.LLLLLLLL.LLL.LLLLLLLLL..LL.LLLL.LLLLLLLLLLL..L.L.LLLLLLL.LL.LLLL.LLLLLLLLL.LLLLLLLLLL
....L.L..L.L...L....L..L...L.LLL...L..LL.L..L.LL.L....L.................L...LL.LL......L...L...LL.
LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.L.LL.LLLL.LLLL.LLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
.....L.LLLL.L.........LL.L..L...LL..LLL..L......LLL.....L.......L.LL.L.L........L...LLLLLL.L..LLL.
LLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLL.LLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.L.LLLLLL.LLLLLLLLLLLLL.LL.L.LLLLLLL.LLL.L.LLLLLLLLLLLLL.LLLLLL.LL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLL..LLLLLLLLLL.LLLLL.L.LLLLLLL.LLLLLLLLL.LLLLL.LLLL
LLLL.....L.L...L.....L..L.L..L......LL..L...LL...L.LLL.L.L..L....L......LL.LL.L..L.L....L...LL..LL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.L
LLLLLLLLL.L.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LL.LLL..LLLLLLLLLLL.L.LLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLLLLL.LL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLL.LL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LL.L..LLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLL.L.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.L.LL.LLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.L.LLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLL.LL.LLLLLLLLLLLLLLLLLLLL
..LL.LL...L....LLLLL.....L.L..LL.L...LLLL.............L..L.LLL..........L.L...LL..LL.....LL.......
LLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LL.LLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLL..LLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLL.LL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLL.LLL.LLLLL.LLL.LLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLL.LLLL.LLLLLLL.LLL.LL..LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LL.LLL.LLLL.LLLL.LLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLL
..LLLL.LLL...LLLLL..........L...L......L..LL.....L..L..L..L.L..L..L.L..L.......L..L....LL.L.L.L.L.
LLLLLL.LL.LLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLL.LL.LLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLL.L.LLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLL..LLLL..LLLLLLLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLL.LLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL..LLLLLLLLL
LLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLL.LLL..LLLL.LLL.LL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LLLL.LLL..LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL...LLLLLLLLL
L.LLLLLLL.LLLLLLL.LLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLL.L
LLLLLLL.L.LLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL..LLLLLLLLLL..LLLLLLL.LLLLLLLLLLLLLLLLLLLL
.LL...............L..L.L.LL...L.LL.....LL..L.LL.L.L...L.......L..L.LL..L.L...LL...L...............
LLLLLLLLL.LLLLLL..LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLLLL.LLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.L.LLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.L.LLL.LLLLLL.LLL.LLLL.L.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLL.LL.LLL.LLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLL.LLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
L.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLLL.LLLLLL.LLLL.LLLLLL..LLLLLLL.LLLLLLLLL.LLLLLLLLLL
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
