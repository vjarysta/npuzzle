import get_args
import get_puzzle
import search_algorithm

def main():
  args = get_args.get_args()
  if args.file:
    initial_state = get_puzzle.from_file(args)
  else:
    initial_state = get_puzzle.from_generator(args.size)
  goal_state = get_puzzle.goal(args.size)
  solver = search_algorithm.IDA_star(initial_state, goal_state, args.size, args.heuristic)
  solution = solver.solve()

  print "FOUND !\nNumber of move:", len(solution) - 1
# TEMPORARY SOLUTION PRINTING
  # for state in solution:
  #   print "======"
  #   for i in range(args.size):
  #     print state[i * args.size:(i + 1) * args.size]
