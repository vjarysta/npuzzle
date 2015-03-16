import re
import random

def goal(size):
  goal = range(1, size * size)
  goal.append(0)
  return goal

def from_generator(size):
  puzzle = goal(size)

  for i in range(300):
    i = puzzle.index(0)
    x = i % size
    y = i / size
    moves = []
    if (x + 1 < size):
      moves.append((x + 1) + ((y) * size))
    if (y + 1 < size):
      moves.append((x) + ((y + 1) * size))
    if (x > 0):
      moves.append((x - 1) + ((y) * size))
    if (y > 0):
      moves.append((x) + ((y - 1) * size))
    to_swap = random.choice(moves)
    puzzle[to_swap], puzzle[i] = puzzle[i], puzzle[to_swap]

  return puzzle

def from_file(args):
  clean_file = map(int, re.sub("[^0-9]", " ", args.file.read()).split())
  args.size = clean_file[0]
  return clean_file[1:]
