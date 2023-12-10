#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''.strip('\n').splitlines()
data1='''
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
'''.strip('\n').splitlines()
data1='''
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
'''.strip('\n').splitlines()
data2='''
FF-7F-7.|FJ7L-7-.FL-F7|-7FFF77J.|7F--J-FF7-L..-7FF-LF7F|-F|7-L-FLJ7-FF-JFF-7-7.-J-.--7.-F---FJ-|..-J7.|J-77-F7---77FFLJ7.LFJF7.FL|-J--7-LJ-|
J.-L-JF-L7J|LL|7FL7LL||.LJ--J7JFL|J7|7.JLJ|L-L7L7-7J|L7|L||..|7L.L7.FL7-L--L-JLJ..FLJ|F7L|7-JJ-LLLJJLF..F77FLJ7FF7-L7|-L7-|7|.FFJJJ7L-LJ|..J
||..L7.LL-7J-.F77F7JF|--L.|7LJ-J.L-FF7J...|||JFJLJ7.L-L77L|.7.||7-J7J7LFJ.7F||-|.7LL77.JLJJ7|F|F|..F.|.FLLL-.---F-7.F7J.7-JLL7--77.|FFJ.7F7J
F-7J.L-7LFJJ7.LF-F77.|LFLFFJ|JJL7JLL|JLF--7J7-L.|FJ.LF-J--L-|.L7LL|7.-J|L|--F7JL7L.LLJFL-J7.77-7777F-F7F7F-J7F|.J|L7L|LFJLJ7L77|-|77-F-F-7L|
.-7||7J7.JJFF-.|FJ|.LL.J.|LFJ.L-LJFFL7FJF-J|F7|-77J.F7LF-F|77-F|7..F-JFL.J|||7.FFJ.FJFFJLJ7FLJJ||FF7FJL--7J.||-FL-JL-JFL.LJ|J.L.|.L777|.FL77
JJ.J-L-77.L||L7|LJF-7|F.FJ7|L-7LL7..LFJFJF7FJ|F--777F7JJJLF7--JJ.F.FL-|7-LFFJL7LJ..J-JL7F7L|7|-7-J|LJF-7FJ-F7J|LFJF7|.|FJ.FL7FF|-F.J7---7LFJ
LLL|.FLJF-7LJ|J||...LJJ-7JF|.||.LJ.FFL7|-|||FJL-7L--JL777..L-77--JF|J7L7.7.J7FLJ|L77F|-FF77||F7JL-L-7L7LJJJL77F|JF|||F|-|F|7.F7JL|F-FJ|LL--7
F|||FFJ7|7--|-7JF7-FJ||-F7JJ--7F|FF7LFJ|FJLJL7F7|F--7FJF|.J|F--7L-7.|LFJL..|L||JJ7|--L-FJL77.F|7F7F-JFJ.LJJ.L-|7-FLLJ||7|L77F-JF77J-|-F-L-7J
L-L7-|7LFL.L|J.|L-7F77-.7J..||77|--F7L7|L7F7FJ|LJL7LLJJ7|FL--|FL-FFF7J||JF-J7L7JL|J|.||L7FJJ7LFF7-L7FJLF..|F-JJ|LJJFLF-7J.J.77FJLF..FJFJ.F-.
FL|LJL|7L7F-||.FJLLJ||-7JF7-|JL|JF7||J||LLJ||FJF7FJ-F7FF--7|7.|.--FJ|F7|F7-F-F-7.F7F-F-7|L7LFF-J|7|||F7F77F7.|L7.|FL-|||LF|L77L--LL7.-JLJ-.|
|L|7F-F-.J7-FJ-L-.F|J77|F7|-J7|LF7FJL-J|F7FJ|L-J||F-JL7L-7|F77L7JLL7LJ|FJL777L7L7JFF7L7|L7|F7L7FJF7||||||FJL77.L---J.L7|.F|JFJ..77L77-L.|L7.
|L|L-7L---JFJ|L-|7FL7|LJL|JJ|F7J||L---7||||FJF7FJLJF7FJF-J||L7-|FF7L-7||F-J.FJL7|F7||FJ|FJLJ|FJ|7|LJ||||||F-JF77.||LF7||-FFFL--|J7FL|F|LJF|7
-7-JJ|JFL.|JJF7-L7LJ7|-.-JJLFJL7||-F7FJLJ||L7||L7F-JLJ-|F7||FJ-F7|L7FJLJ|JF7F7FJLJ|||L7LJF--JL7L7L7FJ|LJLJL7FJ|F-7|.F7F7-FJ.F7-J-FL.LF7FLF-J
.L|J|LF-|-|.L-JFF7-L7J|.L|L-|F-J||FJ|L--7|L7LJ|FJL---7-LJ|||L-7|||FJL-7FJ-||||L--7||L7L-7L-7F7L7|J||||F----JL7||FJ77|LJ|F7|-7|LJLJJ7L|LJ|L|7
|||.7-|F|FL7FJ-|L.|7|---77-FJ|LFJ|L7|F--JL7L-7LJF----JF7FJ||F-J|LJL7F7|L-7||||F7L|LJFJF7|F-J||FJ|FJL-J|F7.F7FJ||L7F7L-7LJ|-JF7JLF-----|-F-7J
L|L-.-7-|L7.-.FJF-LLJ-.|F-7L7|FJFJ-||L-7F7L--JF-JF7F7J||L7||L7LL7F-J|LJF-J|||||L7L-7L-J|||F7||L7|L---7||L7||L7LJFJ||F-JF-J|J||F---7..FLJ|FLJ
.L7.FL|.7LF-|-JLLJLJ|7FFL7L-JLJFJF7|L-7LJL7F-7|F-JLJL7|L7|||FJF-JL77L-7L7L|LJ|L7|F7L--7||||LJL7||-F7FJLJFJ|L7|F-J.|||F7|F---JL7|F--7.F-7-77J
.FF7FFL7LL|J|FLFJ--|77L-FL----7L-J|L-7|7F7LJ-|||F----JL7||LJL7L7F-JF7FL7L7L-7L7|||L-7FJ|||L7F-J|L7||L--7L7L7LJL7F7||||LJ|F----JJJJ|J--7LFFL7
-J.FFJ-|F-J|L--|-|FLFL-.F7F--7|F7FJ-FJ|FJ|F-7||||F7-F-7||L7F-JFJ|F7||F7|FJF7L7LJ|L7FJL7LJ|FJ|F7L7|||F7|L7L-JF--J|||LJL7FJL---7|.L77--J|-JJL7
LLFJFJJ|-J-L7LFF-J-L|-FF||L-7|||LJF7L7LJFJL7||LJ||L7L7|||FJL7FJFJ|||LJ||L-JL7L-7L7|L-7L-7LJFJ|L7|LJ|||F7|F--JF--J|L-7FJL7F---JF7JLJ-|J.FFJF7
FLJ|LF7.|F7-|-FJ-7|.LF7FJL7J|||L7FJL7L7FJ-FJ|L7FJL7L7|||LJF-J|FJFJ|L7FJL---7L7F|FJ|F-JF7L7FJL|FJL-7||||LJL-7LL7F-JF-JL7FJL----JL-7J7LF--7.LJ
L--7.FJ-F--.F7LF---7-||L-7|FJLJFJL-7|FJ|F7L7L-JL7FJFJ|||F-JF-JL7L7|||L-7FF7|FJFJL-J|F7|L-JL7FJ|F7FJ||||F7F7L7FJL-7L--7||F-7F-----J7-F|7.J-J|
LJJJ--JFJ-|F|-7|F|.J7|L--JLJF-7L7F7||L7LJ|-L-7F-JL7||||||F7L-7FJFJ|FJF-JFJLJL7L7F7FJ||L--7FJL7LJ|L7|||||LJL-J|F-7|F-7|LJ|JLJ.F7JLJLFLL7.LJFJ
F|-7-|LF-FFJ|.7----.-L-7F7F7L7L7LJ|||||F-JF7FJ|LF7|L7|||||L77|L7L7|L7L-7L7F--JF||||FJL7F-J|F7|F-JFJ|||||F7F--JL7LJL7LJF7L7F--JL7LF-7.J7FJF|.
JJJ||.FFF7.FL-F7JLFL-F7LJ||L-J-L-7|||FJL7FJLJFJFJLJFJ||||L7L-JFJFJ|FJF-JFJL-7F7LJ|LJF-JL-7||LJL-7|FJ|||LJ||F---JF--JF-JL-JL--7FJ...|-7FF7FF|
.F-J.--7J|77..FF7-|.FJ|F7LJ7F7F7-||||L7FJL--7L7L--7|L|||L7|F--JF|FJ|FJF7L7F-J||LFJF-J.F--J|L-7F7LJ|FJLJF-J|L---7L--7L---7F7F-JL-7-JLLF-JLLF7
L7FLF-F--L-|FFL||JJ.L7|||F7FJLJL-J||L7||F7F-JFJF--JL7|LJFJ|L7F-7||FJL-J|FJL-7|L7L7L--7L--7L7FJ||F7||F--J7FJF---JF7FJF---J||L7F--JJL7L|F7.LL|
.L7FL-|||.|.FF.||F7.FJLJ|||L7F7F-7|L7LJ|||L-7L7L--7FJ|F-JJL7|L7|||L--7FJL7F-JL7|7|F--JF7.|FJL-JLJ|||L--7FJFJF--7||L7L---7||F||F7|FFL-F|J7.FJ
JL7|F-J7-J-F7JF|LJL7L--7||||LJLJF||7L-7LJ|F-JFJF--J|FJL7F7FJL7|LJ|F7FJ|F-J|F7FJL7||FF-JL7||F7F7F7|||F--JL7|LL-7|||FJF-7FJ|L-JLJL-7777F.|FL7|
L||L||F.F|.F7F7L--7L7FFJ|||F--7F-JL---JF-JL-7L7L--7||F-J||L7FJL7FJ||L7||F-J||L-7||L7L--7||||||||LJLJL--7L|L--7|||LJFJJLJL|F-7F---J.J-L-77-F7
FF7-F--777FJ|||F--JFJFJFJ|||F-JL------7|F7LFJFJF7FJLJ|F-J|FJ|F7|L7|L7||||F7|L-7||L7|F7FJLJLJ||||F7F-7F-JFJF-7||LJF-JF-7F7|L7|L77|LLJ.JLLJ.LF
|L77L-7L-7|FJ||L--7L7L7|FJLJL7F7-F7F7FJ||L7L7|FJ|L7F7LJF7|L7LJ|L7LJFJ|LJ||LJF-J|L7||||L---7FJ||LJ|L7LJF7L7L7LJL-7L-7|FJ|LJFJL7L77J..7|.LL77|
|7.F|||F7LJ|FJ|LF-JFJ|||L--7FJ||FJ||||FJ|FJFJ|L7L7LJ|F-JLJ7L7FJL|F-JFL-7|L7FJ-FJFJ|LJ|JF7FJL7||F-JFJF7||JL7L7F7FJF-J||FJF7L-7L7|-.-L|FJ-LJFJ
F77.F7LJL-7|L7L7L-7|JFJL7F7|L7||L7LJ||L7||FJFJFJFJ.FJL7F--7FJL-7|L7F7F7||FJL7FJFJ-|F-JFJ||F-J||L-7L7|LJ|F7|FJ|||FJF7|LJFJL-7L7LJJ.LLLJJFF7J|
||77||F---JL-JFJF-JL7L-7LJLJFJ||-L-7||FJ||L7|F|FJF7L7FJL-7|L7F-J|FJ||||||L-7|L7|F7||F7L7|||F7||F7|FJL-7||LJ|FJ||L-JLJF7L--7|FJ7LL|.|.|-7J|--
|L7F||L--7F--7L7L--7L77L---7L7|L---JLJL7|L7|L7||FJ|FJL7F7|L7|L7FJ|FJ|||||F7|L7|||||||L-J|||||||||||F-7|LJF-JL7LJF----J|F--JLJFF7JLLF|7.LL|.|
L7L-J|F7-LJF7|FJF--JFJF77F7|FJ|F----7F7|L7LJJ||LJFJL7LLJ|L7|L7||FJL7||||||||.LJ||||||7F-J|LJ|||||||L7||.FJF7FJF7L--7F7||F7F7F7||7.FLJLF-7LFJ
LL7F7LJ|F7FJLJL7L--7L7||FJLJL7LJFF7FJ|||FJF--JL-7L-7L--7L-J|FJLJL7FJLJ||LJ|L7F-J|LJ|L7|F7L7FJ|LJ|||FJ|L7L-JLJFJ|F7FJ||LJ|LJ||||L7-|J||.|L-L.
|FLJL7FJ||L--7FJ7F-JFJ||L---7|F7FJLJFJ||L7L7F7F-JF-JF--JF--JL--7.|L-7FJ||FJFJL-7L-7L7|||L7||FJLFJ||L7L-JF-7F7L7|||L-JL-7|F-J|LJFJJJF-.7-7|..
F7JF7|L-JL---JL--JF7L-JL--7FJLJ|L--7|FJ|FJLLJ||7FJF7L--7L--7F--JFJF-JL7L7L7L7LFJF-JJ||||FJ||L-7L7|L7L--7L7LJL-JLJL--7F-J||JFJF-JJFLF7F77L7-F
FF7|LJF7F----7F7F7|L7F--7FJL-7FJJF7LJL7LJFF--J|FJFJ|F-7||F-JL--7L7L7-|L7L7L7L7L7L--7||LJL-J|F-JFJL7L-7FJ7L---------7|L--JL7L7|F-----7-FL7|LF
FJLJF7|LJF---J|||||LLJF-JL-77|L--JL---JJF7L7F-JL7L7|L7LJFJF7F-7L7L7L7F-JFJ.L-J.|F--J||F----JL-7L7FJF-J|F------7F-7FJ|F---7L-JLJF----JJ|.F.7.
L--7||L7-L-7F7|||LJF7FJF7F7L7L--7F------J|FJ|FF7|FJL7L-7L7|||FJFJFJFJL7FJJF7F--JL--7LJL-7F7F-7L7|L7L-7|L-----7LJJLJFJL--7L-----JF-7-J.F7L-7J
LJFJ||FJF--J|LJ||F-JLJFJ||L7L---JL7F----7|L7L7|LJ|F7L7FJ-|||||FJFJFJ7FJL-7|LJF--7F-JFF7LLJ||FJFJ|FJF-J|F-----JF---7L7F7FJ|F7F7F7|FJ.|7LJ-LJ.
L-L7||L7L7F7|F-J|L7F-7|JLJFJF-7F--JL---7LJJ|FJ|F7LJL7|L-7LJ||LJ|L7L-7|F--JL-7|F-JL---J|F--J|L-JFJL7L7FJL------JF--JFJ||L-7|LJLJLJL77J-.JJ|-J
|7LLJL-JFJ|LJL-7|LLJF||F-7L-J-||LF-----JF7FJL7||L7F-J|F7L7FJL--7FL7FJ|L-7JF-J|L-7F7F7FJL--7L--7|F-JLLJF--------JF7LL-J|F7LJF7F7F7FJ.J.L-FL-7
LL77.L|JL7|7F--J|F7F7LJL7|F7F-JL7|F7F7F7|||F-JLJFJL-7||L7||F7F7|F-J|FJF7|FJF7|F-J||||L-7F-JF7FJ||F---7L---------JL-7F-J|L-7|LJLJ||L7|7|FL-LJ
FJ--F-JLLLJFJF7FJ|LJL---JLJLJF--JLJLJLJLJ|LJFF-7L7F-J||FJ|||LJ||L7FJL7||||FJ|||F7|||L--JL-7||||LJL--7L----7F7F-----JL7FJF7|L-7F-J|7L--FL-77|
-|J|F-7||F-JFJLJJL--7F7F7F7F7|F---------7L---JFJJ|L-7LJL7||L-7||FJL7FJ|||||FJ|||LJ|L--7F--J|||F7F7F7L--7F7LJ|L------7LJ|||L--JL-7L7.L-7JF|FF
L|.FL||-7L7FJF7F7F7.LJ||||||LJL7F------7L7F---JF-JF7L7F7||L7FJ|||F7|L7|LJ||L7||L77L7F7|L7F7|LJ|LJLJL---J||F7L-------JF-7|L--7LLLL-JJ.|JLFLJL
-7-L-JJJF-J|FJLJLJL7F7LJ||||F-7||F-----JF||F7|FJF7|L7LJ||L7||F||LJ|L7||F-J|FJ|L7L-7LJLJFJ|||F-JF----7F7FJLJL-7F---7F7L7||F--J7J-F|FLF.FFL-L.
FJFJ7L-.L7FJL-7F--7|||F-J|LJL7LJ|L---7F-7|LJL7L-J|L7|F7||FJ|L7|L7FJFJLJL-7||FJFJF7L--7.L-JLJL--JFF--J|LJF-7F7LJF-7LJL-JLJL7F7FF77LLJ|F7J77|.
|L7F-JL-J|L77L||F-JLJ|L7FJF--JF-JF7F-J|FJL---JF-7L-JLJLJ||-L7||FJL7L---7FJ|LJ-L7||F--JF-77F7F7F-7L--SJF7L7LJ|F7|F|F---7F-7LJL-J|7.|--J.F7777
L.FJF|7|7L7L7FLJL---7|FLJJL7F7L7FJLJJFJL7F--7FJFJF----7FJL-7||||F-JF---JL7|F--7|||L--7L7L-JLJ|L7|7F---JL-JF7LJLJFJL-77||||F----J-.F.FJ-7LL-7
|LJ|-|--7LL-JF7F----JL7F-7FJ||FJL----JF7||F-JL7L7L7F--J|F--J||||L-7L----7|||F7LJ||F--J7L----7L-JL-JF------JL7F-7L7F7L7|L7|L----777FFLJ7L-J|J
|J7JFJJJ|FF7.||L7F---7||FJL-JLJF------J|LJL-7.|FJFJL-7.LJJF7LJ|L7FJF-7F7|LJLJL-7||L--7F7F7F-JF7F7F7|F------7||FJ-LJL7|L-JL-----JF--7LL777.L|
.F--L7F-7L|L-JL7LJ7F-J|||F7F7F-JF7F7F7.L---7L7|L7|F7FJF7F7|L-7|FJL7L7||||FF----J||F--J||||L--JLJLJLJL----7FJLJL7F7|-LJ-F-----7F7L-7L77F7J-77
F7|.LL-L|||F--7L-7FJF7LJLJ|||L--J||LJL7F7F7L-J|FJ||LJFJLJ|L-7||L7FJFJLJ||FJF-7F7|||JF-J|||F-7F--7F-------J|F7F7LJL7F7FFJF7F-7|||F7|FJF||||LL
7L7FJFF-LFJ|F-JF7LJFJL7F-7||L7F77LJF-7LJLJL7F7|L-JL77|F-7|F7||L-JL7L--7||L-JLLJ|||L7|F7LJLJFJL7FJL----7F-7LJLJ|F-7LJ|FJFJLJ||||||LJL7FJL7J7J
|.L7|LJ|JL-JL--JL7FJ7FLJ||LJFJ||F--J.L7F7F7LJLJF7F7L7||||LJLJL---7|F-7|LJFF7.F-J|L-JLJL---7|F7|L7LF---JL7L---7|L7|F-JL7L-7F7LJ||L-7FJ|F-J-|7
JFFJLJ|LFJLLLF---J|F7F7F7L-7|7||L--7F7LJ||L7F7FJLJL7LJL7L-7F-7F7FJ||LLJ-LFJ|FJF7|F--7F-7F-JLJ|L7L7L--7F-JF---JL-JLJF7FJF-J||F7||F-J|FJL-7J||
|7LF|.|-F7J-FL----J|LJLJL--JL7||.F7LJL7FJL7LJ|L7JF7|F-7L-7||JLJ|L7LJ||7.LL7LJFJLJL-7|L7|L---7|7L7|LF7|L7FJF-------7||L7L-7||||||L-7LJF--J.FJ
F7L7JL.LLLF7F7F----JF7F7F7F-7LJL-JL---JL7FJF-JFJFJ||L7L7FJLJ7|7|FJJLFJ7L-LL7FJF----JL-JL----JL--J|FJLJFJL7|F------J||L|F-J|||||L7LL7FJFF7JJJ
.LJL.|L-7.|LJ|L--7F-JLJLJLJ7L---------7FLJFL--JLL7|L-JFJ|F7||F-||JF.|FJJLLLLJ-|F--7F7F7F7F--7F7F7LJF-7L-7LJ|7F---7L||FJ|F7|||||FJF-J|F7||..F
|....-7FJ7L-7L---JL7F----------------7L---7F7JF7FJL--7L7LJL7-|.LJJL-.L7JF77.|JLJF-J|LJLJLJF7||||L7FJFL--JF7L7L7F-JFJ|L7LJLJLJLJL-JF7LJLJL-7J
7.F77.L-L7|.|F7F7F7|L7F7F7F7F--7F---7L7F--J||FJLJF7F7L7L7F7L7-7LJJF|-7F-JL7...|JL-7|F-7F--JLJ|||FJL7F7F7FJL7L-J|F7L7|FJF------7F7FJ|F7F7F7|7
J7.|J..||L7-LJ||||||.LJLJLJ||F-J|F7FJ.LJFF-JLJF-7|LJL-JL||L7|.L.L-7.L7JF|-LJF|J7|LLJL7|L-7F-7|LJL-7||LJ|L-7|F--J|L7|||FJF7F7F7LJLJFLJ||LJLJ7
L7F7|FLF7.LFJL||LJLJF7F7JF7LJL--J|LJF7JF-JF-7FJF|L----7FJL7LJ--J|F7-F777|7|LF77LF7F--JL--J|FJL7F-7LJL-7L--J|L---JFJ|LJL-JLJLJL7F----7|L-7F|J
LL|LJ7-|7F-J..||F-7FJLJL7||F7F7F7L--JL-JF7L7|L-7L--7F-JL--JJ-|7|F|.LLLLLLF7.|L7-||L7F----7|L7FJL7L-7F-JF--7L7F7F7L-JF--7F7F7F7LJF7F7|L-7|J.|
-JJF|JF-JJ.F7-LJL7LJF7F7LJLJLJ||L---7F-7|L-J|F-J.F7LJF7F7F7J.LLJ7|FF7FJL|.L-L7L-JL7LJF7F-J|FJ|F7L-7|L--JF-J|LJLJ|F-7L7|LJ||LJL7FJLJLJ|LLJ--L
.|FL|FJ7L7FJ|LLF7L--JLJL-----7|L---7LJ-|L--7|L-7FJL7FJLJLJ|L7-|L--|JL7FL--|FL|F--7L--JLJF-J|FJ|L--JL--7LL7LF7F77LJFL7L--7|L--7|L-----77-|7-L
F-L-J7FLJ||F77FJL7F7F7F7F----JL---7L7F7L--7||F-J|F-J|F--7FJF7-L-JLJ7LJJFFFL-7LJF-JF-----JF7LJLL-7F7F-7L--JFJLJL----7|F--JL7F-JL--7F--J7--.-7
|-L7J.F7||--J-L-7LJ||||LJF7F-7F--7L-J||F-7LJ|L--J|7FJL7FLJL||FJ7.77|7-|-|.LLJ7LL--JF7F7F-J|F7F--J|LJ.L-7F7|F-7F7F7FJ|L--7FJL----7|L-7L|||-LJ
.LL|J-FL7J.|L|F7L-7LJLJF-J||FJ|F-JF--JLJFJF7L7F-7|FJF7L7F7-||7JJ|JFJ|F-JJ7JLJ|7LF--J|||L-7|||L---JFF---J|LJL7||LJLJFJF--JL7F7F--J|F-J7LL77.J
7.L|L-J|LFFF--J|F7L7F7FJF-J|L7|L7FJF-7F7L-JL7|L7|LJFJL7LJL-JL7-F77L77JF-J|-J.F--JF-7LJ|F7|||L7F7F-7L---7|F--J|L---7L-JF--7LJ|L-7-LJ7LJ|.L77.
LF.7JF-|.|JL--7LJL-J||L7L--JFLJFLJLL7||L----JL-JL-7L-7L--7F--JFJL7-7.LFJFF7|F|F--J-L-7LJ|||L7|||L7||F7|LJL--7|F---JF--JF7|F7|F7L-7-77FL7-|.F
||FJFF7JF--7F-JF--7FJL7|F--7F-------J|L---7F----77L-7L--7LJF-7L7FJF77.L77|FF-J|JF----JF7LJL7|LJ|FJ|FJ|F7F---JLJF7-FJF7FJ|LJ||||F7L7.L|JJ7-|J
|J-FFF7-|F7LJF7|F-J|F7|||F7LJF---7F7-L---7LJF--7L--7|F7FJF7|FJFJ|FJL7-J77LLL--J.L7F7F-JL--7|L-7LJFJ|FJ||L-----7||FJFJLJLL7FJLJ||L7|77|L-J.|7
|L-FJLLFLJL7FJLJL7FJ|LJ|LJL7FJ-F7LJL----7L-7L-7L-7FJLJLJFJ|||-L7LJF-J7F-J-.|7F-7|LJ|L7F---JL--JF7L-JL7||JF----J|||FJF7F-7LJF7|LJJLJLFLFJ--J-
|7F|7.LLJFFJL7JF7||F|F7L7F-J|F-JL-------J-FJF7L-7||.F--7L7|||F7L7FJF7-|.||.LFJFJF--JFJ|F-7F-7F7|L7F-7LJL-JLF7F7||||7|||FJF7|L-7F7-F7J.|FF7J|
|-|J77FJ7LL7FJFJLJL7LJL-JL--JL-----7F--7F7L-JL7FJ|L7L7FJFJLJ||L-J|FJL-7F7-F7L7L7L--7|FJ|.||LLJ||FJ||L7F----J||||LJL7|LJL7|LJF7||L-7.-LLJ|F-J
LJ.JL|7L7FL||-L--7FJJF7F----7F7F---J|F-J||F7F7LJ-L-J.|L7L7F-JL--7LJF--J||-F-7L7L7F-J|L7L7||F--J|L7|F-J|F----J|||F--J|F-7||F-JLJ|F-J-|..|7|-|
L-7||LJ.FLFJ|-LF-J|F-JLJF7F7LJ|L----JL--JLJLJL--7F--7L7|FJL-7LF7|F-JF-7||FJFJFJFJL7FJJL7|||L7F-JFJ||F-J|F7JF-JLJL---JL7LJ|L7F-7||J7FF7.---7J
LL-7LFJ-|.L-J|.L--JL----JLJL-7|F7F7F7F7F--7F----JL-7L7|||F7FJFJ||L-7L7|||L7L7L7L-7||7F7LJLJ7LJF7L7|LJF-J|L7|F------7F7L--JFJL7|||JF7JF-7.LL7
J.L|.|.LL|L|F|-L7F----7F7F7F-JLJLJLJ|||L-7LJF---7F7L7LJ|||LJ|L7LJF-JFJLJL7|FJFJF-JLJFJL-7JF---JL-J|F7L--JFJ|L-7F--7LJL7F-7L-7||||F-7.|7L-7J-
|LJLJ...|L|.F7FLFJF7F7LJ|||L-------7LJL--JF7|F--J||FJF7LJL-7F7L-7L7-|F7F7|||FJFJF7F7L7F7L7|F---7F7||L----J-|F-J|F7L7F7LJJL-7LJLJLJFJ.--J|.|.
F|LFL-FJ7F|7|.||L7|||L-7LJL--------JLF----JLJL--7||L-J|F---J|L-7L7L7LJLJ|LJ|L7|7||||7LJ|FJLJF7FJ|LJ|F----7FJL7FJ|L7LJL7-F7F|F--7F7|.F|JLFF77
JJ.-J|.LJ-J-L-F-FJ|LJF7L-------7F7F7FJF7F-------J||FF7||F7F7L7FJJL7|F7F-JF-JFJL-J|||F-7||7JFJ|L7L7FJ|F---JL7FJ|FJ.|F-7L-JL7LJF7LJLJ-|--F|LL.
F7-J.77-||L-J|F7L-JF-JL--------J|LJLJFJLJF---77F7|L7|||LJLJL7||F7FJLJ|L-7L-7L7F7FJ||L7||L7FJFJ|L-JL-JL7F---JL-JL-7||L|F-7FJF-JL--7-7J|7FJJ.F
LL7|--JFLF.7-FJL---JF7F---7F7F7FJF---JF7-|F--JFJ||FJ||L7F---J||||L7F7L7FJF-JFJ|LJFJL-J||FJL7L7F7F7F---J|F--7F----J||FJ|7|L-JF----JF7|FJL77-F
LJFF-|777L7F7L-7F7F-JLJF-7LJ||||-L---7||FJL--7L7||L7||FJ|F7-FJ|||LLJ|FJL7L-7L7L-7L---7LJ|F-JFJ||||L--7FJL7J|L---7L||L7L7L7F7L-----JL7J.F7JJ|
L7.|||L-7.FL7.|LJLJF7F7L7|F7LJLJF7F--J|LJF--7L-J||FJ|||FJ|L7L7||L-7FJ|F-JF-JFJF7|F-7||F-J|F-JFJLJ||F7LJF7L7|F7F7L7LJ|L-JFLJL7F7F-7F7|.FLJJ.|
FJ--7FL-F7FJ|7|7F7FJLJL7||||F-7J||L---JF7|F7L7F-J|L-J||L7L7|FJLJF-JL7|L-7L7FJFJLJL7|FJL7FJ|F7L--7|FJL--JL-JLJLJL7L7JF--7F7F7||LJFLJ||7FJ|-FF
FJ.LFJ77F-7F-7F7||L---7|||||L7L-JL---7FJLJ|L7|L7FJF-7||FJJ||L--7|F7FJ|F-JFJL7L-7F-J|L-7|L7|||F--J|L----7F7F7F7F7L-JFJF-J|||||L-7FF7LJ7|.-.|J
|--7FL-7L7|L7||||L7LF-JLJLJL7L-7F7F7||L---JFJL7|L-JFJLJ|F7||LF-JLJ|L7|L-7L7FJF-JL-7|F-J|FJ|||L--7|FF7F7LJLJLJLJ|F-7|FJF7||||L--JFJL7F7JFJFJ.
7--LLJ.F-JL-JLJ|L7L7L---7F-7|F7LJLJL7L7F-7FJF-JL--7L7F-J|||L7|F7F-JL|L7FL7|L7L7F7FJ|L7FJL7LJL7F7|L7|LJL--------J|FJ||FJLJLJL-7F-JF-J||L||-J7
LFFJ.L-L-7F--7FJLL7|F7F-J|FJLJL-----JJLJFJL7L-----JFJL-7||L7|||LJF7FJFJF-J|-L7LJ||FJFJ|F7L-7FJ||L7|L7F-----7F7F7|L-JLJF-7F---JL7FJF-JL--7-7.
-7F7-.LJ-LJF-JL---JLJ|L--JL---7F-----7F7L-7|F7F--7FJF--J|L7|LJL7||||FJ7L-7|F7|F-J|L7L7||L7FJ|FJ|FJL7LJFF---J|LJLJF----JLLJLF-7FJL-JF-7F7|.FF
FLL---7|.LJL7F7F7F7F7L------7JLJF---7LJL-7LJ||L-7|L7||F7L7||F-7L7||||F7F7|LJLJL-7L7|FJ|L7||FJ|FJL7FJF7FJF7F7|F---JF7|F7FF7FJFJL7F--J7LJLJ--|
L7L7||J|..|FJ|LJ||||L--7F7F7L--7L--7L----JF7||F-JL-JL7||FJ|LJJ|FJ|LJ|||||L7F-7F7|FJLJFJFJLJL7||.FJL7||L-JLJLJL----JL-J|FJ|L7|F7|L----7J.FF7|
LJ.LJL-|7FFL7|F-J|LJ|F-J|||L7F7L--7L----7L||||L-----7|||L7|FF7|L7L-7||||L-JL7||LJL--7L7L7F--J|L7L-7LJL7F---7F7F--7F---J|FJFJ||||F----JJ|-|-7
.|-|7|JL77.FLJL--J|F-JF-JLJ|LJL--7L----7|FJLJ|F-7F-7|||L-JL7|LJFJF7|LJ|L--7FJ|L7F7F7L7L-JL-77|FJF-JF--JL--7|||L-7LJF7F7||J|FJ|LJ||F7F7LJFJ.J
7L7J-|.L|7-JJ|-F---JF-JF7LF7F----JF--7LLJ|F--JL7|L7|||L7F7FJL7FJFJ||F-JF7F||.L-J||||JL-7F--JFJL7L-7L--7F--JLJ|F-JLFJLJLJL-JL-JF7L-JLJ|F|-||J
L7L-.||JJ|.L-J7|F---JF-JL-J|L---7FJF-JF-7|L7F7FJL7|||L7LJ||F-JL7L7|||F7|L-JL7F7FJLJ|F7FJ|F7FJF-J7FJF--JL---77|L---JF-7F------7||F7F--JF7FFF-
.L-L77|F--.F-LFJ|F7F7|F---7|F7F7||L|F7|FJ|FJ||L7FJ|||FJF7||L-7FJ||||||||F---J||L--7|||L7|||L7||F7|FJF7F7JF7L7L--7F7L7|L-----7|||||L---JL-7|7
F|-|.LL--|7LF7L-J||||LJF--JLJ||LJ|FJ||||FJL7|L7|L-JLJL7|||L7FJL7FJ|||||||F-7FJL7F7|||L7||||FJ|FJLJ|FJ||L7|L-JF7J|||FJL7F--7FJLJLJL7F-----JJ-
|J.F7L|.|F7|.|.F-J|||F7L-7F-7|L-7|L7|LJ|L-7||FJL----7||||L7|L-7||.||||||LJ7|L-7||LJ||FJ|LJ||L||-F-JL7|L7||F--JL7LJ|L-7|L7JLJ7|F7F7LJF7-|J-|.
|FL|--JF7FJ-L7FL-7LJLJ|F7LJFJ||FJL7|||FJF7|||L7F7F7FJFJ|L7||F-J|L7|||||L-7FJF7|||F-J|L7|F-JL7|L7|F7FJ|FJ|LJF7F7L7FJF7|L7L-7F7FJLJ|F-JL-77FF|
L|J|L|.L|L7|.LF7FJF7F7LJL-7L7L7L7FJ||FJFJLJ||FJ|LJLJJL7|FJ||L-7L7|||LJ|F7|L7|||||L-7L7|||F-7|L7|LJ|L7|L7L7FJLJL7||FJ||FJF7LJ||F--J|F---JJF||
.|JF7-F7.|L-JJ|LJFJLJ|F7F7L-JFJL|L7||L7|F7FJ|L7L-----7||L7||F7L7||||F-J|||FJ||||L7||FJ||||7||FJL7FJFJL-J7|L--7|LJ||FLJL7||F7LJL---JL-77-|JL-
.F7-F-JFF-JF.FJF7|F--J||||F-7L--JFJLJ-|LJ||FJJ|F-7F-7|LJFJ||||FJLJ||L7FJ||L7|||L7L7|L7||LJFJ|L7FJL7L--7F-JF-7L-7FJL--7FJ|||L7F7F7F7F7|7.|J-|
-|L-L7.F77|L-L7||||F7FJLJLJLL7F7FJFF--JF7|||F-JL7LJFJL7FL7||||L--7|||||||L7||||.|FJ|FJ|L7-|FJ|||F7L7F-J|F7L7|F-JL7F--JL7|LJ7LJLJLJLJLJLJJ|.L
||F7|L7..FF7J|||LJLJLJ-F-----J||L-7L7F7||||||F-7L-7|F7L-7|||||F7FJ||FJL7L7|LJ|L7||FJL7L7|FJ|F-J|||FJ|F7LJ|FJLJF--JL--7FJL-----------7L77-FL.
-.LL|JJF7|L|-F||.|7LF7LL--7F-7||F-JFJ|||LJ||||J|F-J||L7FJLJLJ|||L7||L7FJF||.FJFJ||L7FJLLJL7||F7LJ|L7LJ|F7LJJF7L7F7F7FJ|F7F7F-7F7F-7FJ.|---.F
FF-7JF-7-L.|7FJ|FFF7|L7F--J|7LJ|L7LL7|LJF-J|LJFJL7FJL7|L-7F--J||FJ||FJL-7|L7L7|FJ|F|L--77-||LJ|F7L7L-7LJL---JL7LJ||LJ.||||LJFJ|LJ|LJ.FJFJ-7|
LF-|.F-J-LFJ-L-JF7|||FJL---JF--JFJF-J|F-JF7|7FJF-JL7FJL7FJ|F--J|L7||L7F7||FJFJ|L7L7|F-7L7FJ|F-J||FJF-JF-7F--7FJ.FJL--7LJ|L7-L7L7|F-7FLLF-7JL
.LFJ-|.|7.7LFFF-JLJLJL----7FJF-7|FL7FJL7FJ|L7L7L--7||F7|L7||F--JFJ||FJ|||||JL7|7L7|LJFJFJL7|L7FJ||FJF7L7|L7FJL-7L-7F-J|LL7L-7L7L-JFJ7J-|L7-.
F-JJ.----FJLF-JF-7F7F-7F-7LJFJFJ|F-JL7L|L7|FJFJF7FJ|||LJFJ||L7F7L7LJL7|||||F-J|F-JL-7L7|LFJ|FJL7||L7||FJL7|L7F7L-7|L-77F7L--J-L7F-JL7J.F7|||
L.|7|J7|.L-7L-7|-LJ||J||FJF7|FJFJL7F7|FJFJ||7|FJ|L7||L7FJF||FJ||FJ7F-J|||||L--JL--7FJJ|L7L7|L7FJ|||LJ|L7FJL7LJL7FJ|F7L-JL--7F-7||J|F-.F-J.-7
|-F|-JFJL-77JLLJJ.FJL7LJL-J||L7|FFJ|||L7|FJL7LJFJFJLJ.||LFJ||FJ|L-7|F7|||LJF------J|.FJFJ.LJFJ|-|L7FFJFJ|F7L7.FLJFLJL7F-7F-J|FJLJF7-LFFJJ.FJ
F.F||LF7|-|.LFJ|.FL7FJF----J|FJL7|FJ||FLJL7FJF-JFJF---JL7L7|||7|F7|||||||JFJF7F7F-7L7L7L--77L7|FJFJFJFJFJ|L7L----7F--JL7|L--JL---JL7.7JL..-7
|F-J-JL-7-|7.JJF-F-J|FL--7F-JL-7||L7LJF---JL7|F7L7L-7F-7L7|||L7||LJ||LJ|L7|FJ||LJFJFJJL7F7|F-J|L7L7L7L7L-J||F----JL7F-7|L7F-7F-7F7FJ7L7JL..|
LLJF7F7.L7F|-L-L7L--JF7F-J|F---J||FJ|FJF7F7FJLJL7L-7||LL7||||FJLJF7LJF-JFJ||FJ|F-JFJF-7||||L7FJF|FJ.L7|7F--JL-----7||FJL7LJL||LLJLJJ7|.-J77|
FL7L7J|7LF7JJ|.F|LF--JLJF7|L7F-7|LJF7L7|LJ|L--7FJF7||L7||||||L-7FJL-7L-7L7LJL-J|F-JF|FJLJLJ-LJF-JL7F-JL7L7F-7F----J||L-7L--7LJJ-JLJLLJ7.|L-J
|.|FL.|7.LJ.||FFF7L7F-7FJ||FJ|FJL--J|-LJ|FJF7FJL7||||FJFJ|||L7FJL--7L-7|FJF----JL---JL-----7F-JF7FJL-7FJ7||-|L----7||F-JF7FJ.|J-J-|LJ-L-FJJ|
F7J|JFF7777.FF-FJL-J|FJL7||L-JL7F--7|7LF7L7||L7|||LJ|L7L7|||FJL--7-L-7LJL7L7F7F7F-7F--7F--7|L7FJ|L--7|L-7||FJF-7F7|LJ|F7|||J.F7LL--7|..FLJ-F
L7.J7-L-F7LJLL-L----J|F-J|L-7|||L-7LJF-JL-J|L-JFJ|F-JFJ-LJ||L7F7FJLF-JF-7L7LJ|||L7|L-7||F-JL7LJFJF--JL7FJ||L7L7||LJ-LLJLJ||---7.FJ|7|-LL...J
F--LJL.F|J|-7..LJ-F--JL7|L7FJF-JF-J.LL7F--7L--7L-JL-7|J.J.LJFLJ|L-7L7FJFJFJF-J||FJ|F-J||L-7FJJLL7L-7F-J||LJFJFJ|L7J7|7LLJLJ.LFJ-||LJ.|J|-|FJ
LF..-7.JJFLFF-7-|LL---7|7LLJJL7FJJLJ-LLJF-JF-7L-7F7LLJ--J7L|-|LL--JFJL7|FJJ|F7|||FJL7J||J|LJ-F--JF7||F7L7F7|FJ-L7|.FL7F|J||77|77F7-----JFF-.
||F---|7FF7.LJL-7-J7LL||7LJ||-LJJJFL--F7L-7|FJF-J||7|J-|.J7L.L.F|LLL--J||J7LJ|||||F-JJ||LJ-LJL7F-J|||||FJ|LJL--7||-J-JLJ.7LFLJ7-L-J||...-J-|
||L7-7|F.L|F7F.LF7-FJL|L7|LLJ7||7.L-|7||-FJ|L7L--JL7|..F7LJJJ-L7LJ.L|LLLJJF|L||||||-|FLJ-L7L-7LJLFJ|LJLJLL--7F-J||7.LL-7-LFF-|L|LFFJF77.F--7
|-LL-F--7-|||-FJ|J7||FL-J-7.L.F7--7.FF||FJFJJ|F7F--JF--|..J7LF-FJ.FL7J|F|-7-|LJ|||||LF|J.|||L7-JFL-J7JL|7|F7||F7||--7FF|7-|LFF7F-||FF7F-|FFJ
|L7|-7FJ|||7.||F|F-77-JFLJ||..FJ|F-FF-JLJFJF-J|LJJ7L|JLJ-F-FF.F-JL7LJ7LJ||L-J7LLJ|L7|LJJ.|J||LJ|7F|L|-JLLL|LJLJ|LJ7-|--.JFJ-7L7.FJ|-J|FJL7--
L7||.|7LJ-J--.F7F-.||L.F-F-LL--7F|.FL--7FJ-L--J.LF-F7J7J|JF|7.F|7-J7FFJ.||F.LFJ|FJFJJ.|JFL-L|J7|7F|-L-J7|.L7F-7L--7.F.FL--J-|FJ-J7|.FLJJ|L|J
LFJJL---|FJ.|-J||LFFJ|.|LJ||LLLJF7F|.J7LJ|FJ|.J7-|-L|FFF|7L----J|.L-|JFLJ7L|-|F-L-J-|-7||.77L---7J.LLL.F7FL|L7L---J..FJ.JL7--L77|-7.LJ-F|FJ7
.LL-F|.-7-J7.L|.J.|L|-F77.FJ-7-L7L--7L77L||F7JJL-|7J|FL||LJ-7JL-J-JJL77L-J.|-J7J-|.-----J-J7F-|7|F7.7F-L-FF|FJJ|F|FJFF-|LLJFJ7|77.J-|-F-7L.F
FFJF7LFLF-LF-F7.L---L..L-|J|7..|LF.LJF||-LJ7|J-J7.F7L-7L|-FF7|L.|.|L|-7LL-|JFL|F-J.|7FLF|7LL7.J7L7||-7|L.|LLJJ.F|JLJL|.||||||F||F-|F|F|LJFF|
FJL7.FF-L7-7FJ|F.||7..|-||F7-7F-JL-.L-7JJFF-J7J.L-L7.LJL7-JJLF.FJ.--|FJ-J|L7J||F7L7--7.7J7-LL|.F7LJ|7FJ.LJFL|--7J7.77FF-L-|-JJ|7|.||LFF..FJJ
L.F--LL7LF-J|JFL-----FL-FLJLL|J.F-J77FJJF|-|||7.|.F7J.|-|||-F7J7.F|FFJJJFF-7.F7|F.LJFJ.|.F7J.|..L7.|-LJ-|FJ7L77|FFFFJJLJJ.-.L--|77FF-LLJF|7J
J-|J.LJL-J....--F-|7.L-FJ.J.--J7.7-L-|LL-LJL-J-7-J-|-JLF-JJ-FJLLF-F-7.7-FL---JL|J7L-7-F--L.--F77-7JJLL-7----JLL--7-|J.LL-7JJJ.LL|JLL-|JLL7JJ
'''.strip('\n').splitlines()



