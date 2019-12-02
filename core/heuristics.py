import numpy as np

def heuristic_aux(x, y, x_g, y_g, name):
  """Admissible heuristics

  Parameters
  ----------
  x, y: int
    state coordinate
  x_g, y_g: int
    goal coordinate
  name: str
    heuristic function name

  Return
  ------
  Float:
    Corresponding heuristic value for a single coordinate
  """
  if name == 'tiles-out':
    return x != x_g or y != y_g
  elif name == 'manhattan':
    return abs(x-x_g) + abs(y-y_g)
  elif name == 'euclidean':
    return np.sqrt((x-x_g) ** 2 + (y-y_g) ** 2)
  elif name == 'uniform-cost':
    return 0

def heuristic(goal, state, name='euclidean'):
  """Heuristic function

  Parameters
  ----------
  goal: list
    Puzzle state we want to achieve
  state: list
    Current Puzzle state
  name: str (Default: 'euclidean')
    Name of heuristic function to use ∈ ['euclidean', 'manhattan', 'tiles-out', 'uniform-cost']

  Returns
  -------
  One of
    'Tiles-out': float
      Number of tiles in the wrong position
    'Manhattan': float
      Sum of the horizontal and vertical distances between,
      current position and desired position, i.e. ∑ |state - goal|
    'Euclidean': float
      Sum of the distance between tiles
      ∑ √(x - x_g)² + (y - y_g)²
  """
  size = int(np.sqrt(len(goal)))

  coord_goal  = np.zeros((size ** 2, 2)) # in index i coordinates of tile i in goal
  coord_state = np.zeros((size ** 2, 2)) # in index i coordinates of tile i in state
  for x in range (size):
    for y in range (size):
      coord_goal[ goal[ x * size + y]] = [x, y]
      coord_state[state[x * size + y]] = [x, y]

  return np.sum([heuristic_aux(*coord_state[i], *coord_goal[i], name) for i in range(size ** 2)])
