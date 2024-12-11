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
