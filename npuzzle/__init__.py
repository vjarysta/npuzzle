import get_args
import get_puzzle
import search_algorithm
import time

def solvable(puzzle, goal, size):
  inversions = 0
  blank_row = 0

  for i in puzzle:
    for j in puzzle[puzzle.index(i) + 1:]:
      if goal.index(i) > goal.index(j) and i != 0 and j != 0:
        inversions += 1

  if size % 2 == 0:
    blank_row = puzzle.index(0) / size + (goal.index(0) / size)

  if (inversions + blank_row) % 2 == 0:
    return True
  else:
    return False

def display_results(results):
  print "Complexity in time :", sum([res.total_set for res in results])
  print "Complexity in size :", sum([res.max_set for res in results])
  print "Number of moves :", sum([len(res.solution) for res in results]) - len(results)
  print "Solution :"
  prev = []
  for res in results:
    for solution in res.solution:
      if solution != prev:
        print solution
      prev = solution

def main():        
  args = get_args.get_args()

  if args.file:
    initial_state = get_puzzle.from_file(args)
  else:
    initial_state = get_puzzle.from_generator(args.size, args.shuffle)

  if not solvable(initial_state, get_puzzle.goal(args.size), args.size):
    print "Unsolvable puzzle"
    return 0

  res = []
  p_db = 0
  start = None
  if args.heuristic == "pattern_database":
    for pattern in get_puzzle.patterns(get_puzzle.goal(args.size), args.size):
        if len(res):
          initial_state = res[-1].current
        solver = search_algorithm.get_algorithm(args.algorithm)(initial_state, pattern, args.size, args.heuristic, p_db)
        if not start:
          start = time.time()
        res.append(solver.solve())
        p_db += 1
        if res[-1] == -1:
          break
  else:
    goal_state = get_puzzle.goal(args.size)
    solver = search_algorithm.get_algorithm(args.algorithm)(initial_state, goal_state, args.size, args.heuristic, p_db)
    start = time.time()
    res.append(solver.solve())

  if res[-1] != -1:
    print "Solved in %s miliseconds" % (int((time.time() - start) * 1000))
    display_results(res)
