#!/usr/bin/python3


data1='''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

s=[]
answer=0
for line in data:
	for ch in line:
		if ch == '[':
			s.append(']')
		elif ch == '(':
			s.append(')')
		elif ch == '{':
			s.append('}')
		elif ch == '<':
			s.append('>')
		else:
			if s.pop()!=ch:
				if ch==')':
					answer+=3
				elif ch == ']':
					answer+=57
				elif ch == '}':
					answer+=1197
				elif ch == '>':
					answer+=25137
print(answer)

t=[]
for line in data:
	s=[]
	for ch in line:
		if ch == '[':
			s.append(']')
		elif ch == '(':
			s.append(')')
		elif ch == '{':
			s.append('}')
		elif ch == '<':
			s.append('>')
		else:
			if s.pop()!=ch:
				break
	else:
		answer=0
		while len(s)>0:
			answer*=5
			ch=s.pop()
			if ch==')':
				answer+=1
			elif ch == ']':
				answer+=2
			elif ch == '}':
				answer+=3
			elif ch == '>':
				answer+=4
		t+=[answer]
print(sorted(t)[len(t)//2])




