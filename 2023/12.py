#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''.strip('\n').splitlines()
data2='''
???#?????#?.#???#??? 9,7
.?.?..?????.?# 1,1,3,1
??#??#?#?#?.?????? 9,1,1
????????????? 1,5,1,1
??#??#????##??. 6,3
#?#..#?#??? 3,5
???#.??.?#??? 3,1,2,1
?.?#??.??????????? 2,1,3,1
??#?#??#.#..?# 4,2,1,2
.????????..#?? 6,1
.??..?.???? 1,1,1
?.?##?#???#?#????# 1,10,1,1
??????????#.#?????.? 2,7,1,4,1
?.???..??.????#? 2,3
????.#??#???. 3,7
????#?????###?????#? 4,12
#.??#????. 1,5,1
?#???#??#.???#?.. 2,1,1,1,3
#???#????#? 7,1
??#..????#?#? 1,1,1,5
.##??#??#????????? 9,3
????#.#??#??#.. 4,1,2,1
...?.???...#?#??.??? 2,4,1
..####?.?????? 4,2
#.?.?##?#??#??#? 1,4,5
??#??#???##?.?.??#?? 11,5
????#?#?.?.#.?#???? 5,1,1,1,2,3
???.????...???#?#? 2,4,2,4
?..???....???#?? 3,4
????##??###.? 2,3,3,1
?#..????#?##?##?#?? 1,13
##?.?#????.?????..# 3,3,2,1,3,1
.???.??????? 1,1,2,1
##?##?#?.?????#? 2,5,3,2
###?#?.??#?#? 3,2,5
##?#?.?#???#??????#? 2,2,3,2,2,3
#?.#?#?.??????.?..?? 1,1,1,5,1,1
.???....#? 1,1
???.#???#?#.??. 1,3,3
#???####????..# 1,8,1,1
.?????????#? 1,2,3
#?#???##?.???? 9,2
.???...??. 2,2
??#?#????# 5,1
#??????#?###.#??? 12,1
???#..??.??#??? 1,1,1,4
????.?.?.?.??? 1,1,2
????#?#?#?#?????? 7,4,3
??#..?.#??##?..????. 1,1,1,6,2
.#?#??#?.?#????#??. 6,8
#????????##??.?? 2,1,2,4,2
?###???.??????#??.?? 6,3,4,1
?#?#????#??.? 1,1,4
###?????.?...??? 3,1,1,1,2
.??#????#.. 3,3
.?..##??#?..???? 1,3,2,2
?.?.?.?.?#?.?.. 1,1,1,3,1
?????#??#??.????.. 4,4,3
??.???..??..?.? 1,2
??#?.??#.#????#? 1,1,1,1,4
???#.???#?#??#?? 1,1,1,5,2
?###??????#??#??.# 4,1,8,1
?#.????.???? 1,1,1,1
?.?????.#.?? 2,1,1,1
?.?#?###?..#?#???.?? 6,5
???????#??? 1,3
?.??#?.?#.????#??? 1,1,1,6,1
.???.?.?.#? 1,1,1
.#????..??? 3,1,2
?###?#???????.#?#? 8,4,1,1
?????????..???#. 2,2,2,1,2
?#.????#??###???? 1,5,3,1
.?.?????#.????#?# 1,5,1,4
?#?#?#????????##???# 3,2,3,6
??????????#?.???.? 1,1,2,4,3,1
.?????????#??? 3,7,1
??###??##?? 3,4
#.?????##? 1,1,5
??????.??#.#?##??# 1,1,1,1,1,5
????...?????? 1,3
??##??#????#??#??? 7,1,5
?.??????????.? 1,1,1
?.?????#??#?? 1,7,2
?.?#?????..?? 6,1
??????###??????#?.? 8,2
?##??????.? 5,1
?.???#???.#? 4,2
??##??.?.#?#???? 4,4
.##..?????# 2,4
????#??#.??????? 2,4,1,1
..???#??.#.???#.#. 1,1,1,4,1
??????????#?????# 2,1,5,1,1
?.??????.???##??.?? 1,3,1,1,2,1
.?????##???#?? 1,7
?.????????? 2,3
?##?#??..#?#?. 6,3
.???#?????#?.??. 2,2
?###??????..?# 6,1,2
?..#?????#?#?#????#? 1,12,1,1
?#.?????.???#.#?##?? 1,1,3,2,4
???###?.?????? 1,5,5
.????.??#?#?#??? 2,1,8
???#??#???#??.? 1,9,1
.#???#?????? 5,2,1
????????????#?. 1,9,2
?.??#??.?.???#??.??? 3,4
???#?..?????####? 5,1,4
????.???#??..? 2,6
#?#.?#??##?#??# 1,1,2,4,2
.?.??.?.#?.??? 1,1,2,2
?##????#.????????##? 5,1,10
???..#??#???# 1,1,2,1
.????.?#??????? 1,1,4,1
?#???.?##?#???.??#?? 1,2,5,1,1,1
.#?..#????? 1,1,2
????#??#??.#.##??? 4,2,1,1,3,1
??.#??#..?#????#? 1,2,1,2,4
#.?.#??.#? 1,1,1
?????.??#???#?. 2,3,2
?????#??????.?? 3,3,3,2
?????????.???#?? 5,3
##????..????????? 5,2,1,1
?#???????# 2,1,1
??.?#?.?#???..#.? 1,2,5,1,1
##??.?.?##?.?? 4,3,2
.#????.????#?? 3,1,1,1
.#..?#?#??? 1,5
?#.?.??.?? 1,1,1
.?????#?.??##??? 2,1,6
??????.??????# 3,1,2,1
?.??.#?#?#??????. 7,1
?#?.#????#?????.?? 2,2,3,2,1
??#???.?##?????? 3,5
#??#?????##?#??#??.# 1,2,5,1,3,1
?????#????#?????? 10,3
.#??.?.?????#? 1,1,1,7
????.???..#?????? 2,1,7
?????#??#??????? 2,2,6,1
???.??.??#????#?. 1,2,9
#.?#?.??##???? 1,1,5,1
.?????#??. 3,2
????#???.???.??? 6,2,2
??###?#?????. 3,1,1,1
????#?.???????.?.?? 1,1,1,7,1,1
????#??.?. 4,1
.#??.??.??.? 2,1,2
.?.????#?#???# 2,5,1
????.?#???#? 1,1,7
??#.?#????##? 1,1,8
???..??#??.??##??? 1,1,1,2,5
#??#??##???#? 1,1,6
??????????? 6,1,1
??#???#?#????. 4,3,1
?..##?###?????? 1,10
.???##????#??.?##?.? 5,4,3,1
???#??.???#?.??# 5,2,2,1,1
??.???.?.?????????? 2,1,2
????.??????#?#????? 3,1,1,5,1
.????##?..#????.?.?? 5,5,1
????????#???##??#?? 8,5,3
?.?.??#??#??##?.? 2,6
???#?????? 4,2
???##?????? 8,1
?#??##???##???#?. 1,3,7
??#??????##?? 1,1,4
??..???.?????. 2,2,1,1
?#??##?.?#? 1,3,1
??.????????##?#?? 2,3,6
.#.#??.??#.? 1,3,2,1
.?#?#???.?????. 5,1,1
????##???#?. 2,3,1
?#??#??????# 1,6,1
?.#?#.??#.##??? 1,1,2,2,1
???#????##?#?#?? 1,1,1,8
??.#..?.?????????. 1,1,1,3,1,1
?.#?##????? 4,1,1
?????.####?? 1,4
?????????????.??? 1,7,1,1
?????#??#?????#?#? 2,3,2,6
??#.?????. 2,4
.??#????#.. 3,2
???#????.??#? 4,1,1
????.??.??.??? 1,1,1,3
??##?#??#????#?..# 7,6,1
???#???.????? 4,1,3
?#?###?.#??##???# 6,2,4,1
?.#?#??.?..??.?? 3,1
#?#?.#?#?????? 1,1,1,7
????#??.??.?.?#. 5,2,1,1
???.??.????.. 1,2
?##????.???. 4,1,1
#.#?##??#???????. 1,14
?#????.####??? 2,2,5,1
??.?????#???.??? 1,5,1,1
????####???#? 7,1
?.??????#????.????? 1,8,1,1
???.?#???#.??# 2,6,2
.???#??.?#?#?? 3,4
???.????##???# 2,7,1
?????????? 1,1,1
#??????#?.??#?????? 1,3,2,3,1,1
#????????. 3,4
??.??#??.?#??#####? 2,1,1,1,9
?#????..?#?? 2,1,3
????????.??? 1,1
?????#??????.#??#?.? 1,5,1,1,5
..?#?##?????.#??#? 9,2,2
????#????.#. 1,1,3,1
???.?#??##?#? 1,7
?#?????#??? 2,4
.??#???#??#?????# 4,6,1
??..??????# 1,3,1
?????.??.?????# 5,1,3,2
.#?#..????.??????? 3,1,1,1,3
?#?##??????#? 6,1,1
?.#?.#?#?##??..???? 1,1,8,1,1
??#?????##??. 5,4
#??#???##????????# 12,1,1
??#?.????? 2,1,1
#.??#????#?.???? 1,1,4,2,2
??.#????#?#????? 1,2,4,1
????#??.??#? 5,2
?#?#???#?.. 5,3
??.??#??##???##?# 1,3,4,2,1
????..??##??.??? 3,6,3
.???.#??##.#.? 1,5,1,1
?#?????##? 2,2,3
#?.???#??#?#?.? 2,7,1
??#??#??.#?#?#?## 1,3,8
.????.#.?????#? 4,1,2,3
#.???.??#???#??? 1,3,1,1,5
??#.#.???.?????? 2,1,1,1,2
??#?#?.#?#?.##??##? 6,3,2,3
?##??.?##?.???? 2,1,2,1,1
?#?.?.???? 3,1
???????##??????? 5,5
..????.?##?? 2,3
?.??.????#??.??? 1,1,1,4,1
.??????#???#?????? 2,8
..?###???.????????? 3,6
????#?#.?????#????? 2,4,1,1,3,1
??.?.??#??? 1,1,4
????#?#?#?#???# 1,5,1,3
..#???#???.??##???#? 7,1,2,3
??.#?..???#???#. 1,1,1,5
..??????#???? 1,1,2,1
???.??#??.??.? 1,4,2
#?.#???#?. 1,2,3
.????#??#?#??.?# 1,10,2
??#.???#?.. 2,1,2
?.?.???##???#?#? 1,11
???????????#?? 1,7,1,1
#?..#?.?#?#.? 1,1,4
????#????.??##?#??? 1,6,5
???.??#???#.#?# 1,1,6,3
????????.? 3,3
???.?.#??##????? 2,1,1,3,1
..????#.??. 1,1,2
???#??##??.#???..# 10,1,1,1
??????????.?????. 8,2
??????????..?.#...?. 5,1,1,1,1,1
??.????#???.???#? 1,5,1,2
???..???##??##?? 3,9
?#.??.?... 1,2,1
#?????#?##??????#?? 1,1,8,3,1
...?????.? 1,3
?##???##????..? 8,1
?.??????##?? 1,5
#????????#?#?#???. 1,13
?#??.???#??? 1,1,1,1
???#????#????#?? 8,3
.#.###???.#? 1,3,1,1
.?##.?????.#???? 3,3
????..????##?.#??#?# 1,1,1,4,1,4
?????????#??????? 6,1,2
#??##..?##?????? 1,3,6
?#....#?##???#?# 1,10
??##??????.??. 3,1,2,2
???.????#????##?.? 1,2,2,3,1
?????.#?.??. 2,2,2
???###.???#?.??. 4,3,1
?##?#???.?? 6,2
.???.?.?.??????? 1,1,1,4,1
????#????.##?#? 6,5
.??????#?#. 2,3
????.#?#????.?##? 3,5,1,4
?.#?#.???#?#??.??? 1,1,1,7,3
.#?#?????.?.?#?#?.? 4,4
????#????.? 1,4,1
??#?#..#.##?#??? 3,1,1,7
#????##?..??. 1,5,2
???#??.??? 3,1
??.#??.??? 1,1
#?#?###???..?.#?#. 1,8,1,1,1
#...?..??.?#??##?? 1,1,1,6,1
????##??????##...??. 1,8,2,1
.?#????##????#? 1,6,1
??#???..??. 6,1
.#?#.???#???#?# 3,4,1,1
#???#.#?###?## 1,2,1,6
?##?#?#??? 6,1
#??????.#??? 2,2,4
??#?.????#?#???? 3,1,5,1
???????#?#? 1,3
#?..???#?? 2,4
??????.##??#??#?? 1,1,1,8,1
??????????.? 3,1
#???#????..?? 7,1,1
??????.##???..?????. 1,2,5,3,1
????#?#?.???.. 4,2
##?.????#?#??##???? 3,13
.?????.?##?.? 1,3
??..??.????#?? 1,1,6
?.#.???.#?#?????. 1,1,8
?#??..#???? 2,1,1
.###??#???#??# 3,8
?#?#?.???#?.?? 3,5,1
?.?.???.?.???##??.? 2,4
?????#.??????? 1,1,4,1
??.??????..#?#?? 1,3,1,1,1
???#?#??#?..? 2,3,1,1
?.##?#?.??#?#? 4,3,1
#??..??.?#???.. 3,5
?????????#?????? 1,5,1,1,1
??#???????#??? 3,3
#.?.?##????????#?? 1,1,7,1,3
??????.#???????#? 4,3,5
.??#???.#????#? 4,1,5
??#??.???.??? 1,2,1,2
#?#??##??#?##?#.??# 1,8,4,2
.#?????.???##?????? 3,2,8
?????????.??? 2,3,1,1
?????##?.???#?? 4,1,3
??????.??#????????#? 2,1,3,3
#???????#??? 2,5,1
??.??#??#??#?????? 1,1,5,1,2,1
??#??????.?.? 2,1,1,1
#????##?#????? 2,1,6,1
.#?#???#??? 3,5
???????.???.?##??. 1,2,5
?.??.???#???#?? 1,1,2,3
?.##?#??###?.???#?. 1,10,1,3
??????#.????#??? 6,4
????????..##?? 2,2,1,4
.##???????###??#?. 4,11
.???#??????????#??? 1,1,1,1,3,4
???.#??#?.##.?#?? 1,1,3,2,1
?.?#.??#?#??? 2,3
.????.?.???#?# 1,1,1,6
??.#???#?? 1,3
???.?????? 3,2,1
.???????#????#???? 12,1
???????....#??#??#? 2,1,7
#????#?????.?????.? 2,4,1,3
???#??#???? 5,1
?#?..##?#.?? 2,4,1
???#??????##???#?#?. 3,10
#?????.???.??? 3,1,2
###?????##...??. 4,4,1
??????????#.??#?? 8,2
#?.????##..?#??? 2,1,2,1,1
????##??#?...????? 1,6,3
?#?.#?????#???#? 2,1,1,4,1
????.#?##.???????# 2,4,4,1
.??#????#? 4,1
????????##??#?#? 1,1,1,7
##.???#????#???##? 2,8,4
.?#??????. 2,1,1
???.?????.? 1,2
?#?#.???##?##??# 4,8
????????.?#??#???#?. 2,1,4,3
??#??#?.?.??#?##?#?? 6,1,1,5
???#????#?..#?#?# 2,5,5
#??#??#?..?? 7,1
...?#?#??#???.#?? 7,3
???#.???#?#?.??. 2,1,3
?#?#???#??? 4,3,1
?.?##???????????? 6,2
?????.?##?#?? 1,1,7
.#????#?.?#?? 7,1
????##??.?#?#?? 1,2,1,3
.?#??##?.???##? 1,4,3
????.#??.?????? 1,1,3,3
.?#????.??. 3,1
???#??.????#?.?? 4,4
??#????#.?? 2,3
??????.??????? 3,3
????#?#.?#?##?##? 3,8
??.?#.????#???? 1,3,3
#???.???##????#. 1,1,6,1,1
#??????.?###?#??#? 1,5,3,2,1
???###???.?.?#???? 1,3,1,1,4
?????????.#?. 4,1,1
?.????????.?.. 7,1
##???#??#?#??..??. 12,2
..??????.????#.??? 1,5
#?.#?.##?.? 1,1,2
???.????#??#???????? 1,15
?#??.?????? 3,4
?????.?????##??#? 2,1,1,6
??#?##?.?##??? 5,3
#???????????.?#. 1,1,3,3,2
.??#????#?#?#?##? 2,4,6
??????.??##.. 1,4
?????##?????#???#? 1,5,1,2,1
?.#???#?#? 5,1
#?????????? 2,5,1
?#????#?????????##?. 2,5,9
??#???????. 3,1,1
?##?????..###??#?#?? 2,3,3,5
?.#???##???#????? 1,8,1,3
?????#?.???.?? 2,3,1,1
#??#??##?#?##?????# 1,1,9,2
????.?#??#???#?????? 1,2,9,1
??#??#??#.? 7,1
????#????.#????? 7,5
???.?#?#??.???#??#?? 3,3,1,1,4,1
?##??????? 3,2
##.?#??????.?.?? 2,5,1,1,1
####?#???#?.????? 4,2,2,5
?????#?#???#.??#???# 10,1,4,1
?..??#?#.?.?. 5,1
?????...??#.??? 1,2,3,1
#?#?#??.????? 5,1,3
???.????????????. 1,10
?.?###?????.??? 7,1
.??#.????#????.?? 1,1,1,4,1
???###?##???#.??? 8,1
?????#.?#???#.#??? 1,1,1,1,1,3
??#???#??#?#? 1,4,1,1
??.????.??????? 1,1,2
?????????????. 2,5,1
.????#?#???????. 2,11
??.????#?#?#? 1,3,1,1
?????????#??#? 2,1,7
????.#?.??? 2,2,1
??.??????.#??#?. 3,5
???###.?????#??? 1,3,9
???#?????#?..?? 11,1
.??#???????????#? 10,3
??.#???.????????.? 3,4
?##.?#..?????#??. 3,2,7
#?#??????.?.#.???? 1,5,1,1,1,1
..??###??#?????.? 5,7
?.?.?###?##?#???? 1,10,2
?##???????#??????.# 7,3,2,1
????#?#?.? 2,5
?.??.?#.????##?#??. 1,2,6
??#?.#?#?##?#????#. 1,1,1,4,1,4
.###??.?.?.?#? 4,1,1
???#??###?#?.?.??. 10,1
#???????#????#?.#.? 4,2,2,1,1,1
?#????#..??? 1,1,1,1
?#?#???..???.. 7,1,1
???#?#??#?. 6,1
.#???????? 1,4,1
???.???.#?#???#???? 1,1,1,1,6,1
???#..#???####??. 4,3,6
???#??#??????#?# 6,1,2,1
?####?.?.?#??.?#?. 6,4,2
???????????.?? 8,1,1
?#?.?.??.???#?#?# 2,1,7
#?#?#?#?##???###?? 7,2,5
.??##..#???..? 3,1,1,1
?#..?.??.???# 1,1,3
?????.?#??? 1,2,3
.#?#.??.#??.??????? 3,1,1,1,5
?????..?..??? 1,1,1
???????#??#.????.??? 10,3
#?#?#?..?? 3,2,1
?????.#?##??#.? 1,1,5,1
?##?.??.?#?#???? 3,6
..??.????????##? 1,2,1,1,3
?#?..?????. 1,3
??##??.#?.??..# 4,1,1,1
??.???#?##..?##????. 5,3
?.?##?..???.?.? 1,3,2,1,1
..?.??##????# 1,7
???.??.???????#??#?. 1,10
???##?..#?????....?. 4,6,1
??#??.?????. 1,4
???#?????.#?? 4,1,1,2
.?#.?#???.#.???. 2,3,1,2
???#?#??#???##???? 7,4
?#?????###? 2,4
???.#.?????? 2,1,1,1
??#.??####? 1,5
??###?..?##??. 4,3
.????.??####?#? 4,9
.????????. 1,1,1
..????#???#??? 9,1
.???????????#?#??. 5,8
??.????#?? 1,3
?..??#.??# 1,1,1
?##.??#?#??? 2,5,1
.??#????#?? 3,1
.????????????# 6,1,1
.?.?##???##??#?? 1,4,2,4
????????##??.??? 3,1,5,1
.???????##????? 1,2,5,2
???????.?#.? 3,1
?#?..?.????.????# 3,2,5
?#???#?#???#??#?? 7,3,1,1
#??#???..???# 1,1,2,4
?.???#?#?????????..? 5,5
??.??###?#??????. 1,8,1
???#?###??#?????? 1,9,1
.??#?????????#???? 3,4,5
?#??#?????.???# 2,2,4,1,1
?.??#???.???. 1,3,1,1
??#???#.#.?###..#? 1,1,3,1,4,1
##?#.?#??..???##??? 4,1,5
#????##?..?? 2,4,1
.??????..#?#..? 2,2,1,1,1
????.?.#?????##? 1,2,1,1,6
#??#.#????##?. 1,2,8
???##??##?????#?? 4,4,4
????.????#???. 1,1,1,3
??#.#?.??.?#??.??? 1,2,1,2,1,1
???##????.?##??? 8,4
?.?????.##???#???#?? 3,1,3,5
???#??????#??#????#. 1,13
.??#?.????. 1,1,1
??#???.???? 1,1,2
???#####?#????#??.? 9,2,1
#..####?????##??.# 1,8,2,1,1
???##???##???????#.? 1,11,1,1
#???????#?#?.? 1,1,3,4
??.??.????? 1,2,3
??.??##??.? 1,4
.??????#...?? 1,1
##.#?#?.?????#?????? 2,1,1,1,8
????????#..?..???#?. 3,1,1,1,4
?.#??..????#.?.#??# 3,1,2,1,1
??#?#??#????#.?.??. 11,1,1,1
#?#????##??????????? 4,11,1
?????.??.#?#??????? 2,1,9
.?#???.?#?????? 3,7
?#?????.???# 3,1,1,1
???.?????#..? 1,1,2,1
##???##?.??? 3,3
.????##?#?#????#.?.. 7,6
?.???###??.?##? 6,3
#?.#?#??????#????#?. 1,1,1,1,6
?#??#????????? 4,1,2
?.??..???#?...??.? 4,1
.?????..?.??#??. 2,2
?????##??#???? 9,2
????#????????#?#???? 5,11
????.????? 2,2
??.???.??? 1,1,1
?#???#..????? 2,1,1,1
????.??##? 3,3
.?#???#????? 2,1,3
.#?#?#??#??.#???#? 9,1,1
???#??#??##?????# 11,1
..?..????.#?#?#?. 1,1,5
?.??????.? 1,1,1
.??#??#???? 7,1
#?.#..??????????# 2,1,9,1
???.???.???.?? 1,1,2,2
?#???#????#?##?????. 2,9,2
#????.###??.??? 1,2,5,1,1
.#..????????# 1,2,5
?.#????#???.#?.##? 1,1,4,1,1,2
?#????#?.#.#?.. 2,1,3,1,1
?#.?.#??#. 2,1,4
?#???.??#? 1,1,1
?????#?#.???#?????# 7,7,1
.#?#.?.??.##??? 3,1,1,5
??.?#??.???#.? 2,4
?.???????? 2,3
??????..????? 1,1,1,3
?#?#?#????..?? 5,1
..##??.?##. 3,3
?##.???#?#. 3,4
?..#.?.???##???### 1,1,1,1,9
#??#?.??##????? 4,9
.???????.#? 2,1,2
???????..??.? 4,1,1
????.?????.?.?? 2,1,1,1,1
?#??.?##???.?#??? 2,5,5
.???#??.??#?##?. 3,5
#.??????#??????.?#? 1,10,2
??#??#?????#?? 2,2,1,3
?.???????????. 1,1,1,3
.???#?.#??? 1,2,3
?????#???????# 8,2
??.??.#??.#????#??? 1,1,1,1,1,5
??#?#????.#??????.? 1,4,1,1,1,1
.?????#??#?.??. 2,6,1
?.#?##?#?##?. 6,2
??#?#?##???.?????. 10,1,1
?#??#?????## 4,1,2
??..????#???????#?? 2,7,4
??#????????.#.? 2,1,4,1,1
??#???#..#?#?##? 1,2,2,1,5
#?????#.????. 7,3
?.?.#?##???#??..?.? 1,1,10,1
??##.#???.??#.? 3,2,1,1,1
???.?#???. 1,2,1
??.?.?#???## 2,1,1,4
#?.#????#??? 2,7
???????.???????#??? 4,6,1
.???#.?..? 1,1,1
.??#.????#????? 1,1,3,1
???.#??????#?#??#.? 2,10
..#?#?.?????#.? 1,1,1,4,1
##???#????. 6,2
..??.?##?.?#?? 2,3,2
.?.??????###???.??#? 1,9,1,3
?.?.??.#.?#. 1,2,1,2
.#?#??#?.?##.?.#?#?? 4,1,2,3
.??###???#?#????? 3,6
?.#???????#??#. 1,2,4,2,1
?#?????#?.??#?. 2,1,1,3
?????.#?.??#????? 3,2,5,1
??.###????? 1,3,2
.????????#??.?????? 1,2,1,2,1,5
?.???.???###?##.. 1,9
#??????#.?? 2,5,1
##??????????..???? 4,1,2,4
??..?##.??.??#?? 2,3,1,4
.#?.???????#??. 1,8
#?#?..????#? 1,1,2,1
?#?#.?##??? 1,1,6
??#??##???#??? 4,3,1
.???#????# 4,1
#?????????###??? 1,1,1,4,1
??#?#?????.?#.?????# 10,1,2,3
.????#.?#?.?.?? 2,1,3,1,1
???????#?#??#??.? 1,10,1
#??.????#. 2,1,1
?.??.???#.? 1,1,2
..????#???????? 9,1,1
????????#?#??#?? 4,4,2
?#??..###?##? 3,6
???#?????? 1,1,2
#??#??..??.?.?#? 6,1,1,3
??#?.##???.??# 1,3,3
????###??????. 6,1
##??###??####?..??? 14,2
???.#????? 1,3
??.?.???..?. 2,1,1,1
.?#.??#?..???#??? 1,4,3,1
??.??.????????? 1,1,3,5
#?##?????.??.#?????# 9,1,2,2,1
?#???.??.#????#?#?? 5,10
???.?????..??.#.?.?. 5,1
??#?.#?#?# 2,5
#?#????#??.??.##? 8,2
.?.?.?#??##?.#.??#?? 1,1,7,1,1,3
????#?#??.?#???# 6,6
??.#?#??#?#??????? 1,1,8,3
????.????#??#? 1,1,1,6
?.?.?##?##??#.?? 1,3,2,1,2
.???.?#?##???? 1,7
?#.?????#??. 1,2
?#.????.???#?#??#?# 1,1,1,1,9
#?.#.??#???????.???. 1,1,4,2,1,3
?#.???????.#?#?# 1,1,1,1,3
.??..##.??#??##? 2,2,2,2
?.?#?..##?.?.. 1,2
?????#?.????? 1,3,3
##??..?????#?? 4,1,2
#..?###????.? 1,4,1
?#?#???????#??. 3,7
?#?.???#??.??. 1,4,2
???#.#?##??.?##??##? 4,1,4,7
???????#..? 4,1,1
???#?????#??#?.? 2,8
..?#.??##???#?.?.. 1,9
????##??.?? 4,2
??##??#?..???##?#?#? 6,8
?.##.?.??? 2,1
.??.????#?. 1,5
?#??.#?#????????# 3,4,3,1
??#.?.?..? 2,1,1
#????????#???.##?#?. 1,6,1,5
??.?#?.#??#??????? 2,4,6
??????#???? 6,1
?????#??????##.??.. 3,6
???????##???#??.#.?? 10,2,1,1,1
.????????????#??? 1,1,10
???????##???#????? 1,1,5,4,1
.??#.?#?.???.#.?#??? 3,2,1,1,4
???..##??? 2,4
??##???#.??.#? 8,2,1
.??.??.?##??..??#? 2,5,1,1
??.???????#??#??.?? 1,2,8,1
..#?????#??.??#. 7,2
?#????#?#??#? 2,3,1,2
???#??#????#??#?.? 9,1,2,1
?.??.????. 2,3
?.???#????#.????#??? 1,1,1,1,1,5
?.?##?#.??.??#?? 5,1
?#??###???# 7,1
#?????..??? 3,1,3
?.???..??## 2,4
.?#????.?#.?.# 3,2,1,1
??#??#.#??????#?#??? 5,2,8
??.???..???##. 2,3,1,3
???????#?# 1,4
??#?.?????#?#?#???. 2,12
??.?#???#?##.?#?? 1,8,2,1
??????????..?? 2,1
??????#????? 1,5
???.??###.? 4,1
???##????#?????? 3,1,3,3
???.???#???? 1,5
#???????.?#?#?#??? 5,1,7,1
#??#???#????????.?? 1,1,4,1,2,1
.?#?..?????????#?. 2,2,6
??..??.?.. 1,2
????.#?????????###?. 1,2,1,12
#?#?##??#.?.?. 9,1
????????#??#??? 4,7
?#????#???? 3,4,1
??????#??? 1,2,1
#??#.??.?# 4,1,1
?.?????#?# 1,6
#?#?.??#???????.?? 1,2,1,1,4,2
?????????.???? 2,5,3
?#??##?.?#??##??# 1,3,5,1
??#?#.?#?..#?? 3,2,1,1
??????#??.? 3,1,1
?.?????#????..###??. 6,4
?##??#????.??. 7,1,1
#.?????????# 1,1,1,1
.??#..#??.???? 3,3,1
.????#?##?#???? 7,2
???????#???#? 2,1,2,2
?..#?????# 1,4,1
???.#?#..??# 1,3,1,1
???.#????#???????.? 1,3,2,1,1,2
#???.??#.??.?#???. 1,1,2,1,2,1
#?????.?.?????? 1,2,1,1,5
??????.???..#?#??? 3,1,1,3,1
??#????????#??#??? 8,3,1,1
??.?#?#???##..?#?? 2,4,1,2,2,1
??#???????..?? 3,5,1
.???##?.???????.? 4,4
???#??????? 3,4
#.???????# 1,1,1
#?####..#?# 6,3
.??#???.?????????.. 5,5,3
?????#.?????#?#.?# 1,3,4,2
?#????#.?#?# 1,4,2,1
??#???##???.#?????? 9,1,1,2
.?#??????? 1,2,2
????????###?????. 5,4,4
?#?##??..#?? 7,3
??#?.?????#?? 2,7
..??.?...??. 1,1,2
??.???#??.?#??? 1,2,2,2,1
???#?.???? 4,1
???#??#??#?#?#?###? 1,16
??.????#?.#??.. 1,2,2,3
???#??????##???? 4,6
##?.??.?#?? 2,1,2
??.##?#?#?.?#??. 1,7,1
??#?#??#??#????.?#? 1,13,2
????###????.????.?#? 9,1,1,1,3
??#?#???#????????#. 1,1,1,1,1,8
.#??#????.?####? 5,5
..#??##???? 1,7
.????#?#?#?#.#?#?#?? 9,6
?????..????? 1,2
???????#?#??#??.?# 1,11,2
.?.??????#???#????? 1,1,7,1,1
.???.??##?#?. 1,6
.??#???.??????? 2,2,1,4
#??..#??##?##???? 3,1,2,3,1
.?#?#??#?#?#???? 11,1
?#?#?????????.?#?# 5,1,2,3
?##???#????#? 8,1
.##?????????..? 2,1,2,1,1
???????????????????# 3,8,1,1,2
??##????..###. 5,3
.?###??????#?? 7,2
?.?..#??.#?#?.## 1,1,1,3,2
???..???#.?????##?? 2,4,2,5
.???.?????. 1,1
?#????#???.?? 2,4,1
?.??#.??.??# 1,1,1,1
?#?????#??????.??? 10,1,2
.????###??#???..?.?. 10,1,1,1
.???##?.????..?#??? 5,1,1,3,1
?##?#?????#??.? 2,3,4,1
???#??#??###?# 1,1,9
?????.?#?#??????## 4,2,1,1,2,2
.#???..???###????? 1,1,1,5,1
?#?#???????# 1,1,4,1
.?#???????#.#?.??.? 7,1,1,1,1
??????#....#??#..#?? 5,4,3
??????#?#??? 1,1,2,1
.####???#..#????#??? 8,2,3,1
.#?#.????.? 3,2
.#?????.#?####??? 2,1,1,7
#????.?#??#?#..? 1,2,2,3
????..???? 1,4
.?###.?#??????. 4,5,1
.???#.???.? 2,1,1
??????#?.?.?.?.???#. 1,1,3,1,1,4
?#????..???.. 2,1,3
?.??#????.?##?? 1,6,4
?#?????.##??#?. 4,6
??##?????..#? 9,1
??.???..??#??# 3,4
??????..??#. 1,1,1,2
?#????.???.? 1,1,1,1
??????????#?# 1,1,8
#.??#??#???.#???#? 1,3,1,1,5
#.???????.?? 1,1,4,2
?#..????.???.#?? 2,1,1,1,3
???.?.?#?#???. 1,1,3,1
.#?#??????#??.? 7,2
????.?.????? 3,1,1,1
?.????#??##???? 3,6
???????#??.. 1,1,1
???.??#?.???? 2,3,1,1
.????#?.?#.??.???? 1,1,2,2,2,1
???#?#??.. 1,3
#?#??????????? 8,3
.?##..#??????.##? 3,7,2
????#.?####??#??? 1,1,7,1
?##??#??#?##?#?## 6,9
.????#??.??? 7,1
???##?.#??#???.#.? 4,7,1
???????#?????###? 1,11
????.???.?#.? 1,1,2
???????#?##??#?#??#? 1,1,1,5,7
???.??##??####.. 5,4
????????????. 2,4,2
??????#??? 1,1
?#.?????.. 1,1,1
.???#??#??#?????. 1,6,1,3
#???.#?.#??? 3,2,1,1
?.??#?#???.??????? 3,2
?.????#?##?#?..? 1,2,7
?#?????????.?#?.? 2,1,2,3,1
#???????.? 4,1,1
#???#.?#?? 2,1,2
?..????.###????? 1,1,7
.#?#???#??? 5,3
.#?.?????#?##?..#?# 1,2,1,3,1,1
??#??#?#???.??? 8,1,3
.?#?#?#??#..?? 6,1,1
??#??.?#??? 3,2
?????#?##??.??. 1,6,1
??#?#???## 5,2
??????#????##??? 1,7
.?##?..??. 2,2
??#??#??.??????? 5,5
.?#?#??????.? 3,2
?#???###?..??? 7,1
??????????? 1,2,1
??????#.#???.???? 1,3,1,1,4
??#..#?#?#?.??#?. 3,1,4,1,2
?#?#??###?????.?? 1,9,1
???#??#??#????? 1,5,1,1,1
?#???##???...?.?#? 9,2
??#???#???#?.?.#?. 2,1,6,1,2
??.????..?.? 2,1,1,1
???????????? 6,2
?.????#?#????#??#?? 2,1,1,1,4,1
.???????#?? 1,3
??????#??#???#.?#?#? 1,1,2,6,2,2
?#???.????.??.?? 2,3,2,1
???##..??????#?? 1,2,1,5
???????.?#??????# 6,6,1
??????????? 2,4,1
??#.???#?# 1,3
???.?????? 1,6
??#.????.? 1,1,1
??????#?#..??####?? 7,1,6
..?..??????#????? 1,1,7,1
?????#.#?????#????#? 6,2,7
???.????????? 1,6,2
#??##??#??##?. 1,2,2,2
?????????.?#?????? 1,1,1,5,1
.??.??..?#??##?## 1,1,2,2,2
??#?##???.? 4,1
???#??.?..???????... 3,5
???.#?#?#.? 2,3,1
.?????#???####.#.?? 1,3,4,1,1
?#???#???.??? 2,1,1,1
?????????.? 1,4
..??.??..???##?#??.? 2,2,1,6,1
#??#?#??#..?#?????? 9,3,1
??????.???#.???? 1,3,4,1,1
???#?????????? 2,1,4
???????##???#?#??#?. 1,13
##???????? 2,1,3
#.#????##????#??# 1,7,4,1
???.??.???#? 1,1,3
.??????#.????????#?? 7,1,1,1,1,1
?..?#????? 3,1
?..?.#????#????#?? 1,1,9,1
??.?.?.?#???#?? 1,1,2,1,1
?.????.???##?#?#?#?? 1,11
??????#???.# 2,1,3,1
.?????????##?. 4,5
?.???????.???#??#. 3,1,5
??#?#.???.?.???##?? 4,1,1,6
?#?#???#?????.####?? 12,6
##????#???? 3,3
??????###?? 1,5
?.?#?#?????##????? 12,2
??#?.#.?.????#??#?. 1,1,2,6
???.???#?#???.?## 1,1,4,1,3
?.??????????.???? 1,2,4,1,2
..?#??.????? 2,2
?#.??.?????#??# 1,1,1,3,2
?##??.?#????#?# 4,4,3
?..#??#???.#??#? 4,5
??.??????? 1,2
?#??..#???????..?? 2,6,2
.#????.????#?#????? 1,1,1,8,1
#?#???#??#???#?????? 7,9,1
?.##?#??.? 4,1
#?##?.????.##?.. 4,1,3
.?#?.???##?. 3,4
#.???##?????.#. 1,5,3,1
?????#?#?#??.?#??. 10,3
?.?#..??.#??#??????? 1,2,1,7,1,1
#####??##???.??????? 10,1,1,2,1
???.????##????#.## 2,1,9,2
.#?.?..??#?#?.. 2,4
##?#..?#??#?# 4,6
##?#???..#?#.?## 5,1,3,2
??#..#??##.. 3,1,2
??????.??.???. 1,4,1,2
?.????????#??#?#??? 1,1,1,1,8
#?##?????#???#.????? 14,1,2
??###.??????.?###?? 4,1,1,3,1
???????.???. 3,2
?#??##????.????.#.?? 2,2,1,4,1,1
.#?????.?????? 1,3,2,3
?##????.?? 4,2
#.##.?????###???? 1,2,9
???##??#.?#? 4,1,1
??##???#????? 3,3
?#???#?????.???#???? 10,1,1,1
?#??..#.?.#? 2,1,1,2
??????.??.##?#?? 1,1,1,2,2
??###????????. 5,1
????##???#.???? 6,1,1,1
.?.????##?? 1,1,3
.#??.???..????#.???. 2,2,2,1,3
?????.???#?##???. 1,1,4,2,1
.??#?.??#???#.? 1,2,3,1
..???????????????? 3,4
???#.?????. 4,1
?..????#???.??...? 1,7,2,1
???????#??#?#? 4,6
.?#???.?##???#?.## 4,7,2
#??.??#?.???. 3,2
???#???????#?.?#? 1,1,5,2
#.???###??.?##???#? 1,1,4,7
???#??.??????.??#.. 4,3
????.#?#?##.##???? 1,6,3
?#.??????? 1,6
#???##?#?..??????.?? 1,7,1,1,1,1
?????????.#? 1,1,1,1
.?..?#?##?? 5,1
..???????????? 2,8
...??.?..?#?#? 1,3
??#??#???????.?? 7,1,1
????#.???#?###.?? 5,8
.????####??#??.????? 11,2
?.??????????...?? 1,2,1,2,1
?.?##??????.?..#. 6,1
#??.?????????.? 3,1,3,1
???.#??#????.?. 2,7
???.#?.?.?#?#???? 2,1,1,2,5
??????.??##?.?.#?..? 2,4,2
?????#?????.????#? 11,5
?##.??????.??#?##?? 3,3,1,1,4,1
???.??#????#?????? 4,5
?.?.?.#?#??.??? 1,1,5,1
.?.??##???##. 6,2
.?????.#?. 2,1
..???.?.???##?#?? 1,1,1,8
??#??#??#??#?#?#?. 9,6
...????.????.???? 1,3
?#???.??.##?#???? 2,1,1,7
.#?.??#???#???#?? 2,1,5,1,3
#???.#??#. 1,1,1
#????????#?#??.#?.? 1,1,9,1,1
????#???????#? 2,3,4
.????#?.??? 6,1
.??.???##?#..?? 1,5,1
?#?????#??#.???#??# 6,2,1,1,1,2
.?????#?##..#??# 9,1,1
?#???.??#.????????? 4,1,5
???????#???#.?..??? 5,2,1,1,2
.???##?.?#? 6,2
??#???#???#?????? 3,11
????##??##.????#.? 9,4,1
'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

mem={}
def recM(a, b, aPos, bPos):
	key = (aPos, bPos)
	if key in mem:
		return mem[key]
	output=rec(a, b, aPos, bPos)
	mem[key]=output
	return output
def rec(a, b, aPos, bPos):
	if bPos==len(b):
		for i in range(aPos, len(a)):
			if a[i]=='#':
				return 0
		return 1

	output=0
	for aPosTry in range(aPos, len(a)-b[bPos]):
		for i in range(aPos, aPosTry):
			if a[i]=='#':
				break
		else:
			for i in range(aPosTry, aPosTry+b[bPos]):
				if a[i]=='.':
					break
			else:
				if a[aPosTry+b[bPos]]!='#':
					output+=recM(a, b, aPosTry+b[bPos]+1, bPos+1)
	return output



answer=0
for line in data:
	a,b=line.split(' ')
	b=','.join(b for i in range(5))
	b=b.split(',')
	b=[int(b) for b in b]
	a=[a for a in '?'.join([a for i in range(5)])+'.']
	mem={}
	out=rec(a,b, 0, 0)
	print(out)
	answer+=out
print(answer)



#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())

#data = [[column for column in line] for line in data]
#W,H=len(data[0]), len(data)
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

# def rec(a, b, pos, bPos, run):
# 	if pos==len(a):
# 		return 1 if bPos == len(b) else 0
# 	elif a[pos]=='?':
# 		left=rec(a, b, pos + 1, bPos, run + 1)
# 		right=0
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				right = rec(a, b, pos + 1, bPos + 1, 0)
# 			else:
# 				right = 0
# 		else:
# 			right = rec(a, b, pos + 1, bPos, 0)
# 		return left+right
# 	elif a[pos]=='#':
# 		return rec(a, b, pos + 1, bPos, run + 1)
# 	elif a[pos]=='.':
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				return rec(a, b, pos + 1, bPos + 1, 0)
# 			else:
# 				return 0
# 		return rec(a, b, pos + 1, bPos, 0)
#
# answer=0
# for line in data:
# 	a,b=line.split(' ')
# 	b=b.split(',')
# 	b=[int(b) for b in b]
# 	a=a+'.'
# 	a=[a for a in a]
# 	answer+=rec(a,b, 0, 0, 0)
# print(answer)

# def rec(a, b, pos, bPos, run, aMin, aMax, bRight):
# 	if run > b[bPos] if bPos < len(b) else 0:
# 		return 0
# 	if pos==len(a):
# 		return 1 if bPos == len(b) else 0
# 	elif a[pos]=='?':
# 		left=rec(a, b, pos + 1, bPos, run + 1, aMin, aMax, bRight)
# 		right=0
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				bPos += 1
# 				br = bRight[bPos] if bPos < len(b) else 0
# 				if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 					right = 0
# 				else:
# 					right = rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
# 			else:
# 				right = 0
# 		else:
# 			br = bRight[bPos] if bPos < len(b) else 0
# 			if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 				right = 0
# 			else:
# 				right = rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
# 		return left+right
# 	elif a[pos]=='#':
# 		return rec(a, b, pos + 1, bPos, run + 1, aMin, aMax, bRight)
# 	elif a[pos]=='.':
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				bPos+=1
# 				br = bRight[bPos] if bPos < len(b) else 0
# 				if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 					return 0
# 				return rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
# 			else:
# 				return 0
# 		br = bRight[bPos] if bPos < len(b) else 0
# 		if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 			return 0
# 		return rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
#
# answer=0
# for line in data:
# 	a,b=line.split(' ')
# 	b=','.join(b for i in range(5))
# 	b=b.split(',')
# 	b=[int(b) for b in b]
# 	a=[a for a in '?'.join([a for i in range(5)])+'.']
# 	aMin=[sum([a[i]=='#' for i in range(j,len(a))]) for j in range(len(a)+1)]
# 	aMax = [sum([a[i] != '.' for i in range(j, len(a))]) for j in range(len(a)+1)]
# 	bRight = [sum(b[i] for i in range(j, len(b))) for j in range(len(b))]
# 	print(a)
# 	print(aMin)
# 	print(aMax)
# 	print(bRight)
# 	answer+=rec(a,b, 0, 0, 0, aMin, aMax, bRight)
# print(answer)
