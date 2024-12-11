#!/usr/bin/python3


data1='''
2199943210
3987894921
9856789892
8767896789
9899965678
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

a=[[int(a) for a in line] for line in data]


#answer=0
#for row in range(len(a)):
#	for col in range(len(a[row])):
#		if col-1>=0 and a[row][col]>=a[row][col-1]:
#			continue
#		if col+1<len(a[row]) and a[row][col]>=a[row][col+1]:
#			continue
#		if row-1>=0 and a[row][col]>=a[row-1][col]:
#			continue
#		if row+1<len(a) and a[row][col]>=a[row+1][col]:
#			continue
#		answer+=a[row][col]+1
#
#print(answer)

visited=[[False for a in line] for line in data]

def flood(row, col):
	if col<0 or row<0 or col>=len(a[row]) or row>=len(a):
		return 0
	if visited[row][col] or a[row][col]==9:
		return 0
	visited[row][col]=True
	answer=1
	if col-1>=0:
		answer+=flood(row, col-1)
	if col+1<len(a[row]):
		answer+=flood(row, col+1)
	if row-1>=0:
		answer+=flood(row-1, col)
	if row+1<len(a):
		answer+=flood(row+1, col)
	return answer
	
ans=[]
for row in range(len(a)):
	for col in range(len(a[row])):
		if col-1>=0 and a[row][col]>=a[row][col-1]:
			continue
		if col+1<len(a[row]) and a[row][col]>=a[row][col+1]:
			continue
		if row-1>=0 and a[row][col]>=a[row-1][col]:
			continue
		if row+1<len(a) and a[row][col]>=a[row+1][col]:
			continue
		ans+=[flood(row, col)]

l=list(reversed(sorted(ans)))
print(l[0]*l[1]*l[2])

