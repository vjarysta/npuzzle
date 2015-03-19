from math import sqrt

def manhattan_distance(current, goal, s):
  distance = 0
  
  for i in current:
    if i is not 0:
      g_i = goal.index(i)
      c_i = current.index(i)
      res_x = abs(g_i % s.size - c_i % s.size)
      res_y = abs(g_i / s.size - c_i / s.size)
      distance += res_x + res_y

  return distance

def xy(current, goal, s):
  distance = 0
  g_i = goal.index(0)
  c_i = current.index(0)

  # Horizontal
  distance += abs(g_i % s.size - c_i % s.size)
  # Vertical
  distance += abs(g_i / s.size - c_i / s.size)

  return distance

def misplaced_tiles(current, goal, s):
  distance = 0

  for i in current:
    if i is not 0:
      if (goal.index(i) != current.index(i)):
        distance += 1
  return distance

def linear_conflict(current, goal, s):
  distance = 0
  
  for i in current:
    if i is not 0:
      g_i = goal.index(i)
      c_i = current.index(i)
      res_x = abs(g_i % s.size - c_i % s.size)
      res_y = abs(g_i / s.size - c_i / s.size)
      distance += res_x + res_y
      # Conflicts
      if (current[g_i] == goal[c_i]):
        # Horizontal conflict
        if (g_i % s.size - c_i % s.size >= 1 and g_i % s.size - c_i % s.size < s.size and g_i / s.size - c_i / s.size == 0):
          distance += 2
        # Vertical conflict
        if (g_i / s.size - c_i / s.size >= 1 and g_i / s.size - c_i / s.size < s.size and g_i % s.size - c_i % s.size == 0):
          distance += 2
  return distance

def pattern_database(current, goal, s):
  distance = 0

  for i in goal:
    if i is not -1:
      g_i = goal.index(i)
      c_i = current.index(i)
      res_x = abs(g_i % s.size - c_i % s.size)
      res_y = abs(g_i / s.size - c_i / s.size)
      distance += res_x + res_y

  return distance

heuristic_functions = {
  "manhattan_distance": manhattan_distance,
  "xy": xy,
  "misplaced_tiles": misplaced_tiles,
  "linear_conflict": linear_conflict,
  "pattern_database": pattern_database
}

def get(heuristic):
  return heuristic_functions[heuristic]
