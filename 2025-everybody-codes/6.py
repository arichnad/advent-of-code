#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
AABCBABCABCabcabcABCCBAACBCa
'''.strip('\n').splitlines()
data2='''
cBCcaABcbBBCBAbacAcAbBaBBBaBBcAAcCBAbcBCCaaAbCBBCcbaACCcABAAbcaABaaaBCAccCCabACbcabACbcAbbbcbbBBAABbaBabCCcaCaCCbCBaccBBAaACAAACCCbCacCBabAcbCacaBcBbBbCcaAcaCacBabcAAbACccAabCccCaCbbcAAbACBaaabbacCCBabbABbACccaaaaaAAcbaBaacaAAcCaBcCccBabBAcbcacBCbabBabacAacaACcccaAAcBCaBaaaABaCaCCbCcabCacaCBcCBabbccCCBccAcbBBcabCCCBbBCbABbCCAbcBbCCCbBccCBbcCcCAcCAcCBBbababCBBCaAABBBCaAABaCBcbbBaacaCaCCaBccBbbABaBbBBbCAbcAbcCBcccBacBbCCAAccaaCaAcaAaaABbcAcaCccBACCAbbbCBBCaaBACccbcbaAbBBCcbBbABbBCcCCaCBCAcccBCAcaBcAbcCabbbCAaBCCbAAcbBaAaaccAbCCBaBccCABcBccCacCCABBABcabbbbCBbbAaAaCcAabcAaAAAcAabCCCacccAcAcbbbAABaaaAAAbBCccCaABcabCBCBbBcaBabaAbbBbbaBABabAccBACbCCaBaBCCABAAcaAcCcBCBABBABacAaACcBbcACCbaBbcacCCaABCAaaCaBbaBCACabCACbbCaBBBbcAaAAcbbbabBabBcCBBbbaBbacBAcBcacAabBBCBBbaCAAaBaacAbbcaBBCaBbaCAacbCCccCAaBbCcBBbABCBBcbCcABccCBCBBBcCCAabcbbAAcCCCaCBcccBaCBcaCabCaBBABCcbBBaCBBAAabCcCcaACBbcbbBbaaccCaAbCAAaCbcaCBbBbABACbacBCABAACaABBAcbCbaACbcBccbaAccAacaAAABAacacBaCBabcACccAcBcaabcCAABaBAcbcABAcAbacbBacbcaaCCBbcbBbAAcCAAABcABCbaaAbacacbbaaAabbcABABaCBbCcabaAbaabaAbAccACBcBBaACcAbBCaAbcacbcbCBcBbaBbccCAbACBbBBabccBABcBAcCbcabacBaCaaCAaCcAbAbCbABCAaaBBAaAcCbababbcAcaAcbacCAAaBBACAAaAaacBaAABCBCACbbacaBbcbBacacAACaBbCcABCacbAbcabcBaBccbCcAbCaCbcAbaabacCAACAAACBbaCBAcccaabACcbaCbACcCaACAacbCbAccBBbccAAcBaAcCCBbccAccacCacCCcBCCabBBbCAAcacACBAbcaaCbCaCabcCCBACBCBBaBabaBbBBaCCBbbBcACabCbBaacABBBaCAcBCbAacBaacCaCAcCcBbaCbBbbcaBaccABbBbbAbCABAaAcCAAAbbacacbBAacAAbACacbbbABaAbbBAABcccbBCbaaAAbCBbCBabCCAAbBBcBbBcBcccACbBbCBcbAacbccBaACbCacAaBBAaCCCbacaBacaCCcBABBbCcaAcBAcBBBabAaBcbAaaCCcCcAaBcCcAabaaacACcBaCAbAabbcCCCbBCbbCBaaAACbabacCCBCacbabAaCAbcBcbbbcCCCAbcaBcBbaCAABBCBCAbAACCabcccBCCCcACaaCabCBaccaccaaacabbcbbAabAAaAbCBccbACCcABBBaccCCAcBbBCBcabbbABbbbAAaaaAcaCBcacBBACACbAcaaaABAbcAaBBCCBbCbCcBbBcbABAbBCcBAcCCCbbaACACbCaBBCbABbccbCCAabbbBCCbbbBCaBCACbcbcbbCBBCAAAcBbaCacbcBcbCCcCBAabBCbCAccBBcbAbBcCACBAACBCBCacaAcAacCaBBbAbbAbccCCBbcCBBBaBaCBBaCAcbCcaabCCbCBcbbabcbbaAAAABCbAbBACccACBCcCBAcaAAcBabBbaaccCaCbAaCAaCBcaaAcCBBBABaCcaCbbBAAcBaaBcBaAcaCbbAcabBbaAAaAAaaAaaCaAbbaABBcACcaAcabbAcaCacCBccbcBcbBcaABccAbcabbcbbcABbCbbaBCBCCbabbababAAcCcBCCbaaACbBaAAbbabBaBcCcCcccbBabCbabBBbcAccBACbCBbAaaabaBbABCAcCBcbCacbBbCbBCabACCcacbABabcbCcBCcBAAAabaabCBbACBCAcbCbacAcAabBABbCCaCcaCCabbBcacCBccCbAaCACBBbcbbabABababbCaBBBbcCbBbbccBbcAaBAbbABAcCaBbccAbCaCacBaBcccABBBCBcAcCAaCbaABCbbCAbabBBAcabacCbBACCAaBAaBcaCcaBacCcacAcbcCABCBCabABAacCcCAbbcAbaCbAacCbBacaCaBbCCAaBbCccAaBbccbCCACbCCCCAAACcbbccCaCBaBBAbCBCBBabbBbaCAbBBacBBaaAbCBcabBcbAbcBbBcCCacaABBaabCccBaaCAbAabCAbccbCBAbcAbAcABabbAABbbBaaCaAaBaaacAaBbacbACCABCbCCACbBaacCbCACbacaBbaCABAcAcBBBCCCABCACBCCBBbCbAABcBCabCcaAcbCacCcBbbcaAaaBBCaBAbCacBbACabAaCAAbCcccBACbcAabcAbaacaCCCbBbbaabBBabBbBaCbcCCabBcccbCcccbCCaAaCCcBcBaACCcbcABCaAAcacBccaCcbcbacBabbccbcCcaCCbbaCacCcccCcaBcCacAacbACbCaBccBAbAacBbCCbCaAacCabCabbAbCbbCAcabBACBbcBBBAbabbbAbBCcCcBBcaABBbcbAbaaCBcbCABccCbaBbBccBbacBCBCaACbaBaBCBCBcCcbbCaAbCcACAaCABCbABaCCAbbAbCbbcbaabbCBBAbbCBBCBcbbAbBBACccCCaBAacbCcBCAacCbbBAabBbAcAbbBBCbBcACBCCbACcBCcCBbbcCABaBbCAcAABaBbBabCAAABbcbBBBabBcaacbCCAaBbCAacaCbacBaCBccBabCCaACbcbcaBaBCcbcBCcbaBaaBbbACAcaBBCCaBBBAcBccbBCBcbbbAacAACCBcAcabCAaCcBbacAACbCcbbACCcBACBaAcAbAAaCAcAbAcbABbCbCcBcBcAaaCCaAaabcccccaaCAcaaCcABAaCBAcbABCACBaCCAAAAcAbaBcBccCBcBcbaBbbAabABacacaBBABcCcBAcCBaabBBbbAAACbAbbCACaccbbACaBacABCcabCcaCbCaBBbcBCbcAaAaCaCBBBABCcbbAaCBcCbbCaBbaCaBcbbcCaabbbCAabcbAcbAbbBbcCcAacabaBcAbcbAAAaACcbBAACBbbcbcAcAAbcbBccCCABabAaCcCaaaBcBBaBaBabcCCCAabBabABccBBcCCCbcCbbBccbccCcCAbbCCcaaaaCBcAcABaBbcbBAbbbABcBBAABBcaCbccaACaaAaaaCcBAaAaCbaAaCbbCABCCAAaAABabBABBababaABcaaCbCbbACccBcbCAbBcaACbaaCBCABaABaABbCcbAAccbBBbcCBbbaAcBAbBCcbbAccCAAAbABBAbBacBCCbACbBBcCCaAAcccaCAcAcAcACCCcbcBAbBBCcAaacBbaACacbBacBcacAcaBcbACABBCCcCBAcBAbcAaBCccaaBBaBBabCBbcAaaAbBbbAacBBABaaCAabaBbcBAbAaCbCBbCAabCbBBBcBcacCbaCCABBBcacAcCAAABbABacCAbBaabcaAaCCcABcbCABbcBbbAccCCBaAbaaccAbCcBcBbAABAaCaAACABcAcBbaBAAbaACbaccBbaBAcccacCaaBAbcbbAccacaAbBBaAAbBCcaaCaCaBAcCBcBccCCAaCaCaCABbAbcAbaAcaBAcCaBbbAabcbBACBCcbbBAabAABCcbbbBCbAbAABcBBBaABCcAcbAaBaBccacAAaacAcBBCBBbaBbabCBCcBBbbBCCBbbcaACAabaaAAbccbBAaAbcbaBbABCcCacabCABCBAcBABcaABcAaBbaAAcccabcbACBACbaBCAcbcCAbABcabCbAaCabBcBaBAABcCcAcCBaAbCBBaABcCABBCBBacAbBbcaAbBBaBCbbacabaAABacaBAACCAcaCcBCCaAaccBabcCCCcbAcBBaabaAaCaBCACccbacacACBAabBcCaabaaabaabccBabbACaAbBCbcABBBCBcbcCccCaaaaCcbCbabbbABcAbCbbaBcaCcbBCaccAccBBAbBcAcCBBaAAAacACAcaaACBBbbCCcabaaaaBCbbbaaaaCBCbCcAbABbacabbCcBBcCCbcBACACBABccbCCcabacaCCbcaABaBccBAbbACaCaABccccCCBccCacBcBCBcCAbCcbcbbBCAaaacCcaaabCabBbBcbAaaBCcaAbaBCaAAcBBAbBcBcaBcBCCaCCBacAaCbCBbaAcCaaaaaCbccbacccacAcACaAcBCBcCCBbCbcbaABAaBcCbacbAaCcbbcccaacCCCCaCcABCCcBCBCcABbcbaACBCBAbCAcAcaBaACaBbcBbBbBbaaCCAAcaBacBBccbBbBcaAABAAcbCcBCBaCacccaAccCCbACaAbbbaCcCaababbabaaabACAbCBAaBacAaCcCBbCaaccAcaaAAccacCCAAccbAaBBCCABABACaBAACcCBBBAcBaccCcccCCcabbabbBbBCabAcabAbCbACCCaAcbabAacaCbaAcCaBCCcBCCaaACCAaccCcAbBBacbAaaCCbcCcaABbAcBbABbAcabbAcAbAaCaBcbaCCbCBBCaBcCaaaABbbbaCBaBBBaBbccAAbABAcaaACCCcCAabaABCCCbaBbAaCAcbbccbABbbCbbcACACCcAACCAAAAbCacBCBaBACbccACbCBaBaBAcaCaAAbaAaacbAbAcCBCCbCAaabAbaacBbAACAAbbacbBbAbBcaBcBAabaAAaABaCcaCBabCCacacBbCBaAbaBBCCAAcbaABCcCAAcabAaCcAcBBcCbaCBcBCBcBbAbbcCAaCAaCBCBAcBcCBcBABcCCACbCCcBBbbaBCAaCAaBAbbCACBAacAbCCCbAacbbbcBaaABcBBbBaCcabBbACcBaCcBbcBBCcBCBBCbBCbbAbBcaaBbBabBbACCaCbABACbCabCBaCcbaacABCAcaABBBBacCcBCBAccCBaaaAccBCabBACCCcCCAcACCCcAbaabBbaaaAAccaBcbbACbccAababaAbcCCCbACBaBaAcCaaABBaccacbAAaAcBaacabccBBCAaAcaccAAbBBCBCccAcBbcAaBabAABbbaaBcbCCBbaCABcbAAaaACBaabCBABCABaCbAAAccaBCaBbbcBcCABAbAbaAABBbcbBcCbbBBCBCaBAccbcBBCCbBBaBbaaCBaBabBcBBBaaBacaAacBcCbaabACbbaaCacbcCbBbACbcCAaBaaABAabCbccbbbAaAABbBCcCACABAaBacbBBBbCcAABBACababbCBBbAcbAAAabbACAccBacAAACcACcaCbBbBcAaaAACAcbbAaCaBbABbCCAAcacCBBBacaCACAccAAaCBBcBBcbABbAbbcAABCbcACCCBAaAAbcBbccaCacAbbabcBBAbCccBAaCCCbCcCCBbabcBaCAACbcbCbcCabABbAaaBbbbbBccAcaACacaAcCcbBcBcaBAABaCBCbcCCcCaBccCcAAAaABBcbcaAaaabaCabAbaBBbCCbBaCCBbaAAAcbBBccAaAabBCCbbaabBcaAAbbCcCcaBCAAaaaabcCABcAcCaaCbcbbCcacccAAcCBbCABbbAabcbABaaabABBbBAaAAcBbAcCbbaCacBAAaABcCbaBcCCbaAacbCbbBbbCccbcbaAAAcbCCbcBCbBbacAaBCCbCAcbbacBbbcBAABCabaAbcbABabAabAbCbbcccacAaCcccACbaaaBBcBccBcAacAaCBaCBaBBbAacCBCBBaCCaBaABCABBccbcBAAcaAaaCaCAaBaCAcbcCacCBBcabaCacBaCaBaBCACaaacBAbccccacBAacbCaccCCBacbbBAabBCbCAAcBCCabAccabBccaBcBBCacbcbaACaAbaaCbcbaCBBCaBBcBcBABBbcbAcBabcBccbcbBaCCBbbaACcBBbcBbCBacBAacBaCCBBbABAcbaAabcBaBBaCaCccACacCAaABAcBbcABBBacbBAcbBACabbbCbCCacbaACBAAACBcbBBcAbCAbBAABBcBabCBcAbcAbBACaaAaAabAaAcbACcACbbcBbbaaaCaAcbBBBBbcabABABaAaCCBccBCaAbBAcbCBBBaACBaBACCACbAaaAabABbcBCAabcBAbacaaaABCCCBcCaaCCBbcBabCCABbbbbBBbACBabaCaACCbAabCbbBaAbCAbaaCbCbCbCAcaAcaACCBacaAacACbcbbbCABcbabbaAbbAAABCcacbBCcbcABbcaCaBACAcBbAccABCaBbABBCbBbcBcbbBCAAbbaABaAaBbBabbcBaAcBbAbAaacbccbaBabCCBBBaBBCBCaAcBBbCABBcbAaAcCBBBACABAbababBbcacCcbBCaacaAbBAcbCBbbaABbAaaCCCCAaBcbabAcABcbcABABcBcCbAacAbbbCBaACCCAcaCcBACAACBBACBbcccCccacCcABacbaBbCAcBcACBBBAcAcBaBCcCCBACbAaBACAaCCAcBaACCBCBcABCbaAaBAcCabcBCcCaaBabbbBAABBCcCbcabBababbcCCCAbccbCCCaBAAbaABAABbcbABcAAAAcBCaaCBBbaAabBbBcCCBCcBAaBBCBAccABAAABBbBAaCAACacaBABcBccbaAAACCbbaabacCAcCcBaACBbBAcBacacCCAbBbBaAACBBCBCaAaCaaCBbCbBBaBaBCBacCcaCCBcBccBcbaACBbcbcAccccBcBbcbbBAccAcbACABCacCBcBabCcbbCcCccCBAbACCBbcccABABabbaCaCABBccCbBCbaCaCbAbCCbaCBcaAcBcccbBAbBAAbCbCcBcBacccbBBcAbcbAAabCCccacBBACBCBbaCaaAbCAaBAcccCBBBcCaCabcBaaBbbcaBcaBcAABcaBBCcAaAaaaBccbCAaCCAcbBABaBbaaaACCbbAaAaabAaccCbbbcaBaCcBaAcCcbCcacbcbcaAaAAACcbccCabCcAccBBAaaAcBbBBcACBaaBAbbAbcacbCaAaAcaAaAcCbcbaCaAAAAAcCACccaBbAABCcBCBCABbBAbBBbcccCAaAcAbCCabcABabAcACbCCAaCBaCBCcaCCACAcBAcbCbbcABBbBBACCbcCBBbcCcCacBBabBABAaAbBacaaccbBcBaACbCACaABBbCCAccbCcCcaAbbabAAbaCbCcBaCcCbBCbBCBccABbBCbBaaBcBcBcCbBcbbaccAcACCbcBABaaabCbcBcACaabcbcbAbCAACBBCccBCAAcbcAcBBACaABbaACaBaaBCCabAbbcAbbbBAcCaBAbbabaABBbCaBbacAcaCBaABcbcCaaAAbcCABcAaABbaabbbCBABcBBABCaababbCCBBbaAbACcbaAAbcACcbCcBcBbabbBcBcCaBCAabcBBCBCaBcaCcbcABbCBCCaCCaccCABaCacCbBbBaCCCBCAcCAaCabBCcCCBAcaACbcaCbCACcaBbAAaBcBBBbbAbbcaaAAAbAabacAabAbaCabCBcAbBCcAcBaBcbbacCCabACBbAbBBAABccBCCcBBccAbABcaaBBAcBcbBcabacAaCaaccbBcCBBcBbccBCaABaababBacAbCCAaCabCCBcABbABAAaCcbccAbcAcBBaaACcBbbCabAaccCACbBAbBabCCaAAcCAbCBBcaBaAcbaaAbBbABabcaCCaBACAAcCBABCccCcbCbabbaCCCbaBCBCbcBBbaCaBCBbAaBbcbBbacCBAcbbabAcBacBbBAAAABCCbbBacaBABCCCCAcCABBaacABCBCACabbAcCbababAcCbccaCaCcAcCCbaabCBcccbBaacaABCBccbcaCAcBbaCBaACaBBABaAaaACBbabABbcCacBbCcCbBaABacCBCbcCbbCccABAaaBbcaBAaBaAAAcBAcbaBbACbcAcCAABCbBACBaAbbBCBAbaaACbaBaBcABabaaAaaccCBBcBBBaacBccAabaCbcbaBBbcCBCCbAABcbcAAaaCaaaCbBbBBaCBAabbABAAcAcAcAaaCBacCbbABCCCaaaaaBBBAcCCCbAbAbCbCCbbAcbccCcabCcabBaaccBbCcAbcbAcCAabaBAcCABcACbCABacAbaBBAcacCcaBbaCCbbcBCCAAbbaabbBCcBaCCCaCBaBACcbccacbAbcAbbCacbAbBCCcCbAAbbBCCBaBcbBbcaCBbaCcabcBCAACCacccbCBabacaCbCbcBcbBAAcAaCCcAbaAcabaBCcCbACbababcCBAAbaaaBbCabBAABbaCabaBBBabaBCCacaBCBBcBAacbccBbccaABcCabbbacBBaCAacBAbbCCcabbBcBbbBBbcbaCCAAACBcAaAAAbAcBCCbCCCaaBcbbCCcBAaCbAAcbacBBBCcCCabBabCcAabcCAcAcBccbCBbcbaabbaabBccCcBCBBBBAabBbcbACabCcaACabcbBcbBcBbCacccaACACabBBcbbacbCABbCABacAacbBcAACcCCbBCCbbaCAcAabacbACcbabBBbBAbABbacCAACbAbCAcbcaAabaBCAcAaaCcCBccbaCcbbAAcCAcbCcBBBcbBBCACBabBbcCcCAacCcbACABbBBCCCACBcAACbBCBABacbbBcBabBACbAbcAcaBcaaBaaBcbBaAbaCbcBCacCaCbbBcBBAbaccCCbbaBcAcBAbBacbCbCCCCAbCbBAcbbbCabbBCCcbCaACBACcACBaaACBbbccCACACbCAABbAABbBcAaCBcacBAaBACbacbcBABcAcCaBAbbAcACbbCCABABcaAbcCaCaCcAcAcbBbacbabAAaBcbCbcaAcbACCcCbcbcCaABBCaACaBBbbcAACBCAccBbbcBCAACbabaCcbBcAacccAacCCBCBcbcCaBbcCCcbaBACBbbACBCbCBAbacccAACCCCCaaBBcbBbAcaBbBcCbCCbaAaACBBABAABcbcBBCaaABCcabcBCbbcCBCBCCaBBAaCabaCcBbBBabACaCaACcAcCbCcaBbbccbBBacbbCbABACACBaaBaBcabbCcabBCcbaAccbBcACBaBCccaBCbcbBcABaaaacAaAAbbAccCaBbaBaCAAACAaCabCCCACCCBCbBbACabbBbCcAAaacaCAaAcCccaCAbbcaaCBaCCacbCccCaaCcCCbCbBCabbAbACbcBAACbABBBabBbaabACAcabbcAbACabACabbacBCBbcBAacbccCCAACCABCaabBAcACAbCBBaCaABaCcBbABCCBCbabbBcABcCbCcaBcBbCCCaBBcaAAcccbBCCAAaCCCBcCbBcCBacaBaBcAACAabbBAbACbCCCAcaBAaabCaBbBabcccBBbAbAbbbBBBaacBcAAcAcaAcBCACccAcCbBcaCcaacbCaBcAbaacACBABaACBBCBcaCBcCBAaaCaaAbC
'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() #does not run in parallel on separate cores

