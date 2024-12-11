#!/usr/bin/python3


data1='''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data=[int(d) for d in data[0].split(',')]

data=[[char for char in line] for line in data]
gamma,epsilon=0,0
for pos in range(len(data[0])):
	count0=0
	count1=0
	for line in data:
		if line[pos]=='0':
			count0+=1
		else:
			count1+=1
	if count1>count0:
		gamma+=1
		print('gamma 1')
	else:
		epsilon+=1
		print('epsilon 1')
	gamma*=2
	epsilon*=2
print(gamma//2 * epsilon//2)




#data=[int(d) for d in data[0].split(',')]

data=[[char for char in line] for line in data]
gamma,epsilon=[True for i in range(len(data))],[True for i in range(len(data))]
for pos in range(len(data[0])):
	count0,count1=0,0
	for row in range(len(data)):
		if gamma[row]:
			if data[row][pos]=='0':
				count0+=1
			else:
				count1+=1
	for row in range(len(data)):
		if gamma[row]:
			if count1>=count0 and data[row][pos]=='0':
				gamma[row]=False
			elif count1<count0 and data[row][pos]=='1':
				gamma[row]=False
	if sum(gamma)==1:
		for row in range(len(data)):
			if gamma[row]:
				gammaAnswer=data[row]
		break
for pos in range(len(data[0])):
	count0,count1=0,0
	for row in range(len(data)):
		if epsilon[row]:
			if data[row][pos]=='0':
				count0+=1
			else:
				count1+=1
	for row in range(len(data)):
		if epsilon[row]:
			if count1<count0 and data[row][pos]=='0':
				epsilon[row]=False
			elif count1>=count0 and data[row][pos]=='1':
				epsilon[row]=False
	if sum(epsilon)==1:
		for row in range(len(data)):
			if epsilon[row]:
				epsilonAnswer=data[row]
		break

gammaOut,epsilonOut=0,0
for pos in range(len(data[0])):
	gammaOut*=2
	if gammaAnswer[pos]=='1':
		gammaOut+=1
	epsilonOut*=2
	if epsilonAnswer[pos]=='1':
		epsilonOut+=1
print(gammaOut*epsilonOut)


