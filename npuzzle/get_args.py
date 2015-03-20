import argparse
import os.path

def get_args():
  def is_valid_file(parser, arg):
    if not os.path.exists(arg):
      parser.error("The file %s does not exist" % arg)
    else:
      return open(arg, 'r')

  def is_valid_size(parser, arg):
    arg = int(arg)
    if arg < 2:
      parser.error("Size must be at least 2")
    else:
      return arg

  def is_valid_shuffle(parser, arg):
    arg = int(arg)
    if arg <= 0:
      parser.error("Shuffle must be at least 1")
    else:
      return arg

  parser = argparse.ArgumentParser(description='A Python N-puzzle solver using IDA* algorithm coupled with an optional set of heuristic functions.')
  parser.add_argument('--size', type=lambda x: is_valid_size(parser, x), default=3, help="set size of the puzzle (min. 2). Default is 3. --file overrides this option.")
  parser.add_argument('--heuristic', type=str, default='pattern_database', choices=['manhattan_distance', 'xy', 'misplaced_tiles', 'linear_conflict', 'pattern_database'], help="set the heuristic function used by the algorithm. Default to manhattan_distance.")
  parser.add_argument('--algorithm', type=str, default='a_star', choices=['a_star', 'ida_star'], help="set the algorithm used to solve n-puzzle. Default to ida_star.")
  parser.add_argument('--file', type=lambda x: is_valid_file(parser, x), help="use a file as puzzle. Overrides the --size option.")
  parser.add_argument('--shuffle', type=lambda x: is_valid_shuffle(parser, x), default=100, help="set how many iterations are done to make the goal puzzle.")
  return parser.parse_args()
