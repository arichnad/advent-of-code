#!/usr/bin/python3


data='''
199
200
208
210
200
207
240
269
260
263
'''.strip().splitlines()
data='''
'''.strip().splitlines()

#data=[int(d) for d in data[0].split(',')]

ans=0
last=None
prev=[]
for line in data:
	line=int(line)
	prev.append(line)
	if len(prev)>3:
		prev.pop(0)
	print(prev, sum(prev))
	if len(prev)==3:
		if last is not None:
			if sum(prev)>last:
				ans+=1
		last=sum(prev)
print(ans)



#ans=0
#last=[]
#for line in data:
#	line=int(line)
#	if last is not None:
#		if line>last:
#			ans+=1
#	last=line
#print(ans)


