#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''.strip('\n').splitlines()
data2='''
Card   1: 72 42 34  7 30  3 25 63 99 15 | 63 30 64 15 72 55 73 32 75 41 37 77 49 51 95 16 25  3 92 18 87  2 71 28 10
Card   2: 52 89 94 79 81 30 58 77 69  2 | 94 77 35 81 96 52 84 85 69 51 78 24  2 41 37 30 44 57 48 14 33 89 58  5 79
Card   3: 93 12 23 20 64 72  3 32 25 27 | 23 35 36 69 38 12 74 57 20 93 72 41 88  6 25 37 32 76 27 64 81 83 40  3 54
Card   4: 68 36 31 91 12 19 75 32 33 52 | 77 75 12 54 32 59 52 36 19 40 55 31 71 11 84 91 16  7 42 95 68 33 47 67 65
Card   5: 68 39 51 95 10 77  5 36 75 99 | 86 94  1 99 96 68 98 77 25 95 32 20 97 75 28  5 10 51  6 36 14 78 66 29 39
Card   6: 60 53 10 26 45 64 31 88 74 21 | 36 35 11 17 18 47 86 59 28  8 32 21 22 31 77 88  9 16 23 74 26 87 75 95 12
Card   7: 95 93 28 80 39 62 74 91 22 63 | 42 39 33 44 94 52 77 95 38 65 84 92 61 91 73  8 96 51 37 71 58  5 81 22 93
Card   8: 76  7 55  3 95 17 24 23 69 47 |  8 41 67 46 29 18  2 82 86 59 88 22 98 25 95 15 57 26 63  3 36 85  7 24 20
Card   9: 63 60 87 27 47 40 26 38 34 57 | 42  1 28 34 12 98 64 37 33 49  3 87 77 46 26 20 38  4 32 79 45 60 35 57 48
Card  10: 30 16 56 17 48 44 65 76 27 61 | 52  8 35 90 41 64  4 55 77  1 49 80 75 95 16 61 85 31 73 97 93  9 76 66 54
Card  11: 28  7 64 33 13 45 97 24 66 51 | 97 46 24 76 28 31 74 65 13 23  1 30 27 15  3 18 12 51 25 33 64 75 66  7 44
Card  12: 57 89 67 77 23 49 12 96 43  4 | 56 67 25  6 29 34 72 23 41 96 89 61 40 60 87 20 57 46  5 49 69 48 47 10 43
Card  13: 27 58 48 17 10 23 40 79 61 71 | 90 57 48 81 17  1 86 58 23  8 21 20  3 35 29 71 53 78 79 15 60 61 41 22 10
Card  14: 16  8 76 31 64 95 61 14 59 58 | 79 48 62 88 99 82 49 52 66 16 30  1  8 29 98 31 91 38 96 55 51 27 65 93 36
Card  15: 46 39 99 29 88 81 26 42 77 75 | 94 85 34 19 99 54 26 32 56 74 29 28 18 47 81 55 79 17 41 45 46 68 77  4 73
Card  16:  7 10 45 37 11 83  2 78 69 73 | 71 21 32 92 31 25 12 61 19  1  7 20 97 43 64 40 16 55 83 51 53 36 38 69 93
Card  17: 37  8 68 43 21 50 25  4 99 63 | 34 57 66  8 88 16 55 62 32  5 43 19 36 18 12 92 10 73 65 56 77 94 44 39 58
Card  18: 72 99 36 80 48 63 77 75 84 25 | 45 16 71 32 72 64 23 48 88 68 75 77 38  8 84 89 79 41 73 10 51 44 47 29 20
Card  19: 69 78 70 25 84 71 48 52 18  6 | 21 84 13 27 55 34  2  3 14 16 35 44 93 62 46  6 70 99 31 10 68 65 78 61 92
Card  20: 72  8 64 15 20 91  9 73 54 83 | 21 48 56 65 17 44 66 20 68 29 63 30 67  7 18 24 32 85 12 60 11 23 70 35 93
Card  21: 86 13 97 67 60 50 89 56 90 78 | 71 74 38 87 92 39 50 80 61 26 15 53 60 72 46 54  6  7 55 19 37  1  9 20 94
Card  22: 99 41 71 28 23 88 93 94  1 37 | 38  6 79  4 26 47 61 84 52  3 70 43 76 35 32 51 11 49 39 72 60 85 89 25 57
Card  23: 85 24 78 46 99 29 75 55 64 70 | 67 71 16 43 83 47 59  7 34 97 17 62 10  2 36 39 37 38 92 58 42  4 84  3 96
Card  24: 55 60 83 42  8 31 14 30 96 50 | 48 30 88 77  4 29 33 46 21 28 44 71 78 99 84  2 73 45 31 85  9 91  1 86 55
Card  25: 86 39 53 63 74 15 23 16 78 95 | 84 10 32 48 56 92 60 99 37 90 27 96 53 98 19 28 85 49 64 45 59 17 41 24 42
Card  26: 85 27 96 10  6 24 16 15 26  1 | 21 62 61 69 22 81 64 56 95 30 11 76 74 31 73 57 89 27 32 68 67  2 98 71 49
Card  27: 72 99 45 96 53 86 22 92 95 49 | 78 59 30 92 66 95 55 23 85 99 24 45 38 53 79 36 18 70 22 98 47 16 76 49 96
Card  28: 21 35 15 99 47 92 32 64 69 97 | 18 64  2 92 96 57 84 37 34 15 32 36 99 97 69 68 35 43 40 73 21 47 83 67 46
Card  29: 40 88 58 51  2 32 95 26 99 17 | 68 23  7 20  9 64 28 26 72 51 17 65 58 88 87 67 95 21 48 63 32  2 40 99 25
Card  30: 99 65 22 27 36  7 71 54 73 98 | 73 87 35 74 45 68  7 80  4 47 65 71 22 42 91 34  5 62 94 60 23 27 96 89 79
Card  31: 64 26 13 16 63 79 86 88 18 28 | 77 25 80 88 79 30 14 13 65 90 31 28 81 60 18 95 11 39 41 93 82 33 92 96 16
Card  32: 56 82 36  7  6 29 33 90 65 96 | 68 59 25 15 28 20 67 16 51 29  3 11 81 63 84 77 44 41 24 30 33 90 61 72 43
Card  33: 23 59 37 55  3 41 28 17 78 32 |  4 71 66 76 89 93 75 91 88 90  3 17 53 73 28 45 37 60 32 23 58 36 40 22 84
Card  34:  2 18 26  6 49 77 64 59 50 66 | 87 18 41 79 54 26  6 22 27 49 82 83 50 38 44 59 81 36 89 66 15 53 42  9 28
Card  35: 81 48 43 63 21 96 91 68 78 39 | 41  7 82 39 99 46 49 29 48 70 91 25 14 54 87  9 96  4 30 76 28 67 40 73 20
Card  36: 15 66 40 86 77 70 64 30  4 85 | 72 83 81 93 12 97 74 37 15 20 84 28 56 73 92 39 77 70 43 55 58 40 69  2 96
Card  37: 38 22 88 47 39 42  8  9 53 48 | 20 87  9 33 28 31 72 42 74 49 79  4 13 44 77 50 54 81 63 65 36 24 64 26 89
Card  38: 28 72 56 37 77 49 58 57 31 85 | 87  1 97 69 89 45 26 91 96 39 79 46 85 49 25 22 18 35 59 38 23 47 67 53  2
Card  39: 23 86 32 13 71 95  2 96 72 55 | 24 54 80 28 63 39 88  6 38 87 70 23 97 18 52 35  1 61 50 29 58  5 93 21 40
Card  40:  7 45 40 49 94 46 42 53 59  4 | 25 57 76 40 81 11  9 77 43 92  1 61 10 30 47 28 50 31 22 12 84 90 80 74 62
Card  41: 60 79  1 38 65 63 91 25 68 16 | 89 62 70 30 21 84 88 72  6 36 27 80 20 35 85 76 96 18 13  2 12 92 41 64 49
Card  42: 74 42 13 34 14 88 36  4 92  2 | 79 91 47 46 32 66 39 40 24  6 52 31 65 22 71  1 60 96 75 16 69 89 26 41 11
Card  43: 54 35 52 10 78 62 14 26 31 61 | 57 55 27 68  8 49 37 70 51 88 17 25 38 11 22 94 64 99 30 12 92 42 69 18 36
Card  44: 89 80 79 10 39 23 71  4 94 31 | 35 81 20 42 63 89 98  5 48 41 15  6 32 56 51 70  3 95 59 87 62 72 18 38  8
Card  45: 57 25  8 54 47 39 88  9 61 97 | 23 30 13 97 27 52 45 51 82  9 99 86 85 92 70 65 43 41 69 12 90 46 39 21 91
Card  46: 74 39 41 36 98 35 30 44 52 88 | 76 42 17 66 81 71 78 40 93 18 45 36 43 29 95 70 57 26 79 28 98 94 33 12 13
Card  47: 70 61 84 72  4 11 63  3 62 97 | 63 70 88  4 18 24 80 81 56 52 84  2 94 67 41 59 77 62 12 38 60 11 92 15 58
Card  48:  1 70 80 88 71 76 31 98 53 27 | 90 85 45 15 13 23 98 59 37 83 89 91 71 63 82 93 35 32  4 16 64 48 10 58 50
Card  49: 26 45 20  8 85  9  6 97 55 42 | 27 18 68 29 74 59 51 60 87 45  6 67 53 10 72 41  2 84 56 92 30 73 71 42 69
Card  50: 69  1 66 37 88 61 90 58 33 20 | 60 23 71 86  8 95 68 11 67 53 20 35 78 29 48 57 63 69 51  9 43 44 81 25 16
Card  51: 50 30 42 54 28 27 66 26 85 76 | 85 69 68 73 18 49 27 20 16 92 57 37 62 65 75 89 22 99  3 94 31  7 48 70 17
Card  52: 10 93 26 70 17 15 51 90 92 47 | 81 32  4 50 34  2 13 94 33  9 31 35 57 17 86 47 98 85 28 46  7 76 42 83 77
Card  53: 83 36 87 78 79 72 20 99 88 58 | 92 61  4 35 17 36 78 87 25  6 26 97 24 11 89 77 71 39 38 96 22 65 19 10 76
Card  54: 90 13 49 20 35  7 27 46 70 19 | 75 50 84 21 47 56 49  1 41 34 78 86 53 24 36 20 64 13 14  2 16 18 65 54 32
Card  55: 54  7 69 14 56 41 42 65 70  2 | 67 30  4 83 16 12 35 13 92 80 39 52 58  8 15  5 43 29 27 75 53 26 50 89 37
Card  56: 30  6 69 51 65 71 79 35 48 98 | 21 70 11 66 54 42 55 99 18  1 56 63 88 39 86 24 46 67 29 15 44 76 65 37 28
Card  57: 84 79 10 11 50 30 36 65 28 19 | 62 97  7 70  5  9  3 47 20 18 52 35 26 48 59 75 89 91 71 32 34 22 72 16 46
Card  58: 78  9  2  4 14 64 43 34  1 31 |  9 78 61 64 74 43 38 46 20 34  6 84 14 69  2 12 36 42  7  4 51  1 37 31 82
Card  59: 45 81  5 80 50 95 82 16 44 99 | 20 10 55 92 49 39  6 90 81 76 35 54 11 82 80 61 68 23 47 60 88  5 99 96 64
Card  60: 81 26 27 19 54 33 40 11  5 90 | 76 49 33 53 54 79 21 27 35 26 56 11 81 80  5 15 50 90 40 48 87 31 24 19 23
Card  61: 70 65 80 25 30  4 12 71 43 85 | 80 71 97 99 90 27 13 20 16 19 10 61 25 43 49 94 39  4 30 70 12 57 65 85 14
Card  62: 91 52 22 30 60 54 67 83 88 34 | 78 68 37 73 69 92 87 48 44 88 13 91 60 12 72 36 54 14 22 61 67 83 30 52 34
Card  63: 94 41 79 25 24  9 10 42 48 49 | 69 63 66 40 53 94 97 82 80 64 48 99  3 79 41 68 62 30  9 74 59 49 20 52 65
Card  64:  6 68  2 74 31 97  4 71 78  1 | 85 31 78 61 12 71 19  6  4 79 87 15 48  1 27  2 14 29 37 30 97 74 94 68 70
Card  65:  3 56 52 75 44 78 94 87 55 60 | 99 61  1 18 76 23 92  2 43 41 37 93 29 22 19 59 53 17 46 38 13 90 34  9 62
Card  66: 42 76 77 85 81 26 27 38 35 23 | 29  6 25 81 85 89 70 65 30 96 44 91 11 15 60 99 87 27 79 54  7 63 26 76 37
Card  67: 94 13 63 52 10 18 38 80 32 70 | 61 52  8 10 55 80 18 93 15 62 63 32 70 42  2  1 38 13 94 25 59 47 30 91  5
Card  68: 91 60 34 79 36 82 31 43 76  9 | 79 76 60 91 98 64 25 15 24  4 40 31 88  9 97 43  7 19 36  3 87 13 82 34 39
Card  69: 93 70 98 45 55 72 95 66 29 54 | 72 26 55 69 71 95 29 54 93 77 98 73 78 35 94 60 30 10 47 89 59 43  2  8 17
Card  70: 25 74 47 31 15 57 13 67 26 28 |  5 47 85 26 45 89  9 94 78 17 50 52 42  4 72 16 23 67 22 73 58 55 70 32 28
Card  71: 56  4 53 46 94 29 83 30 89  7 | 58 63 84 38 92 21 74 69 30  4 78 89 44 93 40 29 17 52  7 68 47 46 96 82 13
Card  72: 40 90 82 26 33 71 61 77  2 95 | 73 49 89 41 99 91 88 56 44 70 52 54 55  4 93 81 85  6 23 29 64 69 26 18  7
Card  73:  5 19  1 59 68 41 42 63 76 98 | 90 44 72 76 67 21 80 69 29 13  8 54 51 35 70 40 52 89 48 78 84 74  3 22  4
Card  74: 80 76 25 96 50 97 31 65 17 26 | 79 15 91  7 89  4 55 26 14 92 76 25 77 96 72 50 37 13 94  2  6 63  3 35 65
Card  75: 48 44 75 19 64 15  7 84 80 23 | 23 47 24  9 28 18 55  5 30 12 88 74 75 68 19 43 57 73 35 62 97 44 72 54  4
Card  76: 24 58 72 12 78  4 47 26 38 37 | 90 93 34 65 88 48 16 56 13 81 51 59 67  6 28 75  8 85 11 74 47 70 77 41 58
Card  77: 69  1  9 22 48 37 92 23 87 89 | 67 45 38 62 90 13 31 34  2 53 23 16 52 27  8 47 54 88 77 78 73 24 32 95 17
Card  78: 32  2 69 81 63 27 71 40 87 64 | 86 75 53 43 29 44  7  4 78 13 15 80 70 76 96 52 18 24 36 49 31  1 19  9 57
Card  79: 77 75 62 44 93 43 58 36 40 65 | 83 16 49 75 86 25 44 81 77 66  6 96 64 54 32 51 11 95 33  5 19  7 30 38 74
Card  80: 27 25 51 76 78 73 32 26 44 13 | 14 28 50 17 59  5 39 74 15 67 33  8 86 32 40 58 72 68 96 66  1 98 31 65 46
Card  81: 23 80 16 89 92 28 94  8 87 15 | 39 41 85 51 12 58 31 81 26 99 17 77 87 91 84 18 21 52 66  3 98 22 54 76 19
Card  82: 11  8 87 49 66 34  7 92 83 28 | 59  5 10 39 26 81 76  9 61 42 18 20 46 17 77 53 78 88 82 15 21  6 75 64 13
Card  83: 55 37 99 54 46 94 32 15 91 24 | 94 70 68 24 52 65 99 91  8 89 32 48 15 76 73 95 55 78  5 96 26 54 46 37 19
Card  84: 23 80 33 41 81 50 57 78 53  6 |  4 78 66 50 72 53 87 99 74 23 81 18 32 57  6 98 80 39 54  5 41 83 14 86 33
Card  85: 76 83 46 92  6 65 73  3 78 28 | 32 59 26 92 83 65 21 46 64 28 61 50  3 11 29 75 36 20 17 76 73  6 78 91 55
Card  86: 56 50 18 82 63 61  9 95 47 59 | 80 79 74  6  5 25 82 97 61 18 63 21 59 11 32 56 49 65  3  9 95 47 54 50 68
Card  87: 15  2 85 45 33  4  9 24 65 58 | 40  2 98 75  9 41 24 85 78  4 65 15 80 45 58 52 33 32 26 35 51 28 14 56  6
Card  88: 93 35 69 57  8 74 47 39 52  4 | 74  8 64 98 80 86 63 91 93 76 52 24 68 15 39 96 57 97 69 78  4 51 47 35 38
Card  89: 91  8 73 99 75 66 31 43 55 92 | 64 43 25 58 48 91 29 66 20 47 72 75 92 45 36 81 73 55  8 33 13 10 31 99  7
Card  90: 64  8 65  3 29 61 74  7 59 53 |  4  8 67 29 20 97 98 39 95 75 45 74 12 87 53  3 65 31  7 61 55 64 26 59 46
Card  91: 39 70 40 95 23 45  2 18 89 30 | 70 12 64 13 14 18 23 56  5 45 76 73 10 54 81  8 94 83 89 40 49 95 79 92 78
Card  92: 53 30 93 85 86 66 34 35 47 37 | 10 44 41 73  6 34 89 92 30 75 99 87 52  4 21 51 45 59 29 78 67 11 17 68 42
Card  93: 95  3 90 96 73 78 58 55 13 61 | 57 37 26 51 68 64 48 54 24 36 56 25 19 15 17 88 73 55 92 11 74 87 14 35  8
Card  94: 35 13 57 75 85 23  8 49 33  5 | 66 76 20 80 21 33 96  5 49 25 23 88 13 54 24 57 32 62 84 78 60 17 91  8 85
Card  95: 43 77  1 95 38 40 32 68 26 89 | 77  7 65 76  1 37 25 26 12 48 29 89 95 28 96 68 38 40 43 58 57 45 32 67  5
Card  96: 90 22 40 75 80 43 86 34 82  7 | 82 89  7 97 86 69 40 75 34 87 16 65 37 55 57 11 19 85 95 83 71 84 35 90 80
Card  97: 67 12 11 51 56 82 43 18 38 94 | 63 72 48 75 95 14 30 15 68 44 19 73 46 67 88 82 85 35  6 84 78 71 40 24 33
Card  98: 89 64 91 94 98 87 74 68 18 49 | 35 54 21 77 75 38 32 45 46 22 44  4 41 78 27  9 93 25 90 48 57 47 68 30 99
Card  99: 36 16 81 35 91 25 86 50 57 17 | 73 75 18 88 87  8 24 11 25 16 36 59 69 81 68 91 72 78 71 66  1 99 26 86 57
Card 100: 52 71 18 60  6 88 27 33 92 29 | 66 61 80 21 25  8 79  7 41 99 95 43 29  4 93 13 55 37 23 30 72 28 57 26 62
Card 101: 40  8  5 79 92 47 17 48 23 77 | 74 57 65 24 79 52 92 43 10  5 50 40 95 90 71 64 34 15 32 41 63 17  7 26 37
Card 102: 64 77 24 30  8 23 98 75 67 66 | 40 17 69 62  3 21 74 30  8 52 81 42 76 68 75 29 72 19 98 50 15 99 92 49 89
Card 103: 34  9  1 49 90 87 55 86 11 82 | 66 39  3 87 52 81 89 41 99 95 38 54 55 50 27 93 30 91 77 20 29 83 65 88  5
Card 104: 34 10 73 24 15 77 88 95 19 65 | 90 62 70 56 14  8 53 17 81 61 72 13 45 86 71 24 74 76 97 87 23 40 94 41  6
Card 105: 73 47 91 81 55 27 43 80 63 25 | 11 31 44 42 17 93 77 12 96 61 35 53 92 51 18 71 38  9 67 75 58  5 88 72 52
Card 106: 45 52 51 29 16 93 66 96 49 43 | 88 25 58 76 34 54  4 20 81  8 47 65  3 90 94 22 18 41 28  9 21 57 26 70 35
Card 107:  1 12 46 25 11 87 80 82 57 65 |  1 12 17 30 11 95 80 19 22 69 46 82 65 29 34 44 62 57 51 87 25 45  3 23 56
Card 108: 78 12 20 25 16 19 30 93 59 75 | 19 59 79 93 12 92  7 16 20 10 64 89  1 87 62 91 58 38 74 37 72 47 60 27 30
Card 109: 73  8 74 89 18 91  7 93 68 94 | 68 25 56 55 48 74 12 91 43 93 18 94 19 65 95 67 54 42  8 52 82 69 89  7 45
Card 110: 40 59 97 13 34  9  1  7 87 28 | 70 97 71  1 60 20 86 40 44 77 87  4  9 16 34 73 38 39 28 59 96 13 21 78  7
Card 111: 29 60 63 68  4  7 45 46 13 90 | 78 32  2 29 86 47 28 14  5 18 31 59 46 68 64 97 45 55 91 63 90 60 92 93  7
Card 112:  9 25 58 91 81 28 52 99 73 13 |  1 95 60 59 10 12 17 78 11 34 41 35  6 49 64 75 82  3 58 67 14 54 57 28 55
Card 113: 73 14 18 93 70 92 90 65  9 91 | 95 69  6 36 80 56 10 33 48 47 34 58 57  7 83 24 37 26 19 86 76 31 15 35 64
Card 114: 37 62 48 26 58 21 65 25 24 78 | 93 40 52 24 25 19 77 83 57 43 38 62 39 21 10 36 76 20 26 60 37 15 16 65 45
Card 115: 48 30 97 47 75 92 54  7 22 50 | 48 21 54 13 78 17 31 75 92 14  7 20 22 97 30 35 11 77 18 47 45 70 50 69  5
Card 116: 82 21 15 60 81 39 29 10 66 22 | 71 66 40 82 65 23 18 29 21 30 68 43 10 60 67 22 11 15 62 39 69 85 31  2 81
Card 117: 54 50 61 78 99 47 26 44 38 87 | 68 89 64 78 39 11 91 24 26 50 45 74 73 27 87 44 82 47 38 33 67 51 13  3 54
Card 118: 37 53 91 15 79 31 74  9 58 80 | 97 70 28 13 11 79  2 50 69 93 94 12  7 54 14 62 65 40 64 22 59 19 90 10 36
Card 119: 72 96 41 97 17 33  4 81 29  7 | 38 29 47 81 20 17 72 25  4 36 24 33 93 30 49  7 34 52 78 28 41 98 96 56 97
Card 120: 64  7 82 45 92 26  6 47 53 70 | 83 53 63  2 90 81 78 69 11 86 68  5 42 98 37 70 59 75 82 44 40 87 55 43 95
Card 121: 93 90 20 87 23 17 67 74 16 50 | 93 40 43 51 65 69 32 39 10 56 22 99 64  7 37  3  4 61  9 63 92 31 70 35 46
Card 122: 90 15 66 36 47 22 34  2 48 74 | 41 76 38  3 37 84 45 57 96 59 67 47 20  4 93 55 80 18  6 58 72 75 21  7 71
Card 123: 36 51 45 54 40 50 99 78 19 69 | 35  1 68 98 51 65 45 83 95 27 78 91 44 22 48 96 33 79 14 77 88 36 26 54 40
Card 124: 52 80  2 38  6 79 69 12 42 84 | 76 82 11 57 42 38 64 65 81 28 93 23 61 69 75 17 22  9 70 41 30 26 24 59 44
Card 125: 28 15 71 21 45 90 69 99 67 19 | 80 25 23 33 88 86 62 21  5 41 66 20 63 47 76 94 99  9  7 18 31 12 68 83 81
Card 126:  6 83 28 97 66 88 20 30 37 98 | 35 15 39  5 68 38 59 90 11 37 24 82 79 54 22 52 87  9 80 49 76  1 29 23 14
Card 127: 62 33 80 58 34 82 79 50 13 35 | 23 89 99 27 56 64 93 66 29  2 41 86 39 36 16 49 88 22 90 17 72 19 44 46 25
Card 128: 31 97 54 98 68 44 66 21 12 64 | 56 17 41 96 13 20 98 49 16 24 58 10 32 19 38 91 69 67  2 57 48 55 47  4 28
Card 129: 11 31 45 56 28 66 97 69 63 95 | 22 52  1 41 90 77 42 39 62  6 12 61 78 10  2 23 59 48 86 96 33 53 50 46  4
Card 130: 18 30 26 93 24 60 31 40 85 83 |  6 83 18 82 24 63 60 41 43 93 22 30 72 85 29 77 12 84 40 16 61 26  9 31 89
Card 131: 32 16 18 79 55 23 85 67 83 62 | 18 67 96 62 98  5 10 94 72 66 50 55 32 63 93 23 90 85 25 79  8 16 30 83 39
Card 132:  9 30 32 89 54  7 68 75 85 44 | 13 30 94 73 50 21 97  9 85 54 16 38  8 84 20 32 41 25 61 66 90 77  7  3 89
Card 133: 33 36 25 13 44 82 70 87 31 42 | 22 36 17 87 74 26 70 80 25 13 27 33 12 52 46 82 86 16 15 44 21 42 31 96 88
Card 134: 26  4 44 47 89 97 62 72 57  2 | 57 39 66 72 68 11 47 91  2  6 71 31 81 62 15 65 63 40 10 89 44 14  3 38 16
Card 135: 74 25 37 34 15 97 79 55 33 36 | 62 30 34 97 74 55 61 86 54 79 32 25 24 33 14 35 26 27 37 89 15 20 36 69 47
Card 136:  5 35  2 29 40 56 30 20 19  4 | 65 26 55 59 94 36 78 12 13  4  6 75 53 45 63 42 67 37 41 89 54 23 86 46 58
Card 137: 56 64 48 82 59 99 72 53  7 71 | 38 16 27 93 80 12 44 40 63 57 73 41 86 42 55 50 37 36 26 51 11 94 83 20  4
Card 138:  9 41  6 31  7 96 54 67 91 60 | 61 78 89 16 92 64 66 30 58 70 85 23 10 97 11 63 83 36 86 25  6 54 45 17 69
Card 139: 34 30 44 64 37 41 46 49 42 94 | 19 12 22 81  8 15 48  2 47 99 93  9 55 98 62 42 37 36 87 77 92 71 34 25 44
Card 140: 88 45 37 47 62 46 79  5 35 18 |  8 94  3 64  5 95 19 15 41 14 43 20 57 63 35 89 69 81 68 18 45 11 62  2 77
Card 141: 20 40 14 84 69 72 77 97 24 98 | 57 75 64 90 71 95 37 21 55 43  4 98 18 41  2 68 30 20 53 13 27 19 38 89 29
Card 142: 31 76 56 50 12 11 83 29 39 27 | 97 80 20 37 49 51 35 71 19 43 84 89 40 13 72 34 59 77 32 98 30 86  9 25 60
Card 143: 46  8 62 31 75 50 56 22 69 93 | 90 69 91 22  7 21 14 40 17 58 71 87 82 95 43 83 93 49 60 39 61 37 26 18 19
Card 144: 56 58 52 82 31 13 94 26 51  8 | 62 36 54 65 59  4 20 63  6  1 44 93 96 48 57 23 18 34 88 17 35 91 28 71 25
Card 145: 66 55 61 68 13 67 94 43 30 40 | 45 42 38 54 56 34  8 76 26 75 58 37 60 83 46 40 12 64 94 13 48 90 77 71 92
Card 146: 48 26 45 13 82 78 42 53 10 43 | 10 71 22 18 29  9 53 16  8 74 59 63 23 24 68 34 51 79 33 70 84 95 15 17 69
Card 147: 72 62 31 87 90 79 85 88 92 66 | 24 99 82 42 28 34 47 55 25  3 73 64 93 19 11 57 53 38 10 48 76 37 27 60 44
Card 148: 93 38 70 11 87 94 65 81 21  6 | 35 68 36 86 40 29 44 12  2 53  5 85 73 31 45 76 80 52 69 56 25 54 14 16 90
Card 149: 31 52 17 65 41  9 66  5 16 93 |  7 86  8 38 87 35 33 73 68 81  1  6  2 77 60 50 62 70 20 18 95  3 97 91 42
Card 150: 11 57 95 18  5 26  4 44 59 38 |  4 13 60 93 28 17 63  1 97 79 51 49 18 23 53 16 86 45  7 21 56 55 39 65 70
Card 151: 39 36 85  7 88 10 72 97 90 27 | 98  6 10 92 12 99 68 82 42 97 75  5 36 46 35 37 38 88 90 29 23 74  9 56 52
Card 152: 62 56 21 95 54  7 59 84 63 67 | 54 68 88 28 93 52 76 62 64 44 70 90  6  7 95 56 96 87 85 21 67 75 27 82 91
Card 153: 62 31 71 79 15 12  9 57 93 91 | 44 16 58  6 49 88 52 14 57 28 23 79 72 40 17 29 18 22 42 81 37 91  4 97  3
Card 154: 53 70 76 62 19 41 52 69  5 24 | 76 52 38 11 19 67 41 23 91 53  5 24 12 16  7 70 65 37 42 22 62  2 20 35 32
Card 155: 79 63 21 73 65 57 18 27 13 87 | 59 70 98 85 22 25 13 21 95 10  4 17  8 79 77 92  3 33 36 64 58 51 84 97 15
Card 156: 38 68 83 76 26 57 90 64  1 15 | 42 71 74  3 13 21 27 75 28 59 91 51 70 57 99 54 39 73  8 30 62 68 85 92 18
Card 157: 60  1 88 97 76 28 81 66 16 39 | 81  2 61 16 45 33 79 71 90  3 26 58 70 54  1 39 86 88 25 48 47 56 24 40 82
Card 158: 88 28 41 16 95 70  5 94  9 51 |  4 83 15 41 63 94 98 45 32 12 39 75 38  1 64 96 18  9 51 71 95 27  6 10 50
Card 159: 30 46 69 86 50 15 56 88 59 70 | 77 65 53 49 12 31 18  7 94 59 70  3 17 79 72 14 74 57 96 37 21 47 58 50 68
Card 160: 86 44 41 13 16 24 67  2 48  7 | 87 26 34 63 10 52 66 97 64 46 33  4 70 53 61 94  8 13  9 39 14 49 30 75 43
Card 161: 15 46 36 78 41 86 87 92 49 80 |  7 61 58 53 56 33 43 75  6 79 52 25 94 66 90 95  1 48  8 68 72 91 42 34 19
Card 162: 27 98 46 22 87 10 97 18  5 58 | 56 21 62 64 72 48 26  4 54 52 14 63 84 59 37 28 73 99 47 44 82 69 71 81 76
Card 163: 65  8 26 79 35 82 18 75 40 76 | 58 67 84  4 33 74 38 80 89  1 99 55 92 94 69 34 48 52 98 42 32 64 54 88 37
Card 164: 99 15 46 52 23 28 13 72 17 78 | 41 59 97 94 79 95 38 18 64 70 96 77 21  9 66 28 78 90 58 29 71 52 11  2 74
Card 165: 73 39 26  4 67 65 79 22 89 78 | 33 79 70 13 65 94 75 17 22 89 26 67 10 86 28  4 71 38 48 19 45 46 15 59 55
Card 166: 62 85 90 76 53 33 99 32 55 71 | 66 28 87 67 26 80 70 57 16 54 97 38 43 74 19 23 60 72 71 92 37 17 61 46 42
Card 167:  2 71 49 13 39 91 35 14 24 23 | 89  2 72 76 55 23 37 24 66 13 75 56  7 14 39 45 91 49 22 17 19 35 47 41 57
Card 168: 71 51  7 15 99 28 95 70 86 57 | 74 42 73 47 96  5 46 39 76 71  1 94 85 41 67  6 12 69 72 98 18 81 36 59 21
Card 169: 96  3 10  7 70 85 44 33 74 28 | 48 91 61  7  3 85 19 26 90 33 74 96 58  4 13 28 40 31 77 70 44 14 41 10 54
Card 170:  6 29 84 58 93 28 12 74 16 81 | 48 30 98 19 52  2 65 78  4 41 56 35 90 92 12 38 50 17 79 45 51 74  5 88 40
Card 171: 80 82 69 36 31 86 39  7 62  9 | 76 65 36 46 83 17 70 42 62 39 38  9 85 94 66  7 31 86 29 19 80 24 79 82 52
Card 172: 40 45 78 95 18 54 11 52 51  8 | 78 23 90 13 55 40 93 64 63 28 62 58 51 74 65 29 25 69 98 96 85 11 45 37 71
Card 173: 52 13 74 71 73  1 40 76 64 23 | 59 26 48 87 63 16 29 90  3 45 57 67 70 22  1 11 51 24 18 93 95 89  7 86 17
Card 174: 16 22 71 10 78 57 89 41 98 29 | 67 52  9 21 19 15 47 55 42 62 25 38 87 97 61 91 44 80  3  4 95 66 23 39 99
Card 175: 56 53  6 45  5 42 22 59 84 87 | 34 97 63 59 62 47 88 50 75 45  5 26 65 52 25 39 87 68  4 42 13 38 33 19 77
Card 176: 90 63 13 55 52  5 58 70 32  3 | 76 25 32 27 26  5 44 80 14  9 98 39 78 43 24 55 99 47 95 36 72 93 74 16 60
Card 177: 43 79 88 49 34 42 69 83 11 94 | 76 34 28 72  8 14 82 74 67 56 17 53 46 81 69 93 73 78 29 10 41  7  2 94 89
Card 178: 39 29 85 95 63 87 52 16 33 90 | 88 76  1 12 81 38 72 77 19 46 11  2 44 85 71 24 57 25 28 69 97 37 98 94 50
Card 179: 82 36 61 27 71 84 93 48 16  8 | 19 81 37  1 69 77 90 91 40 66 26  4 46 61 83 98 25 73 23 10 85 52 58 56 59
Card 180: 10 53 55 47 40 51 28 27  6  8 | 89 18 44 17 32 86 71  1 87 50 33 94 97 98 29 74 66 56 12 52 84 99 75 83 69
Card 181: 79 27 56  9 80 31 37 75 62 15 | 81 20 28 43 83 72 52 90 95 39 25 57 59 13  3 12 70 66 34 78 74 44  6 35 48
Card 182: 48 96 21 97 45  7 73  3 51 46 | 34 10 41 89 46 24 48 38  3 97 31 51 86 77 21 81 22 45 37 43 73 96  7 11 91
Card 183: 62 89 20 66 77 45 14 96 59 93 | 51 14 97 93 78 49 66 71 20 77 79 62 56  3 18 23 45 55 70 39 59 96 32 89 52
Card 184: 79 43 66 27 76 70 21 71 19 20 | 49 79 21 12 66 71 98 45 43 94 65 36 54 92 37 70 82 20 32 61 60 76 19 58 27
Card 185: 91 40 88  1 15 86 47 42  9 25 | 38  5 40 82 15 63 29 25 91  9 10 66 47 42  1 88 81 50 90 86 98 65  7 24 39
Card 186: 93 94 57 29 81 56 67 86 42 12 | 71 79 86 39 72 67 77 12 64 56 93 94 90 34 41 60 81 65 82 29 16 17 42 57 78
Card 187: 97 76 22 51 85 78 13 28 72 48 | 45 13 62 51 88 78 85 93 99 68 84 48 97 38  1 75 76 11 60 72 91 22 70  3 28
Card 188: 88 60 55 48 93 86 11 39 52 40 | 86 96 11 88 55 72 74  1 40  8 52 48 85 61 81 39 17  9 56 69 93 57  7 60 73
Card 189: 55 92 80 81 19  1  5 57 77 91 | 32  2 87 77 64 36 91 65 73 54  3 88 57  4 92  5 55 47  8 96  1 19 81 41 80
Card 190: 97 13 22 50  7 96  9 69 71 87 | 66 85 20 57 83 69  6 41 24 30 33 46 73 62 52 13 59 97  8 16 58 22 76 54 95
Card 191: 30 45 49 52 89 95 81 50 79 54 | 52 22 71 89 63 75 33 80 37 26  7 54 94 83 50 45 32 81 79 62 95 77 19 49 36
Card 192: 19 65 84  6  8 60 11 68 57 98 | 57 11 84 75 67 65 41 45 95 31 15 83 50 20  3 52 98 58  8 51 60 78 77  6 94
Card 193: 23 13  3 52 40 44 18 54 88 63 | 79 71  3 96 76 97 51 39  7 18 65 38 13 99 16 92 37  4 67 42 23 44 24 50 21
Card 194: 14 18 25 52 51 69 40  9 39 10 | 76 98 45 21 53 24 13 62 17 81  6 99 39 60 70 50 30 33 58 49 18 56  2 27 63
Card 195: 89 74 91 81 24 79 99 94 75  5 | 67 36 12 98 11 95 76 63 20 28 38  6 42 87 64 48 10 54 53 58 60 34 35 43 31
Card 196: 29 83  5 90 63 25 84 53 64 72 | 29 95 11 39 81 24 27 48 36 28 87  3 66 65 96 47 77 13 84 21 68 55 51 16 23
Card 197: 84 59 32 44 20 75 28 97 86 81 | 32 23 11  2 55 81 79 84  8 59 40 46 66 94 64 91 97  1 45 58 33 29 20 86 44
Card 198: 23 56 48 77 39  3 49 65 96 58 | 22 60 46 87 84 92 78 79 59 25 58 33 89 23 57 81 64 40 27  9 65  5 61 54  4
Card 199: 68 34 40 51 99 79 71 61  8 91 | 97 46 35 38 20 29 41 84 44  2 72 23 17 65 53 94 66 74  4 13 62 68 21 75  6
Card 200: 64 57 12  2 31 81 51 92 58  5 | 40 39  8 99 23 90  2 41 31 75 32 83  9 82 33 76 35 95  5 84 67  7 48 55 98
Card 201: 94 22 71 33 19 55 39 51 29 44 | 86 59  4 77 67 66 40 37 96 64 34 72 60 30 83 28 57 85 50 31 29 97 38 15 49
Card 202: 60 61 91 66 26 49 86 19 27 97 | 80 21 43 40 64 85 32 42 20 74 84 54 39 62 90 89 11 17 71 59 50 45 51 63 72
Card 203: 41  5 59  9 93 28 82 80 89 24 | 47 88 66 39 26 50 32 24 84 19 42 25 96 86  8 91 20 57 67 14 77 23 16 11 73
Card 204: 85 56 67 47 39 52 96 97 42 72 | 49 58 17 24 62 14 43 30 69 82 34 68 80 50 23 28 84 53 99 22 16 27 83  5 57
Card 205: 54 17 93 26 35  9 61 49 81 42 | 94 14 76 52 15 18 38 41 69 28 16 31 73 32 47 37 71 23 82 90 33 75 24 85 11
'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]

# answer=0
# for line in data:
# 	line=line.split(": ")[1]
# 	a,b=line.split(" | ")
# 	# a=a.replace("  ", " ")
# 	# b=b.replace("  ", " ")
# 	# a = a.split(" ")
# 	# b = b.split(" ")
# 	a = re.findall('-?[\d]+', a)
# 	b = re.findall('-?[\d]+', b)
# 	a = [int(a) for a in a]
# 	b = [int(b) for b in b]
# 	point=-1
# 	for b0 in b:
# 		if b0 in a:
# 			point+=1
# 	answer+=2**point if point!=-1 else 0
# print(answer)

cards=[1 for i in range(len(data))]
for i, line in enumerate(data):
	print(i, cards[i])
	line=line.split(": ")[1]
	a,b=line.split(" | ")
	# a=a.replace("  ", " ")
	# b=b.replace("  ", " ")
	# a = a.split(" ")
	# b = b.split(" ")
	a = re.findall('-?[\d]+', a)
	b = re.findall('-?[\d]+', b)
	a = [int(a) for a in a]
	b = [int(b) for b in b]
	point=0
	for b0 in b:
		if b0 in a:
			point+=1
	for j in range(point):
		print("  ", i, j+1, cards[i])
		cards[i+j+1]+=cards[i]
print(sum(cards))



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

