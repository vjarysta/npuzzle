from get_args import get_args
import get_puzzle

def main():
  args = get_args()
  if args.file:
    initial_state = get_puzzle.from_file(args)
  else:
    initial_state = get_puzzle.from_generator(args.size)
  goal_state = get_puzzle.goal(args.size)

  print "=== SIZE ===\n", args.size
  print "=== GOAL STATE ===\n", goal_state
  print "=== INITIAL STATE ===\n", initial_state