#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

# visited=set()
# current={}
# data = [[column for column in line] for line in data]
# W,H=len(data[0]), len(data)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S':
# 			current[(j,i)]=0
#
# while len(current)>0:
# 	next= {}
# 	for (j,i),dist in current.items():
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				#if dx==0 and dy==0: continue
# 				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
# 				old=data[j][i]
# 				new=data[newY][newX]
# 				if not (dx==1 and (new=='-' or new=='J' or new =='7') or
# 						dx==-1 and (new=='-' or new == 'L' or new =='F') or
# 						dy==1 and (new=='|' or new == 'L' or new == 'J') or
# 						dy==-1 and (new=='|' or new == 'F' or new == '7')):
# 					continue
# 				if not(
# 						old=='S' or
# 						dx == 1 and (old == '-' or old == 'L' or old == 'F') or
# 						dx == -1 and (old == '-' or old == 'J' or old == '7') or
# 						dy == 1 and (old == '|' or old == 'F' or old == '7') or
# 						dy == -1 and (old == '|' or old == 'L' or old == 'J')):
# 					continue
# 				if (newY, newX) in next:
# 					print('found n', max(next[(newY, newX)], dist))
# 				if (newY,newX) in current:
# 					print('found c', current[(newY, newX)], dist)
# 				if (newY,newX) in visited: continue
# 				next[(newY,newX)]=dist+1
# 				visited.add((newY,newX))
# 	current=next