# mentor = 0
# answer = 0
# for ch in data[0]:
#     if ch=='a':
#         answer+=mentor
#     elif ch=='A':
#         mentor+=1
# print(answer)

# answer = 0
# ma,mb,mc=0,0,0
# for ch in data[0]:
#     if ch=='a':
#         answer+=ma
#     elif ch=='A':
#         ma+=1
#     elif ch=='b':
#         answer+=mb
#     elif ch=='B':
#         mb+=1
#     elif ch=='c':
#         answer+=mc
#     elif ch=='C':
#         mc+=1
# print(answer)

answer = 0
ma,mb,mc=[],[],[]
na,nb,nc=[],[],[]
for i, ch in enumerate(data[0] * 1000):
    while len(ma)>0 and i-ma[0]>1000:
        ma.pop(0)
    while len(mb)>0 and i-mb[0]>1000:
        mb.pop(0)
    while len(mc)>0 and i-mc[0]>1000:
        mc.pop(0)
    while len(na)>0 and i-na[0]>1000:
        na.pop(0)
    while len(nb)>0 and i-nb[0]>1000:
        nb.pop(0)
    while len(nc)>0 and i-nc[0]>1000:
        nc.pop(0)
    if ch=='a':
        answer+=len(ma)
        na.append(i)
    elif ch=='A':
        answer+=len(na)
        ma.append(i)
    elif ch=='b':
        answer+=len(mb)
        nb.append(i)
    elif ch=='B':
        answer+=len(nb)
        mb.append(i)
    elif ch=='c':
        answer+=len(mc)
        nc.append(i)
    elif ch=='C':
        answer+=len(nc)
        mc.append(i)
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

