def misplaced_tiles(current, goal):
	distance = 0

	for i in current:
		if i is not 0:
			if (goal.index(i) != current.index(i)):
				distance += 1
	return distance

if (__name__ == '__main__'):
	current = [
		3, 0, 1,
		7, 2, 8,
		4, 6, 5
	]
	goal = [
		3, 2, 1,
		4, 5, 6,
		7, 8, 0
	]

	print "Misplaced tiles:", misplaced_tiles(current, goal)