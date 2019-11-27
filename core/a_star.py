import numpy as np

def heuristic(puzzle, name='tiles-out'):
  #TODO: add manhattan and euclidean heuristics
  s = puzzle.size
  g = puzzle.goal
  if name == 'tiles-out':
    return s ** 2 - len(set(puzzle.puzzle_list) & set(puzzle.goal))

def reconstruct_path(came_from, current):
  total_path = [current]
  while current in came_from:
    current = came_from[current]
    total_path.insert(0, current)
  return total_path

class AStar(object):
  # cf. pseudocode from https://en.wikipedia.org/wiki/A*_search_algorithm
  def __init__(self, puzzle, hname='tiles-out'):
    # maps integers to puzzle states
    self.states = [puzzle]

    # special heuristic for h
    self.hname = hname

    # utils
    self.size = puzzle.size
    self.goal = puzzle.goal

    # for the output TODO: update those values in _run_
    self.nb_opened_st = 0
    self.max_nb_st_mem = 0
    self.path = []
    self.open_set = [0]

    # For node n, came_from[n] is the node immediately preceding it
    # on the cheapest path from start to n currently known.
    self.came_from = {}

    # heuristic maps (g[0] correspond to g(state_0))
    # IN THE REST OF THE CODE TRIED TO DEAL WITH STATES_ID TO NOT PASS GIGANTIC PUZZLES... MAYBE CONFUSING
    self.g = [0]
    self.h = [heuristic(self.states[0])]
    self.f = [self.h[0]]

  def run(self):
    while self.open_set:
      current = np.argmin(self.f) #id of the state with lowest f score
      current_state = self.states[current]
      if self.states[current] == self.goal:
        return reconstruct_path(self.came_from, current)

      # remove the state
      del self.open_set[current]
      del self.states[current]

      for neighbor in current_state.neighbors():
        neighbor_id = self.states.index(neighbor) if neighbor in self.states else len(self.states)
        if not neighbor in self.states:
          self.states.append(neighbor)
        tentative_g = self.g[current] + 1 # weight of edges are 1
        if tentative_g < self.g[neighbor_id]:
          self.came_from[neighbor_id] = current
          self.g[neighbor_id] = tentative_g
          self.f[neighbor_id] = self.g[neighbor_id] + self.h[neighbor_id]
          if not neighbor in self.open_set:
            self.open_set.append(neighbor_id)
