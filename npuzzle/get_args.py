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

  parser = argparse.ArgumentParser(description='A Python N-puzzle solver using IDA* algorithm coupled with an optional set of heuristic functions.')
  parser.add_argument('--size', type=lambda x: is_valid_size(parser, x), default=3, help="set size of the puzzle (min. 2). Default is 3. --file overrides this option.")
  parser.add_argument('--heuristic', type=str, default='manhattan_distance', choices=['manhattan_distance', 'xy', 'misplaced_tiles', 'linear_conflict', 'pattern_database'], help="set the heuristic function used by IDA*. Default to manhattan_distance.")
  parser.add_argument('--file', type=lambda x: is_valid_file(parser, x), help="use a file as puzzle. Overrides the --size option.")
  return parser.parse_args()
