import sys
import random

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
  for i in range(iterations):
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

def puzzle_from_text(filename, dir_name='puzzles'):
  path = os.path.join(dir_name, filename)
  with open(path, 'r') as f:
    lines = [list(l.rstrip('\n')) for l in f]
  return lines[1:]

def generate_puzzle_tab(solvable, unsolvable, size, iterations, filename):
  if filename:
    return puzzle_from_text(filename)

  if solvable and unsolvable:
    print("Can't be both solvable AND unsolvable, dummy !")
    sys.exit(1)

  if size < 3:
    print("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
    sys.exit(1)

  if not solvable and not unsolvable:
    solv = random.choice([True, False])
  elif solvable:
    solv = True
  elif unsolvable:
    solv = False

  s = size

  return make_puzzle(s, solvable=solv, iterations=iterations)
