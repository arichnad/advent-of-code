#!/usr/bin/python3

data='''
16
10
15
5
1
11
7
19
6
12
4
'''.strip().splitlines()
data='''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''.strip().splitlines()


data='''
149
87
67
45
76
29
107
88
4
11
118
160
20
115
130
91
144
152
33
94
53
148
138
47
104
121
112
116
99
105
34
14
44
137
52
2
65
141
140
86
84
81
124
62
15
68
147
27
106
28
69
163
97
111
162
17
159
122
156
127
46
35
128
123
48
38
129
161
3
24
60
58
155
22
55
75
16
8
78
134
30
61
72
54
41
1
59
101
10
85
139
9
98
21
108
117
131
66
23
77
7
100
51
'''.strip().splitlines()

data=sorted(int(line) for line in data)

last,output1,output3=0,0,1
for line in data:
	difference=line-last
	if difference==1:
		output1+=1
	elif difference==3:
		output3+=1
	else: print('fail')
	last=line
print(output1*output3)

visited={}

for line in data:
	outputWays=0
	for check,ways in visited.items():
		if line-check>3:
			continue
		outputWays+=ways
	if line<=3: outputWays+=1
	if outputWays > 0:
		visited[line]=outputWays

print(outputWays)
