#!/usr/bin/python3

import math, sys

from astar import AStar # see installation in template.py

from testtemplate import *

class AStarSolver(AStar):
	def heuristic_cost_estimate(self, current, goal):
		(y1, x1) = current
		(y2, x2) = goal
		return math.hypot(x2 - x1, y2 - y1)

	# only gets called on connecting neighbors
	def distance_between(self, n1, n2): return 1

	def neighbors(self, node):
		(y, x) = node
		output=[]
		for dy in range(-1, 2):
			for dx in range(-1, 2):
				# if dx==0 and dy==0: continue
				if abs(dx)+abs(dy)!=1: continue
				ny,nx = y+dy,x+dx
				if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
				if data[ny][nx] == '#': continue

				newPoint = (y+dy, x+dx)
				output.append(newPoint)
		return output


result = AStarSolver().astar((startY, startX), (endY, endX))


if result is None:
	print('no solution found')
	sys.exit(0)

result=list(result)


print(len(result)-1) # subtracting one to find the distance
print(result)


