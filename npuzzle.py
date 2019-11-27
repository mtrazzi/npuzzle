#!/usr/bin/env python3

import argparse
import random

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

  args = parser.parse_args()

  random.seed()

  puzzle_tab = generate_puzzle_tab(args.solvable, args.unsolvable, args.size, args.iterations, args.filename)

  puzzle = Puzzle(puzzle_tab)
  print("Our Puzzle is solved? {}".format(puzzle.is_solved()))
  puzzle.print_state()

  totalPath = A_Star(puzzle)
  if len(totalPath) == 0:
    print("No Solution found.")
