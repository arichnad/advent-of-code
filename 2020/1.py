#!/usr/bin/python3

data='''
'''.strip().splitlines()

data = [int(line) for line in data]

import sys

def first():
	for i in data:
		for j in data:
			if i+j==2020:
				print(i*j)
				return
first()


def second():
	for i in data:
		for j in data:
			for k in data:
				if i+j+k==2020:
					print(i*j*k)
					return

second()
