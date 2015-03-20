import re
import random

def patterns(goal, size):
  patterns = []
  tmp = [-1 for n in goal]
  for i in range(size - 3):
    pattern = [-1 for n in goal]
    for n in range(size * size):
      x = n % size
      y = n / size
      if (x >= i and y == i) or (x == i and y > i):
        pattern[n] = goal[n]
        tmp[n] = goal[n]
    patterns.append(pattern)
  for n in range(size * size):
    if tmp[n] == -1:
      tmp[n] = goal[n]
    else:
      tmp[n] = -1
  patterns.append(tmp)
  return patterns

def goal(size):
  total_size = size * size
  puzzle = [-1 for i in range(total_size)]
  current = 1
  x = 0
  i_x = 1
  y = 0
  i_y = 0
  while 42:
    puzzle[x + y * size] = current
    if current == 0:
      break
    current += 1
    if x + i_x == size or x + i_x < 0 or (i_x != 0 and puzzle[x + i_x + y * size] != -1):
      i_y = i_x
      i_x = 0
    elif y + i_y == size or y + i_y < 0 or (i_y != 0 and puzzle[x + (y + i_y) * size] != -1):
      i_x = -i_y
      i_y = 0
    x += i_x
    y += i_y
    if current == size * size:
      current = 0
  return puzzle

def from_generator(size, shuffle):
  puzzle = goal(size)
  prev_swap = -1

  it = 0
  while it < shuffle:
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
    if prev_swap != to_swap:
      puzzle[to_swap], puzzle[i] = puzzle[i], puzzle[to_swap]
      prev_swap = i
      it += 1

  return puzzle

def from_file(args):
  clean_file = map(int, re.sub("[^0-9]", " ", args.file.read()).split())
  args.size = clean_file[0]
  return clean_file[1:]
