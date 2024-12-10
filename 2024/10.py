#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''.strip('\n').splitlines()
data2='''
101234653436698943210876543298108967890123211
900945762567787651028945054167211876965254300
812876851008632112987632167054340105874367891
743987945219541003456542108981233234567809892
657641434349898764565876232190543456452912763
898530125896701651698965945087612387301103454
101421056787672340789234876231201293219010989
012336765410589121470125960140340184678321670
987449870323431034561076054057653296501234521
876558901210120345665780143968934187410345438
034569821025001256676891232877065056309654589
125678438136789867589872301986174145218789678
678776569245234798434565432765289036785890541
589989478910135652329806567874376123896781030
431276321210023101210715432990145678765432121
120345290923412302345620121087230109650187656
098010187874503210989430101256521212341090347
187623456365694567876543232344560301032181298
012510589456787655469854741023478912345672107
143421674307897846988767858910890109852109856
231256014210978987671056967378765210763296705
140347123900389034502340191269854307894585014
051298034891276123216521780350123456765674323
565434540762345637897435615443210523456001298
876529651057850136988904306782107610987123367
985018782348943245077211216790108901278994453
123427890167654432106310345889299870122185432
010568921211234501215445432976387761233076541
129877432100235676301456701265456654394567650
431066523231145985490389876014012534585658969
302309012694046796781201078923453421673215678
213218906783459873212212562112969010984504301
304567815612163654304323453007878123435643210
412359854309072345323456894314365036521754965
563456743218781896210567765101254307810867874
694105678907690787890698989210345218987980123
787234563210581654321787876307896210898943321
894563454671410010987345665456987346787652450
763674589582323225676298767645459855898101067
652983673497654134570156958912378764306678998
341672102108987010987667843003569013215463210
030501012896109823478766542103454320176354501
125418923787210734569651033212169010083296101
654327654654323601234569124349078321190187632
789210125345434512103678765678767456783276543
'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\\d]+', line)] for line in data]
data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)
seen = [[0 for i in range(W)] for j in range(H)]

# for j in range(H):
# 	for i in range(W):
# 		if data[j][i] == 9: seen[j][i].add((j, i))
#
# answer=0
# for k in reversed(range(10)):
# 	for j in range(H):
# 		for i in range(W):
# 			if data[j][i]==k:
# 				for dy in range(-1, 2):
# 					for dx in range(-1, 2):
# 						if dx == 0 and dy == 0 or dx != 0 and dy != 0: continue
#
# 						newY,newX=j+dy,i+dx
# 						if newY<0 or newX<0 or newY>=H or newX>=W: continue
# 						if data[newY][newX] != data[j][i] - 1: continue
#
# 						for w in seen[j][i]: seen[newY][newX].add(w)
#
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i] == 0:
# 			answer += len(seen[j][i])
# print(answer)

for j in range(H):
	for i in range(W):
		if data[j][i] == 9: seen[j][i] = 1

answer=0
for k in reversed(range(10)):
	for j in range(H):
		for i in range(W):
			if data[j][i]==k:
				if seen[j][i]>0:
					for dy in range(-1, 2):
						for dx in range(-1, 2):
							if dx == 0 and dy == 0 or dx != 0 and dy != 0: continue

							newY,newX=j+dy,i+dx
							if newY<0 or newX<0 or newY>=H or newX>=W: continue
							if data[newY][newX] != data[j][i] - 1: continue

							seen[newY][newX] += seen[j][i]

for j in range(H):
	for i in range(W):
		if data[j][i] == 0:
			answer += seen[j][i]
print(answer)


#dir = (dir+4)%4
#dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = 'rdlu'.find(d.lower()) #clockwise, starting right
#dir = ['right', 'down', 'left', 'up'].index(d.lower()) #clockwise, starting right
#dir = '>v<^'.find(d.lower()) #clockwise, starting right

#data = [[column for column in line] for line in data]
#for j in range(H):
#	for i in range(W):
#		for dy in range(-1, 2):
#			for dx in range(-1, 2):
#				#if dx==0 and dy==0: continue
#				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
#				newY,newX=j+dy,i+dx
#				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
#for line in data: print(''.join(line))

