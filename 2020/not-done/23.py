#!/usr/bin/python3


#data='''
#'''.strip().splitlines()
#data='''
#'''.strip().splitlines()

#from pyskiplist import SkipList
#from collections import deque

data='853192647' #real
#data='389125467' #test
data=[int(cup) for cup in data]
N=9
N=1000000
for i in range(10, N+1):
	data.append(i)


#loc=[None for i in range(N+1)]
#for index, d in enumerate(data):
#	loc[d]=index


print('start')
#current=0
for i in range(1000):
	front=data.pop(0)
	pickUp=(data.pop(0), data.pop(0), data.pop(0))

	lookFor=front-1
	if lookFor<=0: lookFor=N
	while lookFor in pickUp:
		lookFor-=1
		if lookFor<=0: lookFor=N
	index=data.index(lookFor)

	#data.pop(current+1)
	#data.pop(current+1)
	#data.pop(current+1)
	for d in pickUp:
		index+=1
		data.insert(index, d)
	#if index > current:
	#	for a in pickUp:
	#		data.insert(index+1-3, a)
	#else:
	#	for a in pickUp:
	#		data.insert(index+1, a)
	#		index+=1

	#data[index]
	#current=(current+1)%(len(data))
	data.append(front)

	#print(''.join(str(d) for d in data))

#print(''.join(str(d) for d in data))
print(data)

