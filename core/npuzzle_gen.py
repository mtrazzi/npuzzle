import random
import numpy as np
import re

def make_puzzle(s, _type, solvable, iterations):
  """Generate a puzzle

  Parameters
  ----------
  s: int
    Puzzle size
  _type: str
    Puzzle type ∈ ['snail', 'row']
  solvable: bool
    Does the NPuzzle need to be solvable
  iteration: int
    Number of passes to shuffle the NPuzzle

  Return
  ------
  p: list
    The Puzzle to be solved
  """
  def swap_empty(p):
    idx = p.index(0)
    poss = []
    if idx % s > 0:
      poss.append(idx - 1)
    if idx % s < s - 1:
      poss.append(idx + 1)
    if idx / s > 0 and idx - s >= 0:
      poss.append(idx - s)
    if idx / s < s - 1:
      poss.append(idx + s)
    swi = random.choice(poss)
    p[idx] = p[swi]
    p[swi] = 0

  p = make_goal(s, _type)
  for _ in range(iterations):
    swap_empty(p)

  if not solvable:
    if p[0] == 0 or p[1] == 0:
      p[-1], p[-2] = p[-2], p[-1]
    else:
      p[0], p[1] = p[1], p[0]

  return p

def make_goal(size, _type='snail'):
  """Generate goal

  Parameters
  ----------
  size: int
    Puzzle size
  _type: str
    Puzzle type ∈ ['snail', 'row']

  Return
  ------
  goal: list
    The Puzzle Goal
  """
  goal = make_goal_snail(size) if _type == 'snail' else make_goal_row(size)
  return goal

def make_goal_row(s):
  """Generate goal for 'row' type NPuzzle"""
  p = [x for x in range(1, s**2)]
  p.append(0)
  return p

def make_goal_snail(s):
  """Generate goal for 'snail' type NPuzzle"""
  ts = s*s
  puzzle = [-1 for i in range(ts)]
  cur = 1
  x = 0
  ix = 1
  y = 0
  iy = 0
  while True:
    puzzle[x + y * s] = cur
    if cur == 0:
      break
    cur += 1
    if x + ix == s or x + ix < 0 or (ix != 0 and puzzle[x + ix + y * s] != -1):
      iy = ix
      ix = 0
    elif y + iy == s or y + iy < 0 or (iy != 0 and puzzle[x + (y + iy) * s] != -1):
      ix = -iy
      iy = 0
    x += ix
    y += iy
    if cur == s * s:
      cur = 0
  return puzzle

def puzzle_from_text(filename, _type):
  """Generate a NPuzzle for a given file and type"""
  size = 0
  puzzle = []
  with open(filename, 'r') as f:
    lines = [re.sub('#.*', '', line.strip()) for line in f]
    lines = [line for line in lines if line]
    try:
      size = int(lines[0])
      if size < 3:
        raise Exception("Can't generate a puzzle with size lower than 2. It says so in the help.")
      if len(lines[1:]) != size:
        raise Exception("Input size doesn't match puzzle height.")

      for line in lines[1:]:
        split = line.split()
        if size != len(split):
          raise Exception("Input size doesn't match puzzle width.")
        puzzle.extend([int(x) for x in split])
    except:
      raise Exception("File format not supported please try with another file.")
  return puzzle, make_goal(size, _type), size

def puzzle_from_stdin():
  """Generate a NPuzzle from user input"""
  puzzle = []
  goal = []
  size = int(input("Puzzle size: "))
  if size < 3:
    raise Exception("Can't generate a puzzle with size lower than 2. It says so in the help.")
  print("Enter puzzle arrangement:")
  for _ in range(size):
    line = input()
    split = line.split()
    if size != len(split):
      raise Exception("Input size doesn't match puzzle width.")
    puzzle.extend([int(x) for x in split])
  print("\nEnter goal arrangement:")
  for _ in range(size):
    line = input()
    split = line.split()
    if size != len(split):
      raise Exception("Input size doesn't match puzzle width.")
    goal.extend([int(x) for x in split])
  return puzzle, goal, size

def generate_puzzle_tab(solvable, size, _type, iterations, interactive, filename):
  """Generate function

  Parameters
  ----------
  solvable: bool
    Does the NPuzzle need to be solvable
  size: int
    Size of the the NPuzzle
  _type: str
    NPuzzle type ∈ ['snail', 'row']
  iteration: int
    Number of passes to shuffle the NPuzzle
  interactive: bool
    Set interactive mode to generate NPuzzle
  filename: str
    Generate NPuzzle from file

  Return
  ------
  (state, goal, size): (list, list, int)
    state: The current state of the puzzle
    goal : The state we need to achieved if possible
    size : The size of the puzzle
  """
  if interactive:
    return puzzle_from_stdin()
  if filename:
    return puzzle_from_text(filename, _type)
  if size < 3:
    raise Exception("Can't generate a puzzle with size lower than 2. It says so in the help.")
  if solvable is None:
    solvable = random.choice([True, False])

  return make_puzzle(size, _type, solvable, iterations=iterations), make_goal(size, _type), size
