import numpy as np
import copy

from core.npuzzle_gen import make_goal

def find_coordinates(tab, elt):
  for i in range(len(tab)):
    for j in range(len(tab)):
      if tab[i][j] == elt:
        return i, j

class Puzzle(object):
  def __init__(self, puzzle_str):
    # convert back to list
    puzzle = [int(x) for x in puzzle_str[1:-1].split(',')]
    self.state = puzzle
    self.size = int(np.sqrt(len(puzzle)))
    self.goal = make_goal(self.size)
    self.grid = [[puzzle[x * self.size + y] for y in range(self.size)] for x in range(self.size)]
    self.goal_grid = [[make_goal(self.size)[x * self.size + y] for y in range(self.size)] for x in range(self.size)]

  def next_state(self, move):
    x_0, y_0 = find_coordinates(self.grid, 0)
    state = copy.deepcopy(self.state)
    size = self.size
    if move == "UP" and x_0 > 0:
      state[x_0 * size + y_0], state[(x_0 - 1) * size + y_0] = state[(x_0 - 1) * size + y_0], 0
    elif move == "DOWN" and x_0 < self.size - 1:
      state[x_0 * size + y_0], state[(x_0 + 1) * size + y_0] = state[(x_0 + 1) * size + y_0], 0
    elif move == "LEFT" and y_0 > 0:
      state[x_0 * size + y_0], state[x_0 * size + y_0 - 1] = state[x_0 * size + y_0 - 1], 0
    elif move == "RIGHT" and y_0 < self.size - 1:
      state[x_0 * size + y_0], state[x_0 * size + y_0 + 1] = state[x_0 * size + y_0 + 1], 0
    return str(state)

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
      if neighbor == str(self.state):
        neighbors.remove(neighbor)
    return neighbors

  def nb_permutation(self):
    # go through elements of grid following the path of goal (e.g. a snail)
    nb_inv = 0
    for i in range(1, self.size ** 2):
      x_i, y_i = find_coordinates(self.goal_grid, i)
      # check number of inversions ahead
      for j in list(range(i + 1, self.size ** 2)) + [0]:
        x_j, y_j = find_coordinates(self.goal_grid, j)
        if self.grid[x_i][y_i] > 0 and self.grid[x_j][y_j] > 0:
          nb_inv += self.grid[x_i][y_i] > self.grid[x_j][y_j]
    return nb_inv

  def is_in_row_solvable(self):
    nb_per = self.nb_permutation()
    x_0, _ = find_coordinates(self.grid, 0)
    return nb_per % 2 == 0 if self.size % 2 == 1 else (self.size - x_0 - nb_per) % 2 == 1

  def is_snail_solvable(self):
    return self.nb_permutation() % 2 == 0
