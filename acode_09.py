import math
from collections import defaultdict, Counter, deque
from dataclasses import dataclass, field
from functools import reduce

test_input = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''


def parse_input(data):
    return [list(map(int, [ch for ch in line])) for line in data.split('\n') if line]


def get_near(data, i, j):
    val = data[i][j]
    m = len(data)
    n = len(data[1])
    result = []

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < m and 0 <= new_j < n:
            result.append((new_i, new_j))
    return result



def basin_traversal(tubes):
    basins = []
    applied_tubes = set()
    for i, line in enumerate(tubes):
        for j, val in enumerate(line):
            if val < 9 and (i, j) not in applied_tubes:
                curr_basin = {(i, j),}
                q = deque()
                q.append((i, j))
                while q:
                    (new_i, new_j) = q.popleft()
                    applied_tubes.add((new_i, new_j))
                    x = tubes[new_i][new_j]
                    if x < 9:
                        curr_basin.add( (new_i, new_j))
                        near_tubes = get_near(tubes, new_i, new_j)
                        for (x, y) in near_tubes:
                            if (x,y) not in applied_tubes:
                                q.append((x, y))
                basins.append(list(curr_basin))
    top_basins = sorted([len(x) for x in basins])
    print(top_basins[-3:])

    result = reduce((lambda x, y: x * y), top_basins[-3:])
    print(f'{result=}')




def is_lowest_point(data, i, j):
    val = data[i][j]
    m = len(data)
    n = len(data[1])

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < m  and 0 <= new_j < n:
            if data[new_i][new_j] <= val:
                return False

    return True

def calc_risk_level(v):
    return v+1

def run_test(data):
    tubes = parse_input(data)

    results = []
    for i, line in enumerate(tubes):
        for j, val in enumerate(line):
            if is_lowest_point(tubes, i, j):
                results.append(tubes[i][j])
    print(sum(map(calc_risk_level, results)))

    basin_traversal(tubes)




#     96592275
#     96592275


def main():
    run_test(test_input)
    with open("input_09.txt") as f:
        run_test(f.read())

if __name__ == "__main__":
    main()
