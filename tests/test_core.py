from core.puzzle import find_coordinates
from core.npuzzle_gen import generate_puzzle_tab
from core.puzzle import Puzzle, print_state

def test_find_coordinates(n_iter):
  for _ in range(n_iter):
    puzzle = Puzzle(generate_puzzle_tab(True, 3, 1000, None))
    print_state(puzzle.state, puzzle.size)
    print(find_coordinates(puzzle.state, puzzle.size, 0))