data=data2

onLoop=set()
current={}
data = [[column for column in line] for line in data]
W,H=len(data[0]), len(data)
for j in range(H):
	for i in range(W):
		if data[j][i]=='S':
			current[(j,i)]=0
			onLoop.add((j,i))

startPos=set()
start=None
while len(current)>0:
	next= {}
	for (j,i),dist in current.items():
		for dy in range(-1, 2):
			for dx in range(-1, 2):
				#if dx==0 and dy==0: continue
				if dx==0 and dy==0 or dx!=0 and dy!=0: continue

				newY,newX=j+dy,i+dx
				if newY<0 or newX<0 or newY>=H or newX>=W: continue

				old=data[j][i]
				new=data[newY][newX]
				if not (dx==1 and (new=='-' or new=='J' or new =='7') or
						dx==-1 and (new=='-' or new == 'L' or new =='F') or
						dy==1 and (new=='|' or new == 'L' or new == 'J') or
						dy==-1 and (new=='|' or new == 'F' or new == '7')):
					continue
				if not(
						old=='S' or
						dx == 1 and (old == '-' or old == 'L' or old == 'F') or
						dx == -1 and (old == '-' or old == 'J' or old == '7') or
						dy == 1 and (old == '|' or old == 'F' or old == '7') or
						dy == -1 and (old == '|' or old == 'L' or old == 'J')):
					continue
				if (newY,newX) in onLoop: continue
				if old=='S':
					startPos.add((dx, dy))
					start=(j,i)
				next[(newY,newX)]=dist+1
				onLoop.add((newY, newX))
	current=next
