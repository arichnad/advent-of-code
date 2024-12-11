#!/usr/bin/python3


data1='''
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

answer=0
g={}

#for line in data:
#	a,b = line.split('-')
#	if a in g:
#		g[a].append(b)
#	else:
#		g[a]=[b]
#	if b in g:
#		g[b].append(a)
#	else:
#		g[b]=[a]
#
#visited={}
#
#def v(n):
#	if n in visited:
#		return
#	if n == 'end':
#		global answer
#		answer+=1
#		return
#	if n.upper()!=n:
#		visited[n]=True
#	
#	for i in g[n]:
#		v(i)
#	
#	if n.upper()!=n:
#		del visited[n]
#
#v('start')

for line in data:
	a,b = line.split('-')
	if a in g:
		g[a].append(b)
	else:
		g[a]=[b]
	if b in g:
		g[b].append(a)
	else:
		g[b]=[a]

visited={}

def v(n, twice):
	if n in visited and visited[n]>1:
		return
	if n == 'end':
		global answer
		answer+=1
		return
	
	if n.upper()!=n:
		if n in visited:
			if twice:
				return
			twice=True
			visited[n]+=1
		else:
			visited[n]=1
	
	for i in g[n]:
		if i == 'start':
			continue
		v(i, twice)
	
	if n.upper()!=n:
		visited[n]-=1
		if visited[n]==0:
			del visited[n]

v('start', False)

print(answer)

