import math
from collections import defaultdict, Counter
from dataclasses import dataclass, field

test_input = '16,1,2,0,4,2,7,1,2,14'

# @dataclass
# class Board:
#     places
#     links


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_list(cls, params):
        params = list(map(int, params))
        return Point(params[0], params[1])


#  function line(int x0, int x1, int y0, int y1)
#      int deltax := abs(x1 - x0)
#      int deltay := abs(y1 - y0)
#      int error := 0
#      int deltaerr := (deltay + 1)
#      int y := y0
#      int diry := y1 - y0
#      if diry > 0
#          diry = 1
#      if diry < 0
#          diry = -1
#      for x from x0 to x1
#          plot(x,y)
#          error := error + deltaerr
#          if error >= (deltax + 1)
#              y := y + diry
#              error := error - (deltax + 1)

@dataclass
class Link:
    src: Point
    dst: Point

    @classmethod
    def from_list(cls, params):
        return Link(params[0], params[1])

@dataclass
class Board:
    points: defaultdict = None

    def __init__(self):
        self.points = defaultdict(int)

    def plot(self, x, y):
        self.points[(x, y)] += 1

    def apply_link(self, link: Link):

        x0, y0, x1, y1 = link.src.x, link.src.y, link.dst.x, link.dst.y

        if x0 > x1:
            x0, y0, x1, y1 = x1, y1, x0, y0

        delta_x = abs(x0 - x1)
        delta_y = abs(y0 - y1)


        if x0 != x1 and y0 != y1 and delta_x != delta_y:
            print(f"Broken link? {link=}")
            return

        error = 0
        deltaerr = (delta_y + 1)
        diry = y1 - y0
        if diry > 0:
            diry = 1
        if diry < 0:
            diry = -1
        dx = 1 if x1 >= x0 else -1
        xstart, xstop = min(x0, x1), max(x0, x1)
        ystart, ystop = min(y0, y1), max(y0, y1)

        if x0 == x1:
            for y in range(ystart, ystop+1):
                self.plot(x0, y)
        elif y0 == y1:
            for x in range(xstart, xstop+1):
                self.plot(x, y0)
        elif delta_x == delta_y:
            y = y0
            for x in range(x0, x1+1):
                self.plot(x, y)
                y = y + diry








def parse_line(line):
    coords = Link.from_list([Point.from_list(x.split(',')) for x in line.split(' -> ')])
    return coords

def parse_input(data):
    return list(map(int, data.split(',')))

def v1_cost(x):
    return x

def v2_cost(x):
    return x * (x+1) //2


def find_fuel_to_target(positions, target, cost_function):
    return sum([cost_function(abs(target - x)) for x in positions])


def find_fuel_to_target_v2(positions, target):
    return sum([v2_cost(abs(target - x)) for x in positions])

def find_minimum_target(positions, cost_function):
    def get_cost(value):
        return sum([cost_function(abs(value - x)) for x in positions])
    start, stop = min(positions), max(positions)
    mid = (start + stop) // 2

    rstart, rmid, rstop = get_cost(start), get_cost(mid), get_cost(stop)

    while start < mid < stop:
        if rstart < rmid:
            stop = mid
            mid = (start+stop)//2
            rmid, rstop = get_cost(mid), get_cost(stop)
        else:
            start = mid
            mid = (start+stop)//2
            rstart, rmid = get_cost(start), get_cost(mid)
    print(start, stop, mid)
    return mid

def run_test(data):
    positions = parse_input(data)
    positions.sort()
    median = positions[len(positions)//2]


    around_avg_fuels = [(find_fuel_to_target(positions, median+x, v1_cost), median+x) for x in range(-2, 2)]
    target = min(around_avg_fuels)[1]

    print(find_fuel_to_target(positions, target, v1_cost))
    c = Counter(positions)
    new_target = c.most_common(1)[0][0]
    print(new_target)
    target = find_minimum_target(positions, v2_cost)
    print('target==', target)


    print(around_avg_fuels)
    print(min(around_avg_fuels))


    print('find_fuel_to_target_v2', target,  find_fuel_to_target_v2(positions, target))

#     96592275
#     96592275


def main():
    run_test(test_input)
    with open("input_07.txt") as f:
        run_test(f.read())

if __name__ == "__main__":
    main()
