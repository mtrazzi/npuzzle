#!/usr/bin/env python3

import argparse
import sys

from core.core import Solve

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("--size", type=int, default=None, help="Size of the puzzle's side. Must be >3.")
  parser.add_argument("-s", "--solvable", action="store_true", default=None, help="Forces generation of a solvable puzzle. Overrides -u.")
  parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle.")
  parser.add_argument("-i", "--interactive", action="store_true", default=False, help="Enable interactive mode. Overrides --size -f.")
  parser.add_argument("-n", "--iterations", type=int, default=10000, help="Number of passes.")
  parser.add_argument("-f", "--filename", type=str, default=None, help="Generate puzzle from file. Overrides --size.")
  parser.add_argument("-t", "--type", type=str, default="snail", choices=['snail', 'row'], help="NPuzzle type.")
  parser.add_argument("-a", "--algorithm", type=str, default="A*", choices=['A*', 'BFS'], help="Algorithm used for search. Uniform-cost search: Breadth-first search (BFS). Greedy search: A*.")
  parser.add_argument("--heuristic", type=str, default='euclidean', choices=['euclidean', 'manhattan', 'tiles-out', 'uniform-cost'], help="Heuristic function")
  parser.add_argument("-d", "--demo", action="store_true", default=True, help="Print every step to the solution.")

  args = parser.parse_args()

  if args.interactive is False and args.size is None and args.filename is None:
    print("One of -i or --size or --filename is required. See -h for help.")
    sys.exit(1)

  solvable = args.solvable if not args.unsolvable else False

  try:
    Solve(algorithm=args.algorithm, heuristic=args.heuristic,
          _type=args.type, solvable=solvable, size=args.size,
          iterations=args.iterations, interactive=args.interactive, filename=args.filename, demo=args.demo)
  except Exception as e:
    print(f"Error: {e}")
    sys.exit(2)
  except:
    print("Error while solving. Exiting...")
    sys.exit(3)
