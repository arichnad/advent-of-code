#!/usr/bin/python3


data='''
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
'''.strip().splitlines()

data='''
'''.strip().splitlines()

player=-1
cards=[[], []]
import time
import random
hit=0
startTime=time.time()

for line in data:
	if line == '':
		continue
	elif 'Player' in line:
		#id=int(line.replace('Player ', '').replace(':', ''))
		player+=1
	else:
		cards[player].append(int(line))

ans={}

def getString(cards):
	#return (tuple(cards[0]), tuple(cards[1]))
	allCards=list(cards[0])
	allCards.extend(cards[1])
	allCards=sorted(allCards)
	mapping={}
	for offset, card in enumerate(allCards):
		mapping[card]=offset
	
	return (tuple(mapping[card] for card in cards[0]), tuple(mapping[card] for card in cards[1]))
END_DEPTH=2
def recurse(cards, depth):
	#if len(cards[0])<len(cards[1]):
	#	return 1-recurse([cards[1], cards[0]], depth)
	if depth==END_DEPTH:
		return random.randrange(2)
	#startString=getString(cards)
	
	global hit, startTime
	#if startString in ans:
	#	hit+=1
	#	return ans[startString]
		
	
	#strings=[]
	seen=set()
	while len(cards[0])>0 and len(cards[1])>0:
		#if depth==0:
		#	print(len(cards[0])-1, cards[0], len(cards[1])-1, cards[1])
		string=(tuple(cards[0]), tuple(cards[1]))
		#strings.append(string)
		if string in seen:
			result=0
			#for string in strings:
			#	ans[string]=result
			#ans[startString]=result
			print('seen')
			return result

		#if string in ans:
		#	return ans[string]
		
		seen.add(string)

		a=cards[0].pop(0)
		b=cards[1].pop(0)
		if len(cards[0])>=a and len(cards[1])>=b:
			#if depth==0:
			#	print('r')
			#	print('recurse! %d depth, %d cache hits, %d cache size, time %d' %(depth, hit, len(ans), (time.time()-startTime)//60))
			
			winners=[0,0]
			TRIES=1
			for run in range(TRIES):
				winners[recurse([cards[0][:], cards[1][:]], depth+1)]+=1
			if depth != END_DEPTH-1 and abs(winners[0]-winners[1]) != TRIES:
				print(depth, winners)
			winner=0 if winners[0]>=winners[1] else 1
		else:
			winner=0 if a>b else 1
		if winner==0:
			cards[0].append(a)
			cards[0].append(b)
		else:
			cards[1].append(b)
			cards[1].append(a)
		#print(cards)
	
	if len(cards[1])>len(cards[0]):
		print('yaaaaay', cards)
	
	result=0 if len(cards[0])>0 else 1
	#for string in strings:
	#	ans[string]=result
	#ans[startString]=result
	#for k, v in ans.items():
	#	print(k, v)
	#print()
	if result==1:
		print('yay')
	#if depth==0:
	#	print(len(cards[0])-1, cards[0], len(cards[1])-1, cards[1])
	return result


def id(cards):
	output=0
	for a in cards:
		for offset, b in enumerate(reversed(a)):
			output+=(offset+1)*b
	return output

origCards=cards
for run in range(1000):
	cards=[origCards[0][:], origCards[1][:]]
	recurse(cards, 0)
	if id(cards) != 32516:
		print(cards)
		print(id(cards))

#32516 is too low

