import get_args
import get_puzzle
import search_algorithm

def solvable(puzzle, size):
  return True
  # inversions = 0
  # blank_row = 0

  # for i in puzzle:
  #   for j in puzzle[puzzle.index(i) + 1:]:
  #     if i > j and i != 0 and j != 0:
  #       inversions += 1

  # if size % 2 == 0:
  #   blank_row = puzzle.index(0) / size + 1

  # if (inversions + blank_row) % 2 == 0:
  #   print "inversions:", inversions
  #   return True
  # else:
  #   return False

def display_results(results):
  print "Complexity in time :", sum([res.total_set for res in results])
  print "Complexity in size :", sum([res.max_set for res in results])
  print "Number of moves :", sum([len(res.solution) for res in results]) - len(results) + 1
  print "Solution :"
  for res in results:
    prev = []
    for solution in res.solution:
      if solution != prev:
        print solution
      prev = solution

def main():
  args = get_args.get_args()

  if args.file:
    initial_state = get_puzzle.from_file(args)
  else:
    initial_state = get_puzzle.from_generator(args.size)

  if not solvable(initial_state, args.size):
    print "Puzzle not solvable."
    return 0

  res = []
  p_db = 0
  if args.heuristic == "pattern_database":
    for pattern in get_puzzle.patterns(get_puzzle.goal(args.size), args.size):
        if len(res):
          initial_state = res[-1].current
        solver = search_algorithm.get_algorithm(args.algorithm)(initial_state, pattern, args.size, args.heuristic, p_db)
        res.append(solver.solve())
        p_db += 1
  else:
    goal_state = get_puzzle.goal(args.size)
    solver = search_algorithm.get_algorithm(args.algorithm)(initial_state, goal_state, args.size, args.heuristic, p_db)
    res.append(solver.solve())

  display_results(res)
