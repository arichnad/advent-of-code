#!/usr/bin/python3


data1='''
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

#for line in data:

first=[a for a in data.pop(0)]

data.pop(0)

N=50
P=N+2
H,W=len(data)+P*2,len(data[0])+P*2

input=[['.' for i in range(W)] for i in range(H)]

for j, line in enumerate(data):
	for i, ch in enumerate(line):
		input[j+P][i+P]=ch

for run in range(N):
	output=[['.' for i in range(W)] for i in range(H)]
	for j, line in enumerate(input):
		for i, ch in enumerate(line):
			bin=0
			for dy in range(-1,2):
				for dx in range(-1,2):
					bin*=2
					if j+dy<0 or j+dy>=H or i+dx<0 or i+dx>=W:
						continue
					bin+=1 if input[j+dy][i+dx]=='#' else 0
			output[j][i]=first[bin]

	for j in range(H):
		output[j][0]=output[j][1]
		output[j][-1]=output[j][-2]
	for i in range(W):
		output[0][i]=output[1][i]
		output[-1][i]=output[-2][i]
		

	input=output

print('\n'.join([''.join(o for o in line) for line in output]), sum([sum([1 if o=='#' else 0 for o in line]) for line in output]))

