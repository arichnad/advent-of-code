#!/usr/bin/python3


data1='''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''.strip().splitlines()
data2='''
3113284886
2851876144
2774664484
6715112578
7146272153
6256656367
3148666245
3857446528
7322422833
8152175168
'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
data = [[int(cd) for cd in line] for line in data]
answer=0
tot=len(data)*len(data[0])
			
def f(j,i):
	if data[j][i]<10:
		return
	if visited[j][i]:
		return
	global answer, vn
	visited[j][i]=True
	vn+=1
	answer+=1

	for y in range(-1,2):
		for x in range(-1,2):
			a,b=j+y,i+x
			if x!=0 or y!=0:
				if a>=0 and b>=0 and a<len(data) and b<len(data[a]):
					data[a][b]+=1
					f(a, b)

#depth=100 #problem 1 has depth 100
depth=10000
for k in range(depth):
	visited = [[False for cd in line] for line in data]
	vn=0
	for j in range(len(data)):
		for i in range(len(data[j])):
			data[j][i]+=1
			f(j, i)
	for j in range(len(data)):
		for i in range(len(data[j])):
			if data[j][i]>=10:
				data[j][i]=0
	if vn==tot:
		print(k+1)
		break
print(answer)
