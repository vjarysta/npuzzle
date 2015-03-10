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
		pos_difference = abs(goal.index(i) - current.index(i))
		if i is not 0:
			res_x = pos_difference % size
			res_y = pos_difference / size
			distance += res_x + res_y
			if (abs(goal.index(i) % size - current.index(i) % size) == size - 1 and pos_difference % size == 1):
				distance += 2
	return distance

if (__name__ == '__main__'):
	current = [
		7, 3, 0,
		5, 2, 8,
		6, 1, 4
	]
	goal = [
		1, 2, 3,
		4, 5, 6,
		7, 8, 0
	]

	print manhattan(current, goal)