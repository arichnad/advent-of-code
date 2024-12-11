#!/usr/bin/python3


data1='''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data1

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]
#a=0
#for line in data:
#	input, output = line.split(' | ')
#	for i in input.split(' '):
#		
#	for i in output.split(' '):
#		l=len(i)
#		if l==2 or l==3 or l==4 or l==7:
#			a+=1
#print(a)

a=0
total=0
for line in data:
	input, output = line.split(' | ')
	for i in input.split(' '):
		l=len(i)
		s=set(i)
		if l==2:
			oneValues=s
		elif l==3:
			sevenValues=s
		elif l==4:
			fourValues=s
	fourMinusOne=fourValues - oneValues
	
	answer=0
	for i in output.split(' '):
		answer*=10
		l=len(i)
		s=set(i)
		if l==2:
			answer+=1
		elif l==3:
			answer+=7
		elif l==4:
			answer+=4
		elif l==5:
			if s.issuperset(oneValues):
				answer+=3
			elif s.issuperset(fourMinusOne):
				answer+=5
			else:
				answer+=2
		elif l==6:
			if s.issuperset(fourMinusOne):
				if s.issuperset(sevenValues):
					answer+=9
				else:
					answer+=6
			else:
				answer+=0
		elif l==7:
			answer+=8
	total+=answer
print(total)



