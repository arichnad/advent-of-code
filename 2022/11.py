#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''.strip().splitlines()
data2='''
Monkey 0:
  Starting items: 75, 75, 98, 97, 79, 97, 64
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 1:
  Starting items: 50, 99, 80, 84, 65, 95
  Operation: new = old + 2
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 5

Monkey 2:
  Starting items: 96, 74, 68, 96, 56, 71, 75, 53
  Operation: new = old + 1
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 3

Monkey 3:
  Starting items: 83, 96, 86, 58, 92
  Operation: new = old + 8
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 1

Monkey 4:
  Starting items: 99
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 5

Monkey 5:
  Starting items: 60, 54, 83
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 6:
  Starting items: 77, 67
  Operation: new = old * 17
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 7:
  Starting items: 95, 65, 58, 76
  Operation: new = old + 5
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6
'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

m=0
hasOriginal=[]
test=[]
true=[]
false=[]
operation=[]
for line in data:
	line=line.strip()
	if line.startswith('Starting'):
		x,items=line.split(': ')
		hasOriginal.append([int(i) for i in items.split(', ')])
	elif line.startswith('Operation'):
		x,op=line.split(': ')
		n,o = op.split(' = ')
		a,op,b=o.split(' ')
		operation.append([a,op,b])
	elif line.startswith('Test'):
		x,by=line.split(' by ')
		test.append(int(by))
	elif line.startswith('If true'):
		x,throw=line.split(' monkey ')
		throw=int(throw)
		true.append(throw)
	elif line.startswith('If false'):
		x,throw=line.split(' monkey ')
		throw=int(throw)
		false.append(throw)
	elif line=='':
		m+=1
m+=1

has=[row[:] for row in hasOriginal]

mTotal=[0 for i in range(m)]

for r in range(20):
	for monkey in range(m):
		for item in has[monkey]:
			mTotal[monkey]+=1
			o=operation[monkey]
			o1,o2=o[0],o[2]
			o1Value=item if o1=='old' else int(o1)
			o2Value=item if o2=='old' else int(o2)
			item=(o1Value * o2Value if o[1]=='*' else o1Value+o2Value)//3
			div = item % test[monkey] == 0
			has[true[monkey] if div else false[monkey]].append(item)
		has[monkey]=[]
s=list(reversed(sorted(mTotal)))
print(s[0]*s[1])

has=[row[:] for row in hasOriginal]

ll=math.lcm(*test)
mTotal=[0 for i in range(m)]

for r in range(10000):
	for monkey in range(m):
		for item in has[monkey]:
			mTotal[monkey]+=1
			o=operation[monkey]
			o1,o2=o[0],o[2]
			o1Value=item if o1=='old' else int(o1)
			o2Value=item if o2=='old' else int(o2)
			item=(o1Value * o2Value if o[1]=='*' else o1Value+o2Value)%ll
			div = item % test[monkey] == 0
			has[true[monkey] if div else false[monkey]].append(item)
		has[monkey]=[]
s=list(reversed(sorted(mTotal)))
print(s[0]*s[1])

