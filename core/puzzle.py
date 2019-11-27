import numpy as np
import copy

from core.npuzzle_gen import make_goal

def find_coordinates(tab, elt):
  for i in range(len(tab)):
    for j in range(len(tab)):
      if tab[i][j] == elt:
        return i, j

class Puzzle(object):
  def __init__(self, puzzle):
    self.state = puzzle
    self.size = int(np.sqrt(len(puzzle)))
    self.goal = make_goal(self.size)
    self.grid = [[puzzle[x * self.size + y] for y in range(self.size)] for x in range(self.size)]
    self.goal_grid = [[make_goal(self.size)[x * self.size + y] for y in range(self.size)] for x in range(self.size)]

  def heuristic(self, name='tiles-out'):
    s = 0
    for x in range (self.size):
      for y in range (self.size):
        x_g, y_g = find_coordinates(self.goal_grid, self.grid[x][y])
        if name == 'tiles-out':
          s += x != x_g or y != y_g
        elif name == 'manhattan':
          s += abs(x-x_g) + abs(y-y_g)
        elif name == 'euclidean':
          s += np.sqrt((x-x_g) ** 2 + (y-y_g) ** 2)
    return s

  def next_state(self, move):
    x_0, y_0 = find_coordinates(self.grid, 0)
    neighbor_candidate = copy.deepcopy(self)
    grid = neighbor_candidate.grid
    if move == "UP" and x_0 > 0:
      grid[x_0][y_0], grid[x_0 - 1][y_0] = grid[x_0 - 1][y_0], 0
    elif move == "DOWN" and x_0 < self.size - 1:
      grid[x_0][y_0], grid[x_0 + 1][y_0] = grid[x_0 + 1][y_0], 0
    elif move == "LEFT" and y_0 > 0:
      grid[x_0][y_0], grid[x_0][y_0 - 1] = grid[x_0][y_0 - 1], 0
    elif move == "RIGHT" and y_0 < self.size - 1:
      grid[x_0][y_0], grid[x_0][y_0 + 1] = grid[x_0][y_0 + 1], 0
    neighbor_candidate.state = list(np.array(grid).flatten())
    return neighbor_candidate

  def is_solved(self):
    return self.grid == self.goal_grid

  def print_state(self):
    s = self.size
    print("%d" % s)
    for x in range(s):
      for y in range(s):
        print("%s" % (str(self.grid[x][y]).ljust(s + 1)), end='')
      print()

  def neighbors(self):
    neighbors = [self.next_state(move) for move in [ "UP", "RIGHT", "LEFT", "DOWN"]]
    for neighbor in neighbors:
      if neighbor.state == self.state:
        neighbors.remove(neighbor)
    return neighbors
