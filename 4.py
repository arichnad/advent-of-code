#!/usr/bin/python3


data1='''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.strip().splitlines()
data2='''
38,54,68,93,72,12,33,8,98,88,21,91,53,61,26,36,18,80,73,47,3,5,55,92,67,52,25,40,56,95,9,62,30,31,85,65,14,2,78,75,15,39,87,27,58,42,60,32,41,83,51,77,10,66,70,4,37,6,89,23,16,49,48,63,94,97,86,64,74,82,7,0,11,71,44,43,50,69,45,81,20,28,46,79,90,34,35,96,99,59,1,76,22,24,17,57,13,19,84,29

57  7  8 38 31
17 96  5 12 18
58 45 81 89  4
73 51 93 32 10
74 50 26  0 24

79 67 21 84 71
25 22 19 80 13
10 63 90 78 33
93 50 89 58 87
91  7 45  6 41

66 85  4 91 41
59 69 16  0 90
35 13 64 61 93
11 20 29 67 77
92 75 58  3 34

19  1 34 50 76
26 75  8 28 20
96 64 49 77  2
18 58 62 53 60
82 99 38 10 83

89 69 97 16 48
32  3 83 17 33
82 53 15 50 94
52  0 86 25 81
42 38 84 73 76

68 18 44 61 66
24 21 22  6 41
48 29  4 64 78
93 25 88 95 96
72 49 51  2  5

35 41 59 23 21
 0 66 34 12 85
61 26 29 68  5
28 69 90  2 96
 1 16 32 24 44

98 73 33 82 18
51 62 88 67  6
99 44 53 39 36
34 90 50 72 43
64 40 11 26  5

88  8 81 57 99
61 16 22 50  5
26 84 85  7 15
97 27 47 18 21
 3 78 66 94 58

56 40 68 20 24
26 98  6 76 89
61 63 22 99 83
31  5 32 54 82
18 23 17 46 13

35 95 67 73 13
86 33  7  9 43
44 28 55 32 52
54 91 84 97 98
17 49 93 23 56

22 90 61 12 13
87  4 46 25 88
70 38 53 80 11
75 56 96 49 32
 3 55 43 19 67

40 17 70 76 61
82 86 37  8 28
60 48 24 83 53
57 87 44 92 63
10 49 88 15 55

36 80 47 46 84
25 70  2 79 75
55  5 13 99 45
54 73 83 59 67
57  0 69 33 68

51 52 21 44 36
17 30 15 42 18
 6  3 47 94  2
57 77 45 70 90
29 60 19  9 84

16 12 37  6 27
86 87 21 70 71
84  0 11 67 83
 5 68 33 23 26
51 43 28 79 49

22  5 53 12 42
29 81 46 13 88
80 65  8 62 33
72 67 34 21 35
38 77 90 52 44

63 57 52 82 96
46 11 32 20 58
35 15 83  1 55
18 16 73 19 17
22 88 45 95 47

43 15  7 97 88
96 52 84 86 49
80 13 21 28 29
16 36 98 82 41
32 10 62 68 24

46 69  8 55 50
28 21 92 79 73
19 71 74 53 44
24 27 10 14 85
 2 39 58 81 72

68 74 43 62 61
82 73 37 40 93
16  7 41 54 96
10  3 85 70 65
69 71 94  5 81

17 53 87 80 98
76 41 30 25 58
29 14 73 74 43
20 91 24 70 39
46 48 51  9 18

20 41 36 81 93
46 75 33 73 78
26 16 80 54 90
87 17 12 67  1
51 10 39 91 45

76 21 31  3 69
27 42 97 32 87
26 22  4 63 38
46 77 67 80 43
37 50 59 88 96

17 16 10 68 76
 2 45 94 29 40
 1 54 60 66 93
 0 13 42 39 70
 6 82 46 74 43

87 95 31 22 94
86 30 39 56 18
89 74 23 11 64
63 48 85 20 49
27 15 40 83 50

