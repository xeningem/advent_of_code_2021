import copy
import math
from collections import defaultdict, Counter, deque
from dataclasses import dataclass, field
from functools import reduce

test_input = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''


mini_test = '''
11111
19991
19191
19991
11111'''


def find_first_incorrect(line):
    l = []

    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for i, ch in enumerate(line):
        if ch in brackets:
            l.append(ch)
        else:
            last_bracket = l[-1]
            if ch == brackets[last_bracket]:
                l.pop(-1)
            else:
                return l, ch
    return None, None


def find_autocomplete(line):
    l = []

    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for i, ch in enumerate(line):
        if ch in brackets:
            l.append(ch)
        else:
            last_bracket = l[-1]
            if ch == brackets[last_bracket]:
                l.pop(-1)
            else:
                return []
    if l:
        return [brackets[x] for x in l[::-1]]
    return []

def parse_input(data):
    return [[int(x) for x in line] for line in data.split('\n') if line]


bracket_points = {')': 3, ']': 57, '}': 1197, '>': 25137}

autocomplete_bracket_points = {")": 1, "]": 2, "}": 3, ">": 4,}

def bracket_cost(bracket_info):
    return bracket_points.get(bracket_info[1], 0)

def calc_autocomplete_cost(brackets):
    score = 0
    for ch in brackets:
        score *= 5
        score += autocomplete_bracket_points[ch]
    return score

def dump_levels(iteration, levels, flash_count=0):
    s = '\n'.join([''.join(map(str, line)) for line in levels])
    s = s.replace('0', '_')
    print(f'{iteration=},{flash_count=}\n', s, '\n', sep='')


def run_step(l):
    flash_list = set()
    m = len(l)
    n = len(l[0])
    flash_count = 0

    flashes_set = set()
    flashes = deque()
    for i in range(m):
        for j in range(n):
            l[i][j] += 1
            if l[i][j] == 10:
                flash_count += 1
                flashes.append((i, j))
                flashes_set.add((i, j))

    while flashes:
        (fi, fj) = flashes.popleft()
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                i, j = fi + di, fj + dj
                if 0 <= i < n and 0 <= j < m:
                    l[i][j] += 1
                    if l[i][j] == 10:
                        flash_count += 1

                        if (i, j) not in flashes_set:
                            flashes.append((i, j))
                            flashes_set.add((i, j))

    for (i, j) in list(flashes_set):
        l[i][j] = 0
    return len(flashes_set)



def run_test(data):
    levels = parse_input(data)
    print('Data loaded')
    dump_levels(0, levels, 0)
    m = len(levels)
    n = len(levels[0])

    flash_count = 0
    first_full_flash_step = 0
    for i in range(1, 10000):
        flash_diff = run_step(levels)
        flash_count += flash_diff
        # dump_levels(i, levels, flash_count)
        if i == 100:
            print(f'{i=}, {flash_count=}')
        if flash_diff == m*n:
            print('RESULT', i)
            break







#     96592275
#     96592275


def main():
    run_test(mini_test)

    run_test(test_input)
    with open("input_11.txt") as f:
        run_test(f.read())

if __name__ == "__main__":
    main()
