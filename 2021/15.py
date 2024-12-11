#!/usr/bin/python3


data1='''
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
data = [[int(a) for a in line] for line in data]
H=len(data)
W=len(data[0])

def scale(x):
	if x>9:
		x-=9
	return x

data = [[scale(data[j%H][i%W]+j//H+i//W) for i in range(5*W)] for j in range(5*H)]
H=len(data)
W=len(data[0])

#print('\n'.join([''.join([str(a) for a in line]) for line in data]))

best=[[10000 for i in range(W)] for j in range(H)]

changes=True
while changes:
	changes=False
	for j in range(H):
		for i in range(W):
			if i==0 and j==0:
				best[j][i]=0
				continue
			check=data[j][i]+min(best[j-1][i] if j>0 else 10000, best[j][i-1] if i>0 else 10000)
			if check < best[j][i]:
				best[j][i]=check
				changes=True

	for j in reversed(range(H)):
		for i in reversed(range(W)):
			check=data[j][i]+min(best[j][i+1] if i+1<W else 10000, best[j+1][i] if j+1<H else 10000)
			if check < best[j][i]:
				best[j][i]=check
				changes=True
	
print(best[-1][-1])



