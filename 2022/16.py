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
Valve DJ has flow rate=0; tunnels lead to valves ZH, AA
Valve LP has flow rate=0; tunnels lead to valves AA, EE
Valve GT has flow rate=0; tunnels lead to valves FJ, AW
Valve RO has flow rate=5; tunnels lead to valves NO, FD, QV, BV
Valve PS has flow rate=0; tunnels lead to valves FY, UV
Valve QV has flow rate=0; tunnels lead to valves EB, RO
Valve MV has flow rate=0; tunnels lead to valves FL, EB
Valve RN has flow rate=0; tunnels lead to valves AW, LQ
Valve HF has flow rate=0; tunnels lead to valves QN, HW
Valve PY has flow rate=19; tunnel leads to valve SN
Valve AT has flow rate=0; tunnels lead to valves YQ, UY
Valve UY has flow rate=3; tunnels lead to valves KV, ID, AT, PB, PG
Valve YI has flow rate=0; tunnels lead to valves FL, FD
Valve EB has flow rate=8; tunnels lead to valves MV, GQ, QV
Valve ID has flow rate=0; tunnels lead to valves NO, UY
Valve FY has flow rate=15; tunnels lead to valves LQ, PS
Valve GQ has flow rate=0; tunnels lead to valves EB, KM
Valve HW has flow rate=0; tunnels lead to valves FJ, HF
Valve CQ has flow rate=17; tunnels lead to valves KM, GO
Valve AW has flow rate=20; tunnels lead to valves RN, GT, WH, MX
Valve BV has flow rate=0; tunnels lead to valves RO, ZH
Valve PB has flow rate=0; tunnels lead to valves UY, AA
Valve MX has flow rate=0; tunnels lead to valves AW, YG
Valve DE has flow rate=4; tunnels lead to valves MM, PZ, PG, DS, EP
Valve AA has flow rate=0; tunnels lead to valves EP, PB, LP, JT, DJ
Valve QN has flow rate=23; tunnels lead to valves SN, HF
Valve GO has flow rate=0; tunnels lead to valves CQ, MK
Valve PZ has flow rate=0; tunnels lead to valves IJ, DE
Valve PG has flow rate=0; tunnels lead to valves UY, DE
Valve FL has flow rate=18; tunnels lead to valves MV, YI
Valve DS has flow rate=0; tunnels lead to valves DE, ZH
Valve ZH has flow rate=11; tunnels lead to valves YQ, BV, DJ, DS, SB
Valve KV has flow rate=0; tunnels lead to valves UY, IJ
Valve UV has flow rate=9; tunnels lead to valves MM, PS, YG
Valve WH has flow rate=0; tunnels lead to valves JT, AW
Valve FD has flow rate=0; tunnels lead to valves YI, RO
Valve FJ has flow rate=24; tunnels lead to valves HW, GT
Valve JT has flow rate=0; tunnels lead to valves AA, WH
Valve SN has flow rate=0; tunnels lead to valves PY, QN
Valve KM has flow rate=0; tunnels lead to valves GQ, CQ
Valve LQ has flow rate=0; tunnels lead to valves RN, FY
Valve NO has flow rate=0; tunnels lead to valves ID, RO
Valve SB has flow rate=0; tunnels lead to valves ZH, IJ
Valve MK has flow rate=25; tunnel leads to valve GO
Valve YG has flow rate=0; tunnels lead to valves MX, UV
Valve IJ has flow rate=16; tunnels lead to valves EE, KV, PZ, SB
Valve EP has flow rate=0; tunnels lead to valves AA, DE
Valve MM has flow rate=0; tunnels lead to valves UV, DE
Valve YQ has flow rate=0; tunnels lead to valves AT, ZH
Valve EE has flow rate=0; tunnels lead to valves LP, IJ
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

