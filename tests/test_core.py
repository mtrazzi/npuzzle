import os
import timeit

from core.core import Solve

def test_snail():
  for file in os.listdir("./puzzles/snail"):
    start = timeit.default_timer()

    print(f"Test for file {file}:")
    filename = os.path.join("./puzzles/snail", file)
    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=True, size=3,
          iterations=1, interactive=False, filename=filename)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_row():
  for file in os.listdir("./puzzles/row"):
    start = timeit.default_timer()

    print(f"Test for file {file}:")
    filename = os.path.join("./puzzles/row", file)
    Solve(algorithm='A*', heuristic='euclidean',
          _type='row', solvable=True, size=3,
          iterations=1, interactive=False, filename=filename)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_AStar(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=True, size=3,
          iterations=100, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_BFS(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='BFS', heuristic='euclidean',
          _type='snail', solvable=True, size=3,
          iterations=20, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_euclidean(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=True, size=3,
          iterations=100, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_manhattan(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='manhattan',
          _type='snail', solvable=True, size=3,
          iterations=100, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_tiles_out(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='tiles-out',
          _type='snail', solvable=True, size=3,
          iterations=25, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_uniform_cost(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='uniform-cost',
          _type='snail', solvable=True, size=3,
          iterations=10, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_size4(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=True, size=4,
          iterations=25, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_size5(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=True, size=5,
          iterations=10, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_unsolvable_snail(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='euclidean',
          _type='snail', solvable=False, size=3,
          iterations=100, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")

def test_unsolvable_row(n_iter):
  for _ in range(n_iter):
    start = timeit.default_timer()

    Solve(algorithm='A*', heuristic='euclidean',
          _type='row', solvable=False, size=3,
          iterations=100, interactive=False, filename=None)
    print(f"Time to execute: {timeit.default_timer() - start}\n")
