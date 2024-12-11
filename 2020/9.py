#!/usr/bin/python3


N=5
data='''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''.strip().splitlines()

N=25
data='''
'''.strip().splitlines()


data=[int(line) for line in data]

for i in range(N+1,len(data)):
	found=False
	for j in range(1,N+1):
		for k in range(j+1,N+1):
			if data[i]==data[i-j]+data[i-k]:
				found=True
				break
	if not found:
		answer=data[i]
		break
print(answer)

values={}
for line in data:
	newValues={}
	for total,(largest, smallest) in values.items():
		if total+line==answer:
			print(largest+smallest)
			break
		newValues[total+line]=(max(largest, line),min(smallest, line))
	newValues[line]=(line, line)
	values=newValues

