#!/usr/bin/python3


data1='''
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0
'''.strip().splitlines()
data1Fold='''
fold along y=7
fold along x=5
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2
dataFold=data2Fold
N=1500

#data = [int(line) for line in data[0].split(',')]
data = [[int(a) for a in line.split(',')] for line in data]

a=[[False for i in range(N)] for j in range(N)]

for line in data:
	[x,y]=line
	a[y][x]=True

for line in dataFold:
	d,u,st=line.split(' ')
	ax,num=st.split('=')
	num=int(num)

	if ax=='x':
		for x in range(num+1,N):
			newX=num-(x-num)
			for j in range(N):
				if a[j][x]:
					if newX>=0:
						a[j][newX]=True
					a[j][x]=False
	else:
		for x in range(num+1,N):
			newX=num-(x-num)
			for j in range(N):
				if a[x][j]:
					if newX>=0:
						a[newX][j]=True
					a[x][j]=False
	print(sum(sum(line) for line in a))

for line in a[:10]:
	for i in line[:40]:
		print('#' if i else '.', end='')
	print()