if (1,0) in startPos and (0,1) in startPos:
	data[start[0]][start[1]]='F'
if (1,0) in startPos and (0,-1) in startPos:
	data[start[0]][start[1]]='L'
if (-1,0) in startPos and (0,1) in startPos:
	data[start[0]][start[1]]='7'
if (-1,0) in startPos and (0,-1) in startPos:
	data[start[0]][start[1]]='J'
if (-1,0) in startPos and (1,0) in startPos:
	data[start[0]][start[1]]='-'
if (0,1) in startPos and (0,-1) in startPos:
	data[start[0]][start[1]]='|'
for line in data:
	print(''.join(line))


current=set()
current.add((0,0))
outsideLoop=[[False for i in range(W*2)] for i in range(H*2)]
while len(current)>0:
	next= set()
	for (j,i) in current:
		for dy in range(-1, 2):
			for dx in range(-1, 2):
				if dx==0 and dy==0 or dx!=0 and dy!=0: continue

				newY,newX=j+dy,i+dx
				if newY < 0 or newX < 0 or newY >= H * 2 or newX >= W * 2: continue
				if outsideLoop[newY][newX]:
					continue
				if newY//2!=j//2 or newX//2!=i//2:
					outsideLoop[newY][newX] = True
					next.add((newY, newX))
					continue


				old=data[j//2][i//2] if i//2<W and j//2<H else ' '
				new=data[newY//2][newX//2]


				i2=i%2
				j2=j%2

				if (j//2, i//2) in onLoop and (
					abs(dx) == 1 and j2 == 0 and (old == '|' or old == 'J' or old == 'L') or
					abs(dx) == 1 and j2 == 1 and (old == '|' or old == '7' or old == 'F') or
					abs(dy) == 1 and i2 == 0 and (old == '-' or old == 'J' or old == '7') or
					abs(dy) == 1 and i2 == 1 and (old == '-' or old == 'F' or old == 'L')):
					continue
				if new == 'I':
					print(newY, newX, j//2, i//2, j2, i2, old, new, newY//2==j//2 and newX//2==i//2)

				outsideLoop[newY][newX]=True
				next.add((newY,newX))
	current=next

ans=H*W
for j in range(H):
	for i in range(W):
		outside=False
		for j2 in range(2):
			for i2 in range(2):
				if outsideLoop[j*2+j2][i*2+i2]:
					outside=True
		if outside:
			ans-=1


for j in range(H*2):
	for i in range(W*2):
		if (j//2,i//2) in onLoop:
			print('X', end='')
		elif outsideLoop[j][i]:
			print('*', end='')
		else:
			print(' ', end='')
	print()
print(ans) #631 too high






#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())



# current=set()
# for i in range(W):
# 	current.add((0, i))
# 	current.add((H, i))
# for j in range(H):
# 	current.add((j, 0))
# 	current.add((j, W))
# outsideLoop=[[False for i in range(W)] for i in range(H)]
# while len(current)>0:
# 	next= set()
# 	for (j,i) in current:
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
# 				old=data[j][i] if i<W and j<H else ' '
# 				new=data[newY][newX]
# 				if outsideLoop[newY][newX]:
# 					continue
#
# 				if (j, i) in onLoop and (
# 					dx == 1 and (old == '|' or old == 'J' or old == 'L') or
# 					dx == -1 and (old == '|' or old == 'J' or old == 'L') or
# 					dy == 1 and (old == '-' or old == 'J' or old == '7') or
# 					dy == -1 and (old == '-' or old == 'J' or old == '7')):
# 					continue
# 				if (newY, newX) in onLoop and (
# 					dx == 1 and False or
# 					dx == -1 and (new == '|' or new == 'J' or new == 'L') or
# 					dy == 1 and False or
# 					dy == -1 and (new == '-' or new == 'J' or new == '7')):
# 					continue
# 				if new == 'I':
# 					print(newY, newX, j, i, old)
#
# 				outsideLoop[newY][newX]=True
# 				next.add((newY,newX))
# 	current=next
#
# ans=H*W
# for j in range(H):
# 	for i in range(W):
# 		if (j,i) in onLoop:
# 			print('X', end='')
# 			ans-=1
# 		elif outsideLoop[j][i]:
# 			print('*', end='')
# 			ans-=1
# 		else:
# 			print(' ', end='')
# 	print()
# print(ans) #631 too high