81 48 47 73 95
40 65 89 69  5
38 76 85 30 11
31 61  8 67 62
41 68 42 78 20

46 85 96 83 20
94 52  7 97 31
29 95 99 34 62
 8 69  6 51 54
38 59  5 56 55

18 15 10 35 96
44 66 58 91  9
12  2 45 98 80
22 69 37 67 79
46 36 23 51 75

11 58 64 85 26
21 43 32 36 65
94 61 40 68 67
14 23  6 53  2
93  9 74  3 90

73 82 46 37 20
47 75 38 45 54
76 34 65 44 58
93 89 27 13 33
85 67 40 42 17

13 66  2 65 10
98  4 83 79 92
22 48 93  6 23
24 39 17 60  9
77 49 16 19 35

96 37 88  4 32
80 89 59 39 63
67 19 35 10 40
91 66 47  9 79
45 21 86 92 30

76 85 37 32 29
59 41 44 23 93
86 24 83 81 57
22 21 82 53 16
38 99 79 49 30

54 29 64 65 62
44 59 83 75 56
11 13 34 12 24
96 39 31 95 16
41 38 21 25 60

49  8  3 67  2
30 81 39 26 33
83 73 47 32 65
48 20 75 24 40
74 28 11 19 96

87 25 49 81  7
99 34 35 50 86
18 24 68  4 78
59  8 71  0 41
92 54 64 75 46

 2 19 73 29 10
55  6 43 48 22
64 14 62 39 97
99 26 68 25 12
98 72 45 38 40

59 76 40 37  9
42 23  1 12 54
49 51 17 11 34
74 95 26 78 67
65 32 98 80 45

50 86 95 29 38
 6 11 24 10 73
63 28 30 46 68
34  9 20 58 77
88 52 79 89 98

32 20 93 39 80
67 98 99  4 26
22 89 97 13 73
88 11 72 31 78
76 95 64 43 75

75 23 81 89 90
98 86 88 38 99
51  7 65  2  3
16 59 49 41 87
57 20 58 72 83

21 81 24 43 12
55 74  2 90  5
13 89 59 42  3
47 66 38 20 62
61 56 72 84 41

83 68 73 77 66
96 48 24  7 98
57  4 86 10 34
22 46 80 75 49
89 35 60 79 37

27 50 90 37 28
81 74 58 39 61
 8 72 31 85 57
52 43  9  5 91
68 86  0  4 89

14 41 70 67 59
13 94 31 69 65
76 19  9 79  1
33 20 53 91 36
80 50 21 37 85

16 47 62 33 12
11 74 44 63 60
 2 23 84 80 42
14 58 67 81 24
 8 29 31 91 43

62 86 26 57 74
 9 46 47 81 39
 4 99 59 89  3
20 76 51 70 84
95 72 43 67 61

75 93 56 15 30
11 49 97 16 45
52 91 21 92 62
 0 74 85 48 63
28 76 59 79 60

36 18  0 69 10
34 33 21  5 23
73 42 50 14 11
75 26 95 79 51
76 93  1 43 22

86 64 25  9 54
67 79 49  1  8
63 47 60  4 46
94 97 57 38 30
91 87  0 68 15

94 46  6 69  9
18 49 43 30 31
79 35 76 45 92
67 89 82  2 57
65 21 24 81 52

 5 58 43 37 61
65 67 54 15 50
69 75 14 17 96
23 95 71 33  9
68 82 10  3 29

56 43 88 35 82
44 14 64 60 23
33  5 96 86 47
70 74 27  4  1
51 71 95 59 11

46 14 44  6 19
54 81 59 31 28
 7 67 73 23 86
25 91 57 43 92
65 76 80 47 77

 3 39 70 90 23
64 77 33 83 22
 6 36 81 80 68
85 45 72 53 42
 7 19 88 13  9

