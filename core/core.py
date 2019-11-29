
import random

from core.npuzzle_gen import generate_puzzle_tab
from core.search import A_Star, BFS
from core.puzzle import Puzzle, print_state

def Solve(algorithm, heuristic, _type, solvable, size, iterations, interactive, filename):
  random.seed()
  state, goal, size = generate_puzzle_tab(solvable, size, _type, iterations, interactive, filename)
  puzzle = Puzzle(state, goal, size)

  if not interactive:
    print("Initial State:")
    print_state(puzzle.state, puzzle.size)

  if not puzzle.is_snail_solvable():
    print("Puzzle is not snail solvable, exiting.")
    return 0

  print("Starting Search...\n")
  if algorithm == "BFS":
    totalPath, pathLen, nbOpen, nbSelected = BFS(puzzle.state, puzzle.goal, puzzle.size)
  else:
    totalPath, pathLen, nbOpen, nbSelected = A_Star(puzzle.state, puzzle.goal, puzzle.size, hname=heuristic)

  if len(totalPath) == 0:
    print("No solution found.")
    return

  print(f"Total number of states ever selected in the openSet (Complexity in time): {nbOpen}")
  print(f"Maximum number of states ever represented in memory at the same time during the search (Complexity in size): {nbSelected}\n")
  print(f"\nNumber of moves required: {pathLen}")
  stateId = 0
  for path in totalPath:
    print(f"\nState {stateId}:")
    print_state(path, puzzle.size)
    stateId += 1
