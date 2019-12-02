import random
import time
import os

from core.npuzzle_gen import generate_puzzle_tab
from core.search import A_Star, BFS
from core.puzzle import Puzzle, print_state

def Solve(algorithm, heuristic, _type, solvable, size, iterations, interactive, filename, demo):
  """Solve function

  Parameters
  ----------
  algorithm: str
    Name of the algorithm ∈ ['A*', 'BFS']
  heuristic: str
    Name of heuristic ∈ ['euclidean', 'manhattan', 'tiles-out', 'uniform-cost']
  _type: str
    NPuzzle type ∈ ['snail', 'row']
  solvable: bool
    Does the NPuzzle need to be solvable
  size: int
    Size of the the NPuzzle
  iteration: int
    Number of passes to shuffle the NPuzzle
  interactive: bool
    Set interactive mode to generate NPuzzle
  filename: str
    Generate NPuzzle from file
  demo: bool
    Tell how to print the solution
  """
  random.seed()
  state, goal, size = generate_puzzle_tab(solvable, size, _type, iterations, interactive, filename)
  puzzle = Puzzle(state, goal, size)

  if not puzzle.check():
    print(f"Puzzle is not well formatted, exiting.")
    return

  if not interactive:
    print("Initial State:")
    print_state(puzzle.state, puzzle.size)
    if demo:
      time.sleep(1)
    if (_type == 'snail' and not puzzle.is_snail_solvable()) or (_type == 'row' and not puzzle.is_row_solvable()):
      print(f"Puzzle is not {_type} solvable, exiting.")
      return

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
    if demo:
      time.sleep(1)
      os.system("clear")
    print(f"\nState {stateId}:")
    print_state(path, puzzle.size)
    stateId += 1
