#!/usr/bin/python3

def find(pub):
	subNum=7
	val=1
	l=0
	while val != pub:
		val*=subNum
		val%=20201227
		l+=1
	return l

subNum=3667832
val=1
for l in range(find(17115212)):
	val*=subNum
	val%=20201227
print(val)


