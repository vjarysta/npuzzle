import get_args
import get_puzzle
import search_algorithm

def solvable(puzzle, size):
  inversions = 0
  blank_row = 0

  for i in puzzle:
    for j in puzzle[puzzle.index(i) + 1:]:
      if i > j and i != 0 and j != 0:
        inversions += 1

  if size % 2 == 0:
    blank_row = puzzle.index(0) / size + 1

  if (inversions + blank_row) % 2 == 0:
    return True
  else:
    return False

def display_results(res):
  print "Complexity in time :", res.total_set
  print "Complexity in size :", res.max_set
  print "Number of moves :", len(res.solution)
  print "Solution :"
  for solution in res.solution:
    print solution

def main():
  args = get_args.get_args()
  if args.file:
    initial_state = get_puzzle.from_file(args)
  else:
    initial_state = get_puzzle.from_generator(args.size)
  if not solvable(initial_state, args.size):
    print "Puzzle not solvable."
    return 0
  goal_state = get_puzzle.goal(args.size)
  solver = search_algorithm.IDA_star(initial_state, goal_state, args.size, args.heuristic)
  res = solver.solve()
  display_results(res)
