# 42 Project: N-Puzzle

About
-----
>We had to create a program capable of solving [15-puzzles](https://en.wikipedia.org/wiki/15_puzzle) of various sizes in the smallest amount of moves using A*.

Implemented Algorithms
----------------------
- [A* search](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)

Installation
------------
```bash
$make install
```

Usage
-----
```bash
$python3 npuzzle.py
```

Additional Arguments
--------------------

```bash
  -h: show this help message and exit
  --size SIZE: Size of the puzzle's side. Must be >3.
  -s: Forces generation of a solvable puzzle. Overrides -u.
  -u: Forces generation of an unsolvable puzzle.
  -i: Enable interactive mode. Overrides --size -f.
  -n ITERATIONS: Number of passes.
  -f FILENAME: Generate puzzle from file. Overrides --size.
  -t {snail,row}: NPuzzle type.
  -a {A*,BFS}: Algorithm used for search.
  --heuristic {euclidean, manhattan, tiles-out, uniform-cost}: Heuristic function
  -d: Print every step to the solution.
```

### Example

`$python3 npuzzle.py --size 3 -s`

```bash
Initial State:
2 8 4
5 0 6
1 3 7
Starting Search...

Total number of states ever selected in the openSet (Complexity in time): 2302
Maximum number of states ever represented in memory at the same time during the search (Complexity in size): 933


Number of moves required: 22

State 0:
2 8 4
5 0 6
1 3 7

[...]

State 22:
1 2 3
8 0 4
7 6 5
```

## Authors

Michaël Trazzi – [@MichaelTrazzi](https://twitter.com/michaeltrazzi) – mtrazzi@student.42.fr

Kevin Costa – [@kcosta42](https://github.com/kcosta42) – kcosta@student.42.fr

## License

Distributed under the MIT license. See ``LICENSE`` for more information.

## Context

This project took roughly 3 days in December 2019 as a coding project for the Algorithmic/AI branch of [42](https://www.42.us.org/).
