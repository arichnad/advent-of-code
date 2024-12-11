#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''.strip().splitlines()
data2='''

'''.strip().splitlines()


#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

def main():
	d={}
	for line in data:
		s=line.replace(',','').split(' ')
		label,rate,destinations=s[1],s[4],s[9:]
		rate=int(re.findall('-?[\d]+', rate)[0])
		destinations.append(label)
		d[label]=(rate,destinations)

	cur={('AA', 0): ((), 0)}
	new={}
	for minute in range(0, 30):
		for (pos, rate), (opened, total) in cur.items():
			total+=rate
			for newPos in d[pos][1]:

				newOpened=opened
				newRate=rate
				
				if pos==newPos:
					if pos in opened:
						continue
					newOpened=set(opened)
					newOpened.add(pos)
					newOpened=tuple(newOpened)
					newRate+=d[pos][0]
				
				if (newPos, newRate) not in new or total > new[(newPos, newRate)][1]:
					new[(newPos, newRate)]=(newOpened, total)
		cur=new
		new={}
	print(minute, max(total for (pos, rate), (opened, total) in cur.items())) #1651 1906
	

	cur={(('AA', 'AA'), 0): ((), 0)}
	new={}
	for minute in range(0, 30-4):
		for (pos, rate), (opened, total) in cur.items():
			total+=rate
			for newPos0 in d[pos[0]][1]:
				for newPos1 in d[pos[1]][1]:
					newPos=(newPos0, newPos1)
					
					newOpened=opened
					newRate=rate
					
					if pos[0]==newPos[0]:
						if pos[0] in newOpened:
							continue
						newOpened=set(newOpened)
						newOpened.add(pos[0])
						newOpened=tuple(newOpened)
						newRate+=d[pos[0]][0]
					
					if pos[1]==newPos[1]:
						if pos[1] in newOpened:
							continue
						newOpened=set(newOpened)
						newOpened.add(pos[1])
						newOpened=tuple(newOpened)
						newRate+=d[pos[1]][0]

					if (newPos, newRate) not in new or total > new[(newPos, newRate)][1]:
						new[(newPos, newRate)]=(newOpened, total)
		cur=new
		new={}
	print(minute, max(total for (pos, rate), (opened, total) in cur.items())) #1707

data=data2
main()

