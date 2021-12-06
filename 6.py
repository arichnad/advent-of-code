#!/usr/bin/python3


data1='''
3,4,3,1,2
'''.strip().splitlines()
data2='''
1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,4,1,4,4,1,1,2
'''.strip().splitlines()

data=data2

#data=[int(d) for d in data[0].split(',')]

#for line in data:
states=[int(i) for i in data[0].split(',')]

#for i in range(80):
#	newStates=[]
#	for p, s in enumerate(states):
#		s-=1
#		if s==-1:
#			s=6
#			newStates.append(8)
#		newStates.append(s)
#	states=newStates
#print(len(states))


newStates=[0 for i in range(10)]
for s in states:
	newStates[s]+=1
states=newStates

for i in range(256):
	newStates=[0 for i in range(10)]
	for p, s in enumerate(states):
		p-=1
		if p==-1:
			p=6
			newStates[8]+=s
		newStates[p]+=s
	states=newStates
print(sum(states))


