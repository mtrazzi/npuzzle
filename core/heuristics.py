import numpy as np

def heuristic_aux(x, y, x_g, y_g, name):
  if name == 'tiles-out':
    return x != x_g or y != y_g
  elif name == 'manhattan':
    return abs(x-x_g) + abs(y-y_g)
  elif name == 'euclidean':
    return np.sqrt((x-x_g) ** 2 + (y-y_g) ** 2)

def heuristic(goal, state, name='manhattan'):
  size = int(np.sqrt(len(goal)))

  coord_goal = np.zeros((size ** 2, 2)) # in index i coordinates of tile i in goal
  coord_state = np.zeros((size ** 2,2)) # in index i coordinates of tile i in state
  for x in range (size):
    for y in range (size):
      coord_goal[goal[x * size + y]] = [x,y]
      coord_state[state[x * size + y]] = [x,y]

  return np.sum([heuristic_aux(coord_state[i][0], coord_state[i][1], coord_goal[i][0], coord_goal[i][1], name) for i in range(size ** 2)])
