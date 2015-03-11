import math

'''
current and goal are under the following form :
	current = [7, 3, 0, 5, 2, 8, 6, 1, 4]
	goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
'''
def manhattan(current, goal):
	distance = 0
	size = int(math.sqrt(len(current)))
	res_x = 0
	res_y = 0
	for i in current:
		if i is not 0:
			res_x = abs(goal.index(i) % size - current.index(i) % size)
			res_y = abs(goal.index(i) / size - current.index(i) / size)
			distance += res_x + res_y
	return distance

def linear_conflict(current, goal):
	distance = 0
	size = int(math.sqrt(len(current)))
	res_x = 0
	res_y = 0
	for i in current:
		if i is not 0:
			res_x = abs(goal.index(i) % size - current.index(i) % size)
			res_y = abs(goal.index(i) / size - current.index(i) / size)
			distance += res_x + res_y
			# Conflicts
			if (current[goal.index(i)] == goal[current.index(i)]):
				# Horizontal conflict
				if (goal.index(i) % size - current.index(i) % size >= 1 and goal.index(i) % size - current.index(i) % size < size and goal.index(i) / size - current.index(i) / size == 0):
					distance += 2
				# Vertical conflict
				if (goal.index(i) / size - current.index(i) / size >= 1 and goal.index(i) / size - current.index(i) / size < size and goal.index(i) % size - current.index(i) % size == 0):
					distance += 2
	return distance

if (__name__ == '__main__'):
	current = [
		3, 0, 1,
		7, 2, 8,
		4, 6, 5
	]
	goal = [
		1, 2, 3,
		4, 5, 6,
		7, 8, 0
	]

	print "Manhattan distance:", manhattan(current, goal)
	print "Linear conflict:", linear_conflict(current, goal)