#!/usr/bin/env python3

import argparse
import random
import sys

from core.npuzzle_gen import generate_puzzle_tab
from core.a_star import A_Star
from core.puzzle import Puzzle, print_state

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("--size", type=int, default=None, help="Size of the puzzle's side. Must be >3.")
  parser.add_argument("-s", "--solvable", action="store_true", default=None, help="Forces generation of a solvable puzzle. Overrides -u.")
  parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle.")
  parser.add_argument("-i", "--iterations", type=int, default=10000, help="Number of passes.")
  parser.add_argument("-f", "--filename", type=str, default=None, help="Generate puzzle from file.")
  parser.add_argument("--heuristic", type=str, default='manhattan', choices=['manhattan', 'euclidean', 'tiles-out'], help="Heuristic function (must be admissible).")

  args = parser.parse_args()

  if args.size is None and args.filename is None:
    print("One of --size or --filename is required. See -h for help.")
    sys.exit(1)

  solvable = args.solvable if not args.unsolvable else False

  random.seed()
  puzzle = Puzzle(generate_puzzle_tab(solvable, args.size, args.iterations, args.filename))

  print("Initial State:")
  print_state(puzzle.state, puzzle.size)

  if not puzzle.is_snail_solvable():
    print("Puzzle is not snail solvable, exiting.")
    sys.exit(0)

  print("Starting A* ...\n")
  totalPath, pathLen, nbOpen, nbSelected = A_Star(puzzle.state, puzzle.goal, puzzle.size)
  if pathLen == 0:
    print("No Solution found.")

  print(f"Complexity in time: {nbOpen}\nComplexity in size: {nbSelected}\n\nNumber of moves required: {pathLen}")
  stateId = 0
  for path in totalPath:
    print(f"\nState {stateId}:")
    print_state(path, puzzle.size)
    stateId += 1
