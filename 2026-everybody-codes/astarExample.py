#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading

from astar import AStar # see installation in template.py

from testtemplate import *

class AStarSolver(AStar):
	def heuristic_cost_estimate(self, current, goal):
		(x1, y1) = current
		(x2, y2) = goal
		return math.hypot(x2 - x1, y2 - y1)

	# only gets called on connecting neighbors
	def distance_between(self, n1, n2): return 1

	def neighbors(self, node):
		(x, y) = node
		return[(nx, ny) for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)] if 0 <= nx < W and 0 <= ny < H and data[ny][nx] != '#']

print(list(AStarSolver().astar((startX,startY), (endX,endY))))
# error about NoneType is not iterable, means astar couldn't find a path

