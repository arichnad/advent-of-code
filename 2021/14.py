#!/usr/bin/python3


data1='''
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

a=data.pop(0)
data.pop(0)

m=[]

for depth in range(40):
	m.append({})
	for rule in data:
		c,b=rule.split(' -> ')
		[a0,a1]=c
		if depth==0:
			output={b: 1}
			if a1 in output:
				output[a1]+=1
			else:
				output[a1]=1
			m[depth][(a0,a1)]=output
		else:
			output={}
			for k,v in m[depth-1][(a0,b)].items():
				if k in output:
					output[k]+=v
				else:
					output[k]=v
			for k,v in m[depth-1][(b, a1)].items():
				if k in output:
					output[k]+=v
				else:
					output[k]=v
			m[depth][(a0,a1)]=output


depth=40-1
output={a[0]: 1}
for i in range(len(a)-1):
	for k,v in m[depth][(a[i], a[i+1])].items():
		if k in output:
			output[k]+=v
		else:
			output[k]=v
maxCount=-1
minCount=-1
for k,v in output.items():
	if v > maxCount:
		maxCount=v
	if minCount==-1 or v < minCount:
		minCount=v
print(maxCount-minCount)
	

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

#for line in data:





