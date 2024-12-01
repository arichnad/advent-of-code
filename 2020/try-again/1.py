#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading, numpy
#sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
# sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
1721
979
366
299
675
1456
'''.strip('\n').splitlines()
data2='''
1742
1763
1238
1424
1736
1903
1580
1847
1860
1933
1779
1901
1984
1861
1769
1896
1428
2010
1673
1491
1996
1746
1973
1696
1616
2006
1890
1600
1991
1724
1804
1794
462
1706
2002
1939
1834
1312
1943
1465
1405
1459
1659
1288
1241
1935
1294
1388
1772
1945
1649
813
1956
1274
1686
1404
1770
1631
1366
1321
1353
1685
1365
1738
1911
1235
1495
1837
1456
1283
1929
1326
1735
1604
1223
1261
1844
1850
1429
277
1848
1818
1395
1522
1863
1475
1562
1351
1538
1313
1416
1690
1539
1338
1982
1297
1821
780
1859
1420
1934
1303
1731
1714
1702
1417
1872
1998
1908
1957
1270
1359
1760
1997
1773
2000
1203
1880
1955
1273
1775
1893
1237
1707
1885
1900
1801
1367
1561
1524
1678
1511
1623
1464
1477
1733
1423
1575
1851
2007
1651
804
1836
1849
1713
1401
1502
1806
1506
1646
1968
1253
1889
1759
1734
1611
1558
1256
1657
1778
1953
1578
1717
1498
1381
1919
1512
1391
384
1802
1573
1940
1323
2003
1689
1936
1368
1962
1964
1586
1619
1482
1445
372
1792
96
1468
1999
1301
1757
1613
1807
1941
1642
1557
1884
1626
489
1989
1327
'''.strip('\n').splitlines()

data=data2

data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)


# for line in data:
#     for line2 in data:
#         if line + line2 == 2020: print(line*line2)

for line in data:
    for line2 in data:
        for line3 in data:
            if line + line2 + line3 == 2020:
                print(line*line2*line3)
                sys.exit(0)

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

