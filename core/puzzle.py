from core.npuzzle_gen import make_goal

def find_coordinates(state, size, elt):
  idx = state.index(elt)
  return (idx // size), (idx % size)

def next_state(state, size, move):
  x_0, y_0 = find_coordinates(state, size, 0)
  state = list(state)
  size = size
  if move == "UP" and x_0 > 0:
    state[x_0 * size + y_0], state[(x_0 - 1) * size + y_0] = state[(x_0 - 1) * size + y_0], 0
  elif move == "DOWN" and x_0 < size - 1:
    state[x_0 * size + y_0], state[(x_0 + 1) * size + y_0] = state[(x_0 + 1) * size + y_0], 0
  elif move == "LEFT" and y_0 > 0:
    state[x_0 * size + y_0], state[x_0 * size + y_0 - 1] = state[x_0 * size + y_0 - 1], 0
  elif move == "RIGHT" and y_0 < size - 1:
    state[x_0 * size + y_0], state[x_0 * size + y_0 + 1] = state[x_0 * size + y_0 + 1], 0
  return tuple(state)

def neighbors(state, size):
  """Give all neighbors for a given State"""
  neighbors = [next_state(state, size, move) for move in [ "UP", "RIGHT", "LEFT", "DOWN"]]
  for neighbor in neighbors:
    if neighbor == state:
      neighbors.remove(neighbor)
  return neighbors

def print_state(state, size):
  """Print given Puzzle state"""
  padding = len(str(size ** 2))
  for i in range(size ** 2):
    print(f"{state[i]:{padding}}", end=" ")
    if (i + 1) % size == 0:
      print("")

class Puzzle(object):
  """Puzzle class

  Parameters
  ----------
  state: list
    Current puzzle state
  goal: list
    State we want to achieve
  size: int
    Puzzle size
  """
  def __init__(self, state, goal, size):
    # convert back to list
    self.state = tuple(state)
    self.goal = tuple(goal)
    self.size = size

  def nb_permutation(self):
    """Find number of permutation for a snail disposition"""
    grid = [[self.state[x * self.size + y] for y in range(self.size)] for x in range(self.size)]
    nb_inv = 0
    for i in range(1, self.size ** 2):
      x_i, y_i = find_coordinates(self.goal, self.size, i)
      for j in list(range(i + 1, self.size ** 2)) + [0]:
        x_j, y_j = find_coordinates(self.goal, self.size, j)
        if grid[x_i][y_i] > 0 and grid[x_j][y_j] > 0:
          nb_inv += grid[x_i][y_i] > grid[x_j][y_j]
    return nb_inv

  def is_row_solvable(self):
    nb_per = self.nb_permutation()
    x_0, _ = find_coordinates(self.state, self.size, 0)
    return nb_per % 2 == 0 if self.size % 2 == 1 else (self.size - x_0 - nb_per) % 2 == 1

  def is_snail_solvable(self):
    return self.nb_permutation() % 2 == 0

  def check(self):
    for x in range(self.size**2):
      if x not in self.state:
        return False
      if x not in self.goal:
        return False
    return True
