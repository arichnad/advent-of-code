#!/usr/bin/python3


data='''
abc

a
b
c

ab
ac

a
a
a
a

b
'''.strip().splitlines()

data='''
'''.strip().splitlines()

data+=['']

group=[]
output=0
for line in data:
	if line=='':
		output+=(len(set(group)))
		group=[]
		continue
	group+=[value for value in line]

print(output)

group=None
output=0
for line in data:
	if line=='':
		output+=(len(group))
		group=None
		continue
	values=set([value for value in line])
	group=values if group is None else group.intersection(values)
	

print(output)

