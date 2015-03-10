import math

'''
current and goal are under the following form :
	current = [7, 3, 0, 5, 2, 8, 6, 1, 4]
	goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
'''
def manhattan(current, goal):
	distance = 0
	size = math.sqrt(len(current))
	res_x = 0
	res_y = 0
	for i in current:
		pos_difference = abs(goal.index(i) - current.index(i))
		if i is not 0:
			res_x = pos_difference % 3
			res_y = pos_difference / 3
			distance += res_x + res_y
			if (abs(goal.index(i) % 3 - current.index(i) % 3) == 2 and pos_difference % 3 == 1):
				distance += 2
	return distance