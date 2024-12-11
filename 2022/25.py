#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

t=0
for line in data:
	l=len(line)
	ans=0
	for ch in line:
		ans*=5
		if ch=='-':
			ans-=1
		elif ch=='=':
			ans-=2
		else:
			ans+=int(ch)
	t+=ans
nex=0
out=''
while t>0 or nex!=0:
	n=(t%5)+nex
	t=t//5
	nex=0
	if n==0 or n==1 or n==2:
		out=str(n)+out
	if n==3:
		out='='+out
		nex=1
	if n==4:
		out='-'+out
		nex=1
	if n==5:
		out='0'+out
		nex=1

print(out)
	
	


		

