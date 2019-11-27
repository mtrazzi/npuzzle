import numpy as np
import copy

from core.npuzzle_gen import make_goal

class Puzzle(object):
  def __init__(self, puzzle):
    self.puzzle_list = puzzle
    self.size = int(np.sqrt(len(puzzle)))
    self.goal = make_goal(self.size)
    self.puzzle_grid = [[self.puzzle_list[x * self.size + y] for y in range(self.size)] for x in range(self.size)]

  def next_state(self, move):
    # finding the coordinates of the empty cell
    for i in range(self.size):
      for j in range(self.size):
        if self.puzzle_grid[i][j] == 0:
          x_0, y_0 = i, j

    # making the switch
    neighbor_candidate = copy.copy(self)
    grid = neighbor_candidate.puzzle_grid
    if move == "UP" and x_0 > 0:
      grid[x_0][y_0], grid[x_0 - 1][y_0] = grid[x_0 - 1][y_0], 0
    if move == "DOWN" and x_0 < self.size - 1:
      grid[x_0][y_0], grid[x_0 + 1][y_0] = grid[x_0 + 1][y_0], 0
    if move == "LEFT" and y_0 > 0:
      grid[x_0][y_0], grid[x_0][y_0 - 1] = grid[x_0][y_0 - 1], 0
    if move == "RIGHT" and y_0 < self.size - 1:
      grid[x_0][y_0], grid[x_0][y_0 + 1] = grid[x_0][y_0 + 1], 0
    return neighbor_candidate

  def is_solved(self):
    return self.puzzle_list == self.goal

  def print_state(self):
    s = self.size
    print("%d" % s)
    for y in range(s):
      for x in range(s):
        print("%s" % (str(self.puzzle_list[x + y*s]).ljust(s + 1)), end='')
      print()

  def neighbors(self):
    return [self.next_state(move) for move in ["UP", "RIGHT", "DOWN", "LEFT"] if self.next_state(move) != self]
