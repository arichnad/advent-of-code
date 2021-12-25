#!/usr/bin/python3


data1='''

'''.strip().splitlines()
data2='''
'''.strip().splitlines()

data=data1

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

#for line in data:

m={}

def rec(p1, p2, p1S, p2S):
	k=(p1, p2, p1S, p2S)
	if k in m:
		return m[k]
	out=[0, 0]
	for a in range(1, 4):
		for b in range(1, 4):
			for c in range(1, 4):
				x=p1+a+b+c
				while x>10: x-=10
				if p1S+x>=21:
					ret=(1, 0)
					out[0]+=ret[0]
					out[1]+=ret[1]
					continue
				for d in range(1, 4):
					for e in range(1, 4):
						for f in range(1, 4):
							y=p2+d+e+f
							while y>10: y-=10
							if p2S+y>=21:
								ret=(0, 1)
								out[0]+=ret[0]
								out[1]+=ret[1]
								continue
							ret=rec(x, y, p1S+x, p2S+y)
							out[0]+=ret[0]
							out[1]+=ret[1]
	m[k]=(out[0], out[1])
	#print(p1, p2, p1S, p2S, m[k])
	return m[k]


#p1,p2=4,8
p1,p2=8,1
print(rec(p1, p2, 0, 0))

#die=1
#d=0
#p1S,p2S=0,0
#while True:
#	for r in range(3):
#		p1+=die
#		die+=1
#		d+=1
#		if die==101: die=1
#	p1=((p1-1)%10)+1
#	p1S+=p1
#	if p1S >= 1000: break
#	for r in range(3):
#		p2+=die
#		die+=1
#		d+=1
#		if die==101: die=1
#	p2=((p2-1)%10)+1
#	p2S+=p2
#	if p2S >= 1000: break
#print(min(p1S, p2S)*d)

