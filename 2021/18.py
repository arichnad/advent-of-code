#!/usr/bin/python3


#data1=[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
#data1=[[1,1],[2,2],[3,3],[4,4],[5,5]]
data1=[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
[7,[5,[[3,8],[1,4]]]],
[[2,[2,2]],[8,[8,1]]],
[2,9],
[1,[[[9,3],9],[[9,0],[0,7]]]],
[[[5,[7,4]],7],1],
[[[[4,2],2],6],[8,7]]]
#data1=[[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
#[[[5,[2,8]],4],[5,[[9,9],0]]],
#[6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
#[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
#[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
#[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
#[[[[5,4],[7,7]],8],[[8,3],8]],
#[[9,3],[[9,9],[6,[4,9]]]],
#[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
#[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]]

data2=[]

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]


def addToLeft(a, index, value):
	for i in reversed(range(index)):
		if isinstance(a[i], list):
			if addToLeft(a[i], len(a[i]), value):
				return True
		else:
			a[i]+=value
			return True
	return False

def addToRight(a, index, value):
	for i in range(index, len(a)):
		if isinstance(a[i], list):
			if addToRight(a[i], 0, value):
				return True
		else:
			a[i]+=value
			return True
	return False

def explode(a, depth=0):
	for index, i in enumerate(a):
		if depth>=3:
			if isinstance(i, list) and not isinstance(i[0], list) and not isinstance(i[1], list):
				left,right=i[0],i[1]
				a[index]=0
				if index>0 and addToLeft(a, index, left):
					left=None
				if index+1<len(a) and addToRight(a, index+1, right):
					right=None
				return [left, right]
		if isinstance(i, list):
			retValue=explode(i, depth+1)
			if retValue!=False:
				left,right=retValue
				if left is not None and index>0 and addToLeft(a, index, left):
					left=None
				if right is not None and index+1<len(a) and addToRight(a, index+1, right):
					right=None
				return [left, right]

	return False

def split(a):
	for index, i in enumerate(a):
		if isinstance(i, list):
			if split(i):
				return True
		else:
			if i>=10:
				a[index]=[i//2, (i+1)//2]
				return True
	return False

def mag(a):
	if isinstance(a, list):
		return mag(a[0])*3+mag(a[1])*2
	else:
		return a



#output=None
#for i in data:
#	if output is None:
#		output=i
#	else:
#		output=[output, i]
#	#print('add', output)
#	changes=True
#	while changes:
#		changes=False
#		while explode(output)!=False:
#			changes=True
#			#print('explode', output)
#		if split(output):
#			changes=True
#			#print('split', output)
#	#print()
#print(mag(output), output)

best=-1
for i in data:
	for j in data:
		if i==j:
			continue
		import copy
		output=[copy.deepcopy(i), copy.deepcopy(j)]
		changes=True
		while changes:
			changes=False
			while explode(output)!=False:
				changes=True
				#print('explode', output)
			if split(output):
				changes=True
				#print('split', output)
		total=mag(output)
		if total>best:
			best=total
		#print(i, j, total)
print(best)

	

