from math import sqrt

def xy(current, goal):
	distance = 0
	size = int(sqrt(len(current)))

	# Horizontal
	distance += abs(goal.index(0) % size - current.index(0) % size)
	# Vertical
	distance += abs(goal.index(0) / size - current.index(0) / size)

	return distance

if (__name__ == '__main__'):
	current = [
		0, 3, 1,
		7, 2, 8,
		4, 6, 5
	]
	goal = [
		3, 2, 1,
		4, 5, 6,
		7, 8, 0
	]

	print "xy:", xy(current, goal)