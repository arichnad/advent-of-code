#!/usr/bin/python3

data='''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''.strip().splitlines()
data='''
'''.strip().splitlines()


x,y=0,0
count=0
while y<len(data):
	count += data[y][x]=='#'
	x=(x+3)%len(data[0])
	y+=1

print(count)



output=1
for dx,dy in ((1,1),(3,1),(5,1),(7,1),(1,2)):
	x,y=0,0
	count=0
	while y<len(data):
		count += data[y][x]=='#'
		x=(x+dx)%len(data[0])
		y+=dy
	output*=count

print(output)

