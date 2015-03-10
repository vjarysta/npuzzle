import argparse
import os.path

def is_valid_file(parser, arg):
  if not os.path.exists(arg):
    parser.error("The file %s does not exist" % arg)
  else:
    return open(arg, 'r')

def argv_process():
  parser = argparse.ArgumentParser(description='A Python N-puzzle solver using IDA* algorithm coupled with an optional set of heuristic functions.')
  parser.add_argument('--size', type=int, default=3)
  parser.add_argument('--heuristic', type=str, default='manhattan_distance', choices=['manhattan_distance', 'pattern_database'])
  parser.add_argument('--file', type=lambda x: is_valid_file(parser, x))
  args = parser.parse_args()

def main():
  argv_process()