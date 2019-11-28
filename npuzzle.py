#!/usr/bin/env python3

import argparse
import random
import sys

from core.npuzzle_gen import generate_puzzle_tab
from core.a_star import A_Star
from core.puzzle import Puzzle

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("--size", type=int, default=0, help="Size of the puzzle's side. Must be >3.")
  parser.add_argument("-s", "--solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
  parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
  parser.add_argument("-i", "--iterations", type=int, default=10000, help="Number of passes")
  parser.add_argument("-f", "--filename", type=str, default=None, help="Test file from puzzles/")
  parser.add_argument("--heuristic", type=str, default='manhattan', choices=['manhattan', 'euclidean', 'tiles-out'], help="Heuristic function; must be admissible.")

  args = parser.parse_args()

  random.seed()

  puzzle_tab = generate_puzzle_tab(args.solvable, args.unsolvable, args.size, args.iterations, args.filename)

  puzzle = Puzzle(str(puzzle_tab))
  puzzle.print_state()

  if not puzzle.is_snail_solvable():
    print("Puzzle is not snail solvable, exiting.")
    sys.exit(0)

  totalPath, pathLen, nbOpen, nbSelected = A_Star(puzzle)
  if pathLen == 0:
    print("No Solution found.")

  print(f"Complexity in time: {nbOpen}\nComplexity in size: {nbSelected}\n\nNumber of moves required: {pathLen}")
  stateId = 0
  for path in totalPath:
    print(f"\nState {stateId}:")
    stateId += 1
    for i in range(puzzle.size**2):
      print(Puzzle(path).state[i], end=" ")
      if (i+1) % puzzle.size == 0:
        print()
