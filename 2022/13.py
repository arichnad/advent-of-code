#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''.strip().splitlines()
data2='''
'''.strip().splitlines()

data=data2


#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

import ast

def rec(a, b):
	if isinstance(a, int) and isinstance(b, int):
		return b-a
	if isinstance(a, int):
		return rec([a], b)
	if isinstance(b, int):
		return rec(a, [b])
	if len(a)==0 and len(b)==0:
		return 0
	if len(a)==0:
		return 1
	if len(b)==0:
		return -1
	
	aa=a.pop(0)
	bb=b.pop(0)

	value=rec(aa, bb)
	if value==0:
		return rec(a, b)
	else:
		return value

n=0
answer=0
row=[]
for line in data:
	if line=='':
		answer+=n+1 if rec(row[0], row[1])>0 else 0
		n+=1
		row=[]
		continue
	else:
		row.append(ast.literal_eval(line))
answer+=n+1 if rec(row[0], row[1])>0 else 0
print(answer)

data.append('')
data+='''
[[2]]
[[6]]
'''.strip().splitlines()


n=0
answer=0
row=[]
for line in data:
	if line=='':
		continue
	row.append(ast.literal_eval(line))

s=sorted(row, key=functools.cmp_to_key(lambda x,y: rec(copy.deepcopy(y), copy.deepcopy(x))))
answer=1
for i in range(len(s)):
	if s[i]==[[2]]:
		answer*=i+1
	if s[i]==[[6]]:
		answer*=i+1
print(answer)


