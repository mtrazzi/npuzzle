import sys
import random
import numpy as np
import re

def make_puzzle(s, solvable, iterations):
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

  p = make_goal(s)
  for _ in range(iterations):
    swap_empty(p)

  if not solvable:
    if p[0] == 0 or p[1] == 0:
      p[-1], p[-2] = p[-2], p[-1]
    else:
      p[0], p[1] = p[1], p[0]

  return p

def make_goal(s):
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

def puzzle_from_text(filename):
  size = 0
  puzzle = []
  with open(filename, 'r') as f:
    lines = [re.sub('#.*', '', line.strip()) for line in f]
    lines = [line for line in lines if line]
    try:
      size = int(lines[0])
      if len(lines[1:]) != size:
        print ("Error: Input size doesn't match puzzle height.")
        return []
      for line in lines[1:]:
        split = line.split()
        if size != len(split):
          print ("Error: Input size doesn't match puzzle width.")
          return []
        puzzle.extend([int(x) for x in split])
    except:
      print("Error: File format not supported please try with another file.")
      return []

  return puzzle

def generate_puzzle_tab(solvable, size, iterations, filename):
  if filename:
    puzzle = puzzle_from_text(filename)
    if len(puzzle) == 0:
      sys.exit(1)
    return puzzle

  if size < 3:
    print("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
    sys.exit(1)

  if solvable is None:
    solvable = random.choice([True, False])

  return make_puzzle(size, solvable, iterations=iterations)
