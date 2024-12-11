#!/usr/bin/python3

data='''
.#.
..#
###
'''.strip().splitlines()

data='''
'''.strip().splitlines()

N=40
mid=N//2
value=[[['.' for x in range(N)] for y in range(N)] for z in range(N)]

for y, line in enumerate(data):
	for x, ch in enumerate(line):
		value[mid][y+mid][x+mid] = ch

#for z in range(N):
#	for y in range(N):
#		print(''.join(value[z][y]))
#	print()
#print()
for cycle in range(6):
	newValue=[[[value[z][y][x] for x in range(N)] for y in range(N)] for z in range(N)]
	for z in range(N):
		for y in range(N):
			for x in range(N):
				total=0
				for dz in range(-1,2):
					for dy in range(-1,2):
						for dx in range(-1,2):
							if dx == 0 and dy == 0 and dz == 0: continue
							if x+dx < 0 or x+dx == N: continue
							if y+dy < 0 or y+dy == N: continue
							if z+dz < 0 or z+dz == N: continue
							total += 1 if value[z+dz][y+dy][x+dx] == '#' else 0
				if value[z][y][x] == '#':
					newValue[z][y][x]='#' if 2 <= total <= 3 else '.'
				else:
					newValue[z][y][x]='#' if total == 3 else '.'
					
	value=newValue
	print(cycle)
	#for z in range(N):
	#	for y in range(N):
	#		print(''.join(value[z][y]))
	#	print()
	#print()



output=0
for z in range(N):
	for y in range(N):
		for x in range(N):
			output+=1 if value[z][y][x] == '#' else 0

print(output)


N=18
mid=N//2
mid2=mid-4
value=[[[['.' for x in range(N)] for y in range(N)] for z in range(N)] for w in range(N)]

for y, line in enumerate(data):
	for x, ch in enumerate(line):
		value[mid][mid][y+mid2][x+mid2] = ch

#for z in range(N):
#	for y in range(N):
#		print(''.join(value[z][y]))
#	print()
#print()
for cycle in range(6):
	newValue=[[[[value[w][z][y][x] for x in range(N)] for y in range(N)] for z in range(N)] for w in range(N)]
	for w in range(N):
		for z in range(N):
			for y in range(N):
				for x in range(N):
					total=0
					for dw in range(-1,2):
						for dz in range(-1,2):
							for dy in range(-1,2):
								for dx in range(-1,2):
									if dx == 0 and dy == 0 and dz == 0 and dw == 0: continue
									if x+dx < 0 or x+dx == N: continue
									if y+dy < 0 or y+dy == N: continue
									if z+dz < 0 or z+dz == N: continue
									if w+dw < 0 or w+dw == N: continue
									total += 1 if value[w+dw][z+dz][y+dy][x+dx] == '#' else 0
					if value[w][z][y][x] == '#':
						newValue[w][z][y][x]='#' if 2 <= total <= 3 else '.'
					else:
						newValue[w][z][y][x]='#' if total == 3 else '.'
					
	value=newValue
	print(cycle)
	#for z in range(N):
	#	for y in range(N):
	#		print(''.join(value[z][y]))
	#	print()
	#print()



output=0
for w in range(N):
	for z in range(N):
		for y in range(N):
			for x in range(N):
				output+=1 if value[w][z][y][x] == '#' else 0

print(output)
#1616

