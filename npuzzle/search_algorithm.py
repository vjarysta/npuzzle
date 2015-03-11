from manhattan import manhattan

class IDA_star:

  def __init__(self, initial, goal, size):
    self.initial = initial
    self.goal = goal
    self.size = size
    self.solution = []

  def get_next_states(self, state, size):
    def get_moves():
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
      return moves

    def get_states(moves):
      states = []
      for move in moves:
        states.append(state[:])
        states[-1][move], states[-1][i] = states[-1][i], states[-1][move]
      return states

    def prioritize_states(states):
      def by_heuristic(state):
        return manhattan(state, self.goal)
      return sorted(states, key=by_heuristic)

    i = state.index(0)
    moves = get_moves()
    states = get_states(moves)
    return prioritize_states(states)

  def search(self, state, g, threshold):
    h = manhattan(state, self.goal)
    if h == 0:
      return h
    f = g + h
    if f > threshold:
      return f
    next_threshold = 0
    for next_state in self.get_next_states(state, self.size):
      h = manhattan(state, next_state)
      res = self.search(next_state, g + h, threshold)
      if res == 0:
        self.solution.insert(0, state)
        return res
      elif next_threshold == 0 or res < next_threshold:
        next_threshold = res
    return next_threshold

  def solve(self):
    threshold = manhattan(self.initial, self.goal)
    while 1:
      print threshold
      res = self.search(self.initial, 0, threshold)
      if res == 0:
        self.solution.append(self.goal)
        break
      else:
        threshold = res
    return self.solution