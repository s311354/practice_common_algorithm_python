#!/usr/bin/env python3
import sys


# DFS 
def backtrack_compact(working_set, k, n):
    """docstring for backtrack_compact"""
#     global solutions

#     print(working_set)
    if k == n:
        s = {k for k in working_set if working_set[k] == 1}
#         print(k, working_set[k], s)
        solutions.append(s)
    else:
        k += 1
        for i in [0, 1]:
            working_set[k] = i
            backtrack_compact(working_set, k, n)


def main():
    """docstring for main"""
    if 0 < 1 < len(sys.argv):
        n = int(sys.argv[1])
    else:
        exit("Usage: subsets.py number")

    global solutions
    solutions = []

    backtrack_compact({}, 0, n)
    print(solutions)
    print("Number of subsets: {}".format(len(solutions)))


if __name__ == '__main__':
    main()
