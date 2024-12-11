#!/usr/bin/python3


data1='''
16,1,2,0,4,2,7,1,2,14
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

#m=-1
#for guess in range(min(data), max(data)):
#	value=sum([abs(a-guess) for a in data])
#	if m==-1 or value<m:
#		m=value
#print(m)

m=-1
for guess in range(min(data), max(data)):
	value=sum([abs(a-guess)*(abs(a-guess)+1)//2 for a in data])
	if m==-1 or value<m:
		m=value
print(m)

