from math import sqrt

def manhattan_distance(current, goal):
  distance = 0
  size = int(sqrt(len(current)))
  res_x = 0
  res_y = 0
  
  for i in current:
    if i is not 0:
      res_x = abs(goal.index(i) % size - current.index(i) % size)
      res_y = abs(goal.index(i) / size - current.index(i) / size)
      distance += res_x + res_y
  return distance

def xy(current, goal):
  distance = 0
  size = int(sqrt(len(current)))

  # Horizontal
  distance += abs(goal.index(0) % size - current.index(0) % size)
  # Vertical
  distance += abs(goal.index(0) / size - current.index(0) / size)

  return distance

def misplaced_tiles(current, goal):
  distance = 0

  for i in current:
    if i is not 0:
      if (goal.index(i) != current.index(i)):
        distance += 1
  return distance

def linear_conflict(current, goal):
  distance = 0
  size = int(sqrt(len(current)))
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

heuristic_functions = {
  "manhattan_distance": manhattan_distance,
  "xy": xy,
  "misplaced_tiles": misplaced_tiles,
  "linear_conflict": linear_conflict
}

def get(heuristic):
  return heuristic_functions[heuristic]
