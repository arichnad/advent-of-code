#!/usr/bin/python3


data1='''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data=[int(d) for d in data[0].split(',')]

#rand=data.pop(0).split(',')
#
#import re
#board=[]
#while len(data)>=5:
#	data.pop(0)
#	board.append([re.split(' +', line.strip()) for line in data[0:5]])
#	for i in range(5):
#		data.pop(0)
#
#solved=[[[False for i in range(5)] for i in range(5)] for k in range(len(board))]
#print(board)
#for rCount, r in enumerate(rand):
#	for k in range(len(board)):
#		for j in range(5):
#			for i in range(5):
#				if board[k][j][i]==r:
#					solved[k][j][i]=True
#		s=False
#		for j in range(5):
#			for i in range(5):
#				if solved[k][j][i]==False:
#					break
#			else:
#				s=True
#
#		for j in range(5):
#			for i in range(5):
#				if solved[k][i][j]==False:
#					break
#			else:
#				s=True
#		if s:
#			print(int(r)*sum([int(board[k][j][i]) if not solved[k][j][i] else 0 for j in range(5) for i in range(5)]))
#			import sys
#			sys.exit(0)
rand=data.pop(0).split(',')

import re
board=[]
while len(data)>=5:
	data.pop(0)
	board.append([re.split(' +', line.strip()) for line in data[0:5]])
	for i in range(5):
		data.pop(0)

solved=[[[False for i in range(5)] for i in range(5)] for k in range(len(board))]
for rCount, r in enumerate(rand):
	sCount=0
	for k in range(len(board)):
		for j in range(5):
			for i in range(5):
				if board[k][j][i]==r:
					solved[k][j][i]=True
		s=False
		for j in range(5):
			for i in range(5):
				if solved[k][j][i]==False:
					break
			else:
				s=True

		for j in range(5):
			for i in range(5):
				if solved[k][i][j]==False:
					break
			else:
				s=True
		if s:
			sCount+=1
		else:
			lastK=k
		if sCount==len(board):
			print(int(r)* sum([int(board[lastK][j][i]) if not solved[lastK][j][i] else 0 for j in range(5) for i in range(5)]))
			import sys
			sys.exit(0)

