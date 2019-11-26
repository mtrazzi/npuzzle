#!/usr/bin/env python

import sys
import argparse
import random
import numpy as np

from npuzzle_gen import generate_puzzle_tab, make_goal

class Puzzle(object):
    def __init__(self, puzzle):
       self.puzzle_list = puzzle
       self.size = int(np.sqrt(len(puzzle)))
       self.goal = make_goal(self.size)
    def next_state(self, move):
        """next state given a certain move (e.g. UP, MOVE, LEFT, RIGHT)"""
        return
    def is_solved(self):
        return self.puzzle_list == self.goal
    def print_state(self):
        s = self.size
        print("%d" % s)
        for y in range(s):
            for x in range(s):
                print("%s" % (str(self.puzzle_list[x + y*s]).ljust(s + 1)), end='')
            print()

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