88  3 72  6 29
33 13  1 85 68
28 32 78  8 63
15 99 35 80 41
61 50 43 53 39

22 88 19 86 54
78  3 70 65 85
18 12 21 14 17
 5 48 64 81 71
89 91 55 30 87

35 82 37 42 25
44 53 12  2 73
18 24  0 75 51
34 26 54 52 86
56 64 31 57 80

45 97 83 15  5
40 77  1 53 84
67 44 52 37 20
36 64 33 82 90
49 22  6 65 99

18 69 23 78 55
45  4 31 54 44
16 97 13 81 86
77 87 91 53 33
 1 84 83 75 40

95 46 89  7 38
83 32 99 44 20
 6 57 37 34 48
69  5 84 29 54
62 27 13 80 53

45 92 59 71 83
52 75 42 46 86
76 33 50 80 69
36 89 90  3 31
 7  5 48 38 53

86 80 77 18 87
79 93 52 17 20
30 68 48 12 91
25 98 13  9 47
45 73 97 15 59

93 60 34 18 25
38 80 81 91 40
43 87 20 79  7
70 68  6 24 23
46 97 32 78 67

 9  6 28 17 42
 2 86 84 90 13
91 58 16 37 76
15  3 45 51  4
64 99 41 59 39

44  3 85 80 93
 0 43 90 40 89
82 91 55 79 75
30  5 68 50  1
37 24 59 62 66

38 55 21 45  1
23 14 95 25 22
84 10 39  9  0
17 15 58 70 49
62 44 77 65 88

 8 62 25 75 39
20 95 65 11 32
 5 92 15 86 66
64 34 60  7 85
10 76  6 53 61

71 61 62 25 35
23 30 37 14  9
99 98 52 51 19
77 57 17 72 85
33 91 31 43 67

76 66 39 36 44
49 97 93 33 52
13 70 21 17 32
71 98 80 19 60
73 15 99 74  9

41  8 33 29 87
42 86 66 31 50
45 60 83 81 21
36  4 98 43  0
49 76 18 90 16

83 53 34 39 58
91 68 17 62  4
 2 76 44 31 35
14 61 49 84 92
73  6 86 27 65

56 70 47 60 97
35 89 26 99 59
67 23 27 74 65
61 62 15 18 45
54 93  0  9 71

11 24 97 15 30
46 74 17 48 43
16 64 72 60 37
63 90 41 91 66
25 95  1 54 49

87 67 27 26 38
63 44 65 25 81
 1 66 96 62 17
82  2 58  4 86
61 64 54 24 90

72 94 69 85 43
38 11 93 39 13
86 92 12 42 75
 6 89 58 88 52
79 19 20 55 14

77 93 58  6 52
27 48 29 60 71
87 24 25 54 49
53 38 90 51 80
57 50 18  1 13

85 84 54  2 51
33 41  0 38 80
 5 62  1 28 96
17 88 64 26 90
78 91 56 34 74

83 14 82  6 55
30 13 99 57 39
93 73 37 19  8
29 49 76 22 92
69 66  9 60 53

51 78 52 72 79
42 55 74 88 44
90 75 65 87 69
22 35 64 36 86
63 41 19 59 49

49 86 81 23 12
93 16  9  8 95
68 33  4 82 61
45 28 85 87 38
35 70 63 18 52

63 93 38 34 61
75 21 86 42 25
52 85 99 24 36
41 11 79 54 47
44 84 65 28 89

91 37 30 39 59
 7 94 90 38 40
72 21 75 31 61
68 42 34 20  8
 3 16 76 44 57

32 55 36 81 42
21 75 68 28 65
46 70 29 54 64
66 89 96 25 43
79 76 41 77 71

41 29 60 74 34
84 49 83 72 92
22  6 21 17 94
15 44 62 28  2
25 93 64  1 42

68 76 23 62 10
36 87 15 12 57
79 46 18 83 11
48 81 58 52 28
72 40 64 55 21

