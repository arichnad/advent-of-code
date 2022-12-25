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
11=22-1-1-10=1
1=111===21-0
102=-02=-012010-
1=-
21--0-20--=
211=-1--2-01--2-
1-===-1---
2-=01===2
12=0210=020100
110
21==01
2
1=-01=01
20-2-=-2222-2-2
1=1020==1-=12020=2
1-=-12010-=-1
112200==2-22120==1-
1=22-201-==-12001
1=0=--00-0-00==00
1--021
1-01
2-
2021==--0-1-210--=
1=1=0=02112-==1-1--
1202202-01--=-12-2
1=--10-
1-==202=022=1
1==-2=0
10=-=--
1=10
2=0-1-=2
12===0=-=12-0=1-10
10=20-=
11-1--21-=2=
2-00-1=-0=20
1001-2=--
2-12===202-10-=22
122-1=10=0021
1-2-
1-0-00020-
2=11
1112---=2-==
1--221121--
210-11120-0=1
11-1010-00=-
1=2-==2
2-1-
2-0-200--=211=02
111=1011-
21-2-1=-10=2--0===
220-=-
12--0=---1
210-
1-12-=-2-20202=2=
1=102-=-211212=0-2
121==20-00121-02=2
2-0-
22=1
111=222
201-2120=
21202
11
1===-0-==
1===00101=-2211121-2
1=02==10-
1222-21--121-1-0-
2-0210=201=-122-
210--022=01112
2222-221-=0-
1102--1-=21--=0
2-0212=0
220-2-==--212==2
1--0=--120210-1
1-0=1-120-=2--
22012-00--==-=220
1==
2=2=0002
222=1--1
2-1=
11-01
20-2010-==
1-=02=21==201=22
12--0210=10
10=1==1=2--01
1-02--=-00
1=0-00
1=-01-0100-1-0=122
2-=0-12=1=2-=11=00
122==11111=021=22
1==2=-0
1==-1-
12-0120202=-=2
202-2=212
2=1====2=1
1222-1-01
110=2
11010=--1=0-22
120
10=1122-0-0=
1=-1=2
2--200022=12200=2
1-20-00021
12=2===00
2-=-1-0=-0-=2=
1=-0-2=22==1-=-
1021-0=--2
1=012-1-1=-12=-10
2-1---=
10-121=21-1-
1022--1-02200-2==0
2=-=-01-
1=022-=11
10201--0211-2--0
2=-0010==2
2==--120111==12120
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
	
	


		

