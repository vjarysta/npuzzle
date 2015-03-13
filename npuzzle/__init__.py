import get_args
import get_puzzle
import search_algorithm

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
  goal_state = get_puzzle.goal(args.size)
  solver = search_algorithm.IDA_star(initial_state, goal_state, args.size, args.heuristic)
  res = solver.solve()
  display_results(res)