# bfs
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	newPositions = []
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(x, y)] = cost
#
# 		newPositions.append((cost + 1, x + 1, y))
# 		newPositions.append((cost + 1, x - 1, y))
# 		newPositions.append((cost + 1, x, y - 1))
# 		newPositions.append((cost + 1, x, y + 1))
# 	positions=newPositions
# print(costs[(endX, endY)])


# dijkstra’s
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	(cost, x, y) = heapq.heappop(positions)
# 	if y<0 or y>=H or x<0 or x>=W: continue
# 	if data[y][x]=='#': continue
# 	if (x, y) in costs and cost >= costs[(x, y)]: continue
# 	costs[(x, y)] = cost
#
# 	for (cost, x, y) in ((cost + 1, x + 1, y), (cost + 1, x - 1, y), (cost + 1, x, y - 1), (cost + 1, x, y + 1)):
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue
# 		heapq.heappush(positions, (cost, x, y))
# print(costs[(endX, endY)])

# # flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# visited=set()
# def ff(x, y):
# 	if y<0 or x<0 or y>=H or x>=W: return
# 	if data[y][x] == '#' or (x, y) in visited: return
# 	visited.add((x, y))
# 	ff(x + 1, y)
# 	ff(x - 1, y)
# 	ff(x, y + 1)
# 	ff(x, y - 1)
#
# ff(startX, startY)
