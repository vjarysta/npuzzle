import heuristic_functions

class IDA_star:

  def __init__(self, initial, goal, size, heuristic, p_db):
    self.initial = initial
    self.previous = initial
    self.current = initial
    self.goal = goal
    self.size = size
    self.solution = []
    self.h = heuristic_functions.get(heuristic)
    self.total_set = 0
    self.max_set = 0
    self.p_db = p_db

  def get_next_states(self, current_state, size):
    def get_moves():
      x = i % size
      y = i / size
      moves = []
      if (x + 1 < size):
        moves.append((x + 1) + ((y) * size))
      if (y + 1 < size):
        moves.append((x) + ((y + 1) * size))
      if (x > (0 + self.p_db)):
        moves.append((x - 1) + ((y) * size))
      if (y > (0 + self.p_db)):
        moves.append((x) + ((y - 1) * size))
      return moves

    def get_states(moves):
      states = []
      for move in moves:
        states.append(current_state[:])
        states[-1][move], states[-1][i] = states[-1][i], states[-1][move]
        if states[-1] == self.previous:
          del states[-1]
      return states

    def prioritize_states(states):
      def by_heuristic(state):
        return self.h(state, self.goal, self)

      return sorted(states, key=by_heuristic)

    i = current_state.index(0)
    moves = get_moves()
    states = get_states(moves)
    return prioritize_states(states)

  def is_goal(self, state):
    for i in range(self.size * self.size):
      if self.goal[i] != -1:
        if self.goal[i] != state[i]:
          return False
    return True 

  def search(self, state, g, threshold):
    self.max_set += 1
    self.total_set += 1
    self.current = state
    if self.is_goal(state):
      return 0
    h = self.h(state, self.goal, self)
    f = g + h
    if f > threshold:
      return f
    next_threshold = -1
    next_states = self.get_next_states(state, self.size)
    for next_state in next_states:
      self.previous = state
      res = self.search(next_state, g + 1, threshold)
      if res == 0:
        self.solution.insert(0, state)
        return 0
      elif next_threshold == -1 or res < next_threshold:
        next_threshold = res
    return next_threshold

  def solve(self):
    threshold = self.h(self.initial, self.goal, self)
    while 1:
      self.max_set = 0
      res = self.search(self.initial, 0, threshold)
      if res == 0:
        self.solution.append(self.current)
        break
      else:
        threshold = res
    return self
