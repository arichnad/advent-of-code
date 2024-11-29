#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading

from astar import AStar

data=[' '*10]*10

data = [[column for column in line] for line in data]

W,H=len(data[0]),len(data)
class AStarSolver(AStar):
	def heuristic_cost_estimate(self, n1, n2):
		(x1, y1) = n1
		(x2, y2) = n2
		return math.hypot(x2 - x1, y2 - y1)

	def distance_between(self, n1, n2): return 1

	def neighbors(self, node):
		x,y = node
		return[(nx, ny) for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)] if 0 <= nx < W and 0 <= ny < H and data[ny][nx] == ' ']

print(list(AStarSolver().astar((0,0), (9,9))))