25 51 42 63 41
 0 72 92 23 13
65  1 69 33  2
78 27 95 61 55
30 54 48  3 57

50 40 58 66 59
84 79 64 75 44
88 93 41 25 97
19 86 37 91 81
10 26 94 77 34

76 44 11 16 60
19 92 91 58 50
97  5 46  4 52
87 42 65 75 15
12  2 54 27 86

77 38 51 29 89
 7 76 54 48 44
88 50  2  5 53
12 70 26 57 74
31 19 18 34 47

35 99 86 96 62
61 97 71 70 66
49 55 36 76  3
94 23 31 91 26
80  8 20 95 15

 4 96 40 36 12
87 75 38 30 11
69 29 23 85 91
49  5 14 57 24
88 20 99 78 65

34 65 71 79 67
28  1 33 47 11
15 86 84 83 55
35 10 19 63 23
58 66 45 77 26

74 13 25 39  8
46 47 77 37  0
60  1 81 42 18
 5 51 78 30  4
36 12 10 32 82

51 83 58 10 56
28 18 43 99 14
 3 57 30 49 88
20 68 76 73 82
 1 85 77 22 47

50 12 11 97 83
40 10 49 81 63
43 15 91  3  2
52 20 53 89 33
42 94 59 78 46

19 63 86 82  9
69 13 27 88 37
45 51 79 11  8
 2 29 41 84 73
76 24 78 96 38

15 19 88 95 54
28 94 96 27 26
 8 82 68  6 71
33  9 99 62 63
38 83 41 14 79

67 57  2 21 19
11 79 74 45 95
42 90 68 47 62
80 61  1  0 39
43 76 40 27 66
'''.strip().splitlines()

data=data2

#data=[int(d) for d in data[0].split(',')]

#rand=data.pop(0).split(',')
#
#import re
#board=[]
#while len(data)>=5:
#	data.pop(0)
#	board.append([re.split(' +', line.strip()) for line in data[0:5]])
#	for i in range(5):
#		data.pop(0)
#
#solved=[[[False for i in range(5)] for i in range(5)] for k in range(len(board))]
#print(board)
#for rCount, r in enumerate(rand):
#	for k in range(len(board)):
#		for j in range(5):
#			for i in range(5):
#				if board[k][j][i]==r:
#					solved[k][j][i]=True
#		s=False
#		for j in range(5):
#			for i in range(5):
#				if solved[k][j][i]==False:
#					break
#			else:
#				s=True
#
#		for j in range(5):
#			for i in range(5):
#				if solved[k][i][j]==False:
#					break
#			else:
#				s=True
#		if s:
#			print(int(r)*sum([int(board[k][j][i]) if not solved[k][j][i] else 0 for j in range(5) for i in range(5)]))
#			import sys
#			sys.exit(0)
rand=data.pop(0).split(',')

import re
board=[]
while len(data)>=5:
	data.pop(0)
	board.append([re.split(' +', line.strip()) for line in data[0:5]])
	for i in range(5):
		data.pop(0)

solved=[[[False for i in range(5)] for i in range(5)] for k in range(len(board))]
for rCount, r in enumerate(rand):
	sCount=0
	for k in range(len(board)):
		for j in range(5):
			for i in range(5):
				if board[k][j][i]==r:
					solved[k][j][i]=True
		s=False
		for j in range(5):
			for i in range(5):
				if solved[k][j][i]==False:
					break
			else:
				s=True

		for j in range(5):
			for i in range(5):
				if solved[k][i][j]==False:
					break
			else:
				s=True
		if s:
			sCount+=1
		else:
			lastK=k
		if sCount==len(board):
			print(int(r)* sum([int(board[lastK][j][i]) if not solved[lastK][j][i] else 0 for j in range(5) for i in range(5)]))
			import sys
			sys.exit(0)
	lastR=r
	import copy
	lastSolved=copy.deepcopy(solved)

	


