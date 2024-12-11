#!/usr/bin/python3


data='''
'''.strip().splitlines()

#data='''
#(6 * (7 * 9 + 3) * 2 + 6) + 3
#'''.strip().splitlines()
#23340
#((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2

#(((4 * (3 * 2 + 2) * (9 * 7 * 5 * 4 * 9) * (7 * (7 + 7) * 4 + 9)) + 6) * 4 + 8 + ((6 * 5) * 4 * (2 * 8 + 4 + 7 * 9 + 3) * 2 + 6) + 3)
#(4 * (3 * 2 + 2) * (9 * 7 * 5 * 4 * 9) * (7 * 7 + 7 * 4 + 9)) + 6 * 4 + 8 + ((6 * 5) * 4 * (2 * 8 + 4 + 7 * 9 + 3) * 2 + 6) + 3
#((4 * (3 * (2 + 2)) * (9 * 7 * 5 * 4 * 9) * (7 * (7 + 7) * (4 + 9))) + 6) * (4 + 8 + ((6 * 5) * 4 * (2 * (8 + 4 + 7) * (9 + 3)) * (2 + 6)) + 3)


#(6 * (7 * 9 + 3) * (2 + 6)) + 3


answer=0
for line in data:
	stack=[]
	previousNumber, previousOperator = None, None
	for thing in line:
		if thing == '(':
			stack.append((previousNumber, previousOperator))
			previousNumber, previousOperator = None, None
		elif thing == ')':
			(a, b) = stack.pop()
			if b == '+':
				a += int(previousNumber)
			elif b == '*':
				a *= int(previousNumber)
			else:
				a = int(previousNumber)
			previousNumber = a

		elif thing == '*' or thing == '+':
			previousOperator = thing
		elif thing == ' ':
			continue
		else:
			if previousOperator == '+':
				previousNumber += int(thing)
			elif previousOperator == '*':
				previousNumber *= int(thing)
			else:
				previousNumber = int(thing)
	answer+=previousNumber
print(answer)




answer=0
for line in data:
	stack=[]
	previousNumber, previousOperator = None, None
	for thing in line:
		if thing == '(':
			stack.append([previousNumber, previousOperator, '('])
			previousNumber, previousOperator = None, None
		elif thing == ')':
			while len(stack) > 0 and stack[-1][2] == '*':
				[a, b, dummy] = stack.pop()
				if b == '+':
					a += previousNumber
				elif b == '*':
					a *= previousNumber
				else:
					a = previousNumber
				previousNumber = a
			[a, b, dummy] = stack.pop()
			if b == '+':
				a += previousNumber
			elif b == '*':
				stack.append([a, '*', '*'])
				a = previousNumber
			else:
				a = previousNumber
			previousNumber = a

		elif thing == '*' or thing == '+':
			previousOperator = thing
		elif thing == ' ':
			continue
		else:
			if previousOperator == '+':
				previousNumber += int(thing)
			elif previousOperator == '*':
				stack.append([previousNumber, previousOperator, previousOperator])
				previousNumber, previousOperator = None, None
				previousNumber = int(thing)
			else:
				previousNumber = int(thing)
	while len(stack) > 0:
		[a, b, dummy] = stack.pop()
		if b == '+':
			a += previousNumber
		elif b == '*':
			a *= previousNumber
		else:
			a = previousNumber
		previousNumber = a
		
	answer+=previousNumber
print(answer)

