#!/usr/bin/python3


data1='''
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data4 #1.6 10 23

#data = [int(line) for line in data]
data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#for line in data:

num=[3,5,7,9]
uValue=[1,10,100,1000]
def getNum(a):
	return num[ord(d)-ord('A')]
def getU(a):
	return uValue[ord(d)-ord('A')]

def check(data):
	a,b,c,d=0,0,0,0
	for j in data:
		for i in j:
			if i=='A':
				a+=1
				if a==5: raise Exception()
			elif i=='B':
				b+=1
				if b==5: raise Exception()
			elif i=='C':
				c+=1
				if c==5: raise Exception()
			elif i=='D':
				d+=1
				if d==5: raise Exception()

def ins(t, data, previousData=[]):
	check(data)
	d=tuple(tuple(line) for line in data)
	#v=(t,d,[(data, t)] + previousData)
	v=(t,d,None)

	s[t].append(v)

N=100000
s=[[] for i in range(N)]
visited=set()

cur=0

ins(0, data)

while True:
	while len(s[cur])==0:
		cur+=1
		#print(cur, len(s[cur]))
	(t,data,previousData)=s[cur].pop()
	if data in visited:
		continue
	visited.add(data)
	data=list(list(line) for line in data)
	

	for y in range(2,len(data)-1):
		if not ( data[y][3]=='A' and data[y][5]=='B' and data[y][7]=='C' and data[y][9]=='D' ): break
	else:
		if previousData is not None:
			for i, t in reversed(previousData):
				print('\n'.join([''.join(d) for d in i]))
				print(t)
		print('\n'.join([''.join(d) for d in data]),t,len(s[cur]))
		break
	
	
	for j in range(len(data)):
		for i in range(len(data[j])):
			d=data[j][i]
			if d=='.' or d=='#' or d==' ':
				continue
			curNum=getNum(d)
			u=getU(d)
			if j==1:
				#go all the way across
				o=curNum
				for x in range(min(i,o),max(i,o)+1):
					if i!=x and data[j][x]!='.':
						break
				else:
					bad=False
					maxY=1
					for y in range(2,len(data)):
						if data[y][o]=='.':
							maxY=y
						elif data[y][o]=='#':
							break
						elif data[y][o]!=d:
							bad=True
							break
					if bad or maxY==1: continue
					data[j][i]='.'
					data[maxY][o]=d
					if maxY==len(data)-1: print('\n'.join([''.join(d) for d in data]),t,len(s[cur]))
					ins(t+u*(abs(o-i)+(maxY-1)), data, previousData)
					data[maxY][o]='.'
					data[j][i]=d
			else:
				bad=False
				for y in range(j+1,len(data)):
					if data[y][i]!='#' and data[y][i]!=d and data[y][i]!='.':
						bad=True
						break
				if i!=curNum or bad:
					for y in range(1,j):
						if data[y][i]!='.':
							break
					else:
						for direction in range(-1,2):
							if direction==0: continue
							for dx2 in range(1,10):
								o=i+dx2*direction
								if o<0 or o>=len(data[1]): break
								f=data[1][o]
								if f!='.':
									break
								if o==3 and d!='A' or o==5 and d!='B' or o==7 and d!='C' or o==9 and d!='D': continue
								data[1][o]=d
								data[j][i]='.'
								ins(t+u*(abs(o-i)+(j-1)), data, previousData)
								data[1][o]='.'
								data[j][i]=d
				

