#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

t=0
subdir={}
cur={}
path=[]
for line in data:
	if line[0]=='$':
		cur[tuple(path)]=(cur[tuple(path)] if tuple(path) in cur else 0) + t
		t=0
		if line[2]=='c':
			cmd,d=line[2:].split(' ')
			if d=='..':
				path.pop()
			elif d=='/':
				path=[]
			else:
				path.append(d)
		if line[2]=='l':
			True
		continue
	if line[0]=='d':
		cmd,d=line.split(' ')
		if tuple(path) not in subdir:
			subdir[tuple(path)]=[]
		subdir[tuple(path)].append(d)
		continue
	a,dummy=line.split(' ')
	t+=int(a)
cur[tuple(path)]=(cur[tuple(path)] if tuple(path) in cur else 0) + t

def recurse(path):
	total=0
	if path in subdir:
		for s in subdir[path]:
			c=list(path)
			c.append(s)
			total+=recurse(tuple(c))
	return (cur[path] if path in cur else 0)+total
ans=0
for k,v in cur.items():
	r=recurse(k)
	if r<=100000:
		ans+=r
print(ans)

u=70000000-recurse(())

print(min(recurse(k) if recurse(k)+u>=30000000 else 70000000 for k,v in cur.items()))

