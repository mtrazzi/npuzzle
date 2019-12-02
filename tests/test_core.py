import os

from core.core import Solve

def test_error():
  for file in os.listdir("./puzzles/errors"):
    print(f"Test for file {file}:")
    filename = os.path.join("./puzzles/errors", file)
    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=True, size=3,
          iterations=1, interactive=False, filename=filename)
