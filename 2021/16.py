#!/usr/bin/python3


data1='''
D8005AC2A8F0
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

#a=format(int(data[0], 16), 'b')


num_of_bits = len(data[0])*4

a=bin(int(data[0], 16))[2:].zfill(len(data[0])*4)
print(a)
print('TYPE', a[3:6])
answer=0

def p():
	global a, answer
	v,t,i=int(a[0:3], 2), int(a[3:6], 2), int(a[6:7], 2)
	answer+=v
	print(v,t,i)
	if t==4:
		a=a[6:]
		output=0
		while a[0]=='1':
			print('literal', a[1:5])
			output*=16
			output+=int(a[1:5], 2)
			a=a[5:]
		print('literal', a[1:5])
		output*=16
		output+=int(a[1:5], 2)
		a=a[5:]
		print('literal answer', output)
	else:
		if i==0:
			print('bits')
			l=int(a[7:22], 2)
			a=a[22:]
			oldLength=len(a)
			data=[]
			while oldLength-len(a)<l:
				print('recurse', a)
				data.append(p())

		else:
			print('packets')
			packets=int(a[7:18], 2)
			a=a[18:]
			data=[]
			for i in range(packets):
				data.append(p())
		if t==0:
			print('sum')
			output=sum(data)
		elif t==1:
			print('product')
			output=1
			for i in data:
				output*=i
		elif t==2:
			print('min')
			output=min(data)
		elif t==3:
			print('max')
			output=max(data)
		elif t==5:
			print('>')
			output=1 if data[0] > data[1] else 0
		elif t==6:
			print('<')
			output=1 if data[0] < data[1] else 0
		elif t==7:
			print('=')
			output=1 if data[0] == data[1] else 0
	return output


print(p())
print(answer)

