#!/usr/bin/python3


data1='''
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data1

#data = [line.split(' ') for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#wow, that was a waste of like 6 hours:  data=reversed(data)

N=30000000

print(N)
states={}
newStates={}
states[(0,0,0,0)]=0

def add(w,x,y,z,inputs):
	if z>N or z<-N: return
	key=(w,x,y,z)
	if key not in newStates or inputs<newStates[key]:
		newStates[key]=inputs

for row, line in enumerate(data):
	args=line.split(' ')
	
	if len(args)==2:
		op,a=args
		bInput='0'
	elif len(args)==3:
		op,a,bInput=args
	
	if bInput!='w' and bInput!='x' and bInput!='y' and bInput!='z': bInput=int(bInput)
	
	newStates={}
	print(row, op, a, bInput, len(states))
	ws,xs,ys,zs=set(),set(),set(),set()
	for key,inputs in states.items():
		(w,x,y,z)=key
		ws.add(w)
		xs.add(x)
		ys.add(y)
		zs.add(z)

		b=bInput
		if b=='w': b=w
		elif b=='x': b=x
		elif b=='y': b=y
		elif b=='z': b=z

		if op=='add':
			if a=='w': w+=b
			elif a=='x': x+=b
			elif a=='y': y+=b
			elif a=='z': z+=b
			add(w,x,y,z,inputs)
		elif op=='mul':
			if a=='w': w*=b
			elif a=='x': x*=b
			elif a=='y': y*=b
			elif a=='z': z*=b
			add(w,x,y,z,inputs)
		elif op=='div':
			if a=='w': w//=b
			elif a=='x': x//=b
			elif a=='y': y//=b
			elif a=='z': z//=b
			add(w,x,y,z,inputs)
		elif op=='mod':
			if a=='w': w%=b
			elif a=='x': x%=b
			elif a=='y': y%=b
			elif a=='z': z%=b
			add(w,x,y,z,inputs)
		elif op=='eql':
			if a=='w': w=1 if w==b else 0
			elif a=='x': x=1 if x==b else 0
			elif a=='y': y=1 if y==b else 0
			elif a=='z': z=1 if z==b else 0
			add(w,x,y,z,inputs)
		elif op=='inp':
			if a=='w':
				for w in range(1,10):
					add(w,x,y,z,inputs*10+w)
			elif a=='x':
				for x in range(1,10):
					add(w,x,y,z,inputs*10+x)
			elif a=='y':
				for y in range(1,10):
					add(w,x,y,z,inputs*10+y)
			elif a=='z':
				for z in range(1,10):
					add(w,x,y,z,inputs*10+z)
	states=newStates
	print(len(states), ws, min(xs), '-', max(xs), ys, min(zs), '-', max(zs))
	print()
	
	if len(states)==0: break
	#if row==20: break
print(min(inputs for key,inputs in states.items() if key[3]==0))

#w=input0
#x=w!=z%26+11A
#z//=1B
#z=z*(25*x+1)+(w+1C)*x


