#!/usr/bin/python3

data='''
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''.strip().splitlines()


data='''
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''.strip().splitlines()

data='''
mask = 100X000X100X00XX1010X0001X11XX100110
mem[33470] = 43619
mem[17642] = 12960
mem[54949] = 1594
mem[25705] = 17992
mem[28651] = 47662
'''.strip().splitlines()

data='''
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''.strip().splitlines()

data='''
'''.strip().splitlines()


mem=[0 for i in range(65536)]
ones=(1<<36)-1


for line in data:
	var, value = line.split(' = ')
	if var == 'mask':
		mask = value
		orMask = int(mask.replace('0', 'X').replace('X', '0'), 2)
		andMask = int(mask.replace('1', 'X').replace('0', '1').replace('X', '0'), 2)
		andMask = ones - andMask
	else:
		index = int(var.replace('mem[', '').replace(']', ''))
		mem[index] = (int(value) & andMask) | orMask
print(sum(mem))



mem={}
ones=(1<<36)-1

def getFloatMask(id, floatMask):
	position = 0
	outputFloatMask = 0
	while id > 0:
		if id&1:
			floatMaskPosition=0
			currentFloatMask = floatMask
			currentPosition = 0
			while currentFloatMask>0:
				if currentFloatMask&1:
					if currentPosition == position:
						outputFloatMask += 1<<floatMaskPosition
					currentPosition+=1
				currentFloatMask>>=1
				floatMaskPosition += 1
		id>>=1
		position+=1
	return outputFloatMask


for line in data:
	var, value = line.split(' = ')
	if var == 'mask':
		mask = value
		floatMask = int(mask.replace('1', '0').replace('X', '1'), 2)
		orMask = int(mask.replace('X', '0'), 2)

	else:
		index = int(var.replace('mem[', '').replace(']', ''))
		current = floatMask
		floatMaskOnes=0
		while current > 0:
			if current & 1:
				floatMaskOnes+=1
			current>>=1
		for id in range(0, 1<<floatMaskOnes):
			outputIndex = ((index | orMask) & (ones-floatMask)) | getFloatMask(id, floatMask)
			#print(index, orMask, getFloatMask(id, floatMask), outputIndex)
			mem[outputIndex] = int(value)


print(sum(mem.values()))


