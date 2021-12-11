from collections import defaultdict
from dataclasses import dataclass, field

test_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''

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
    lines = data.split('\n')
    links = [parse_line(l) for l in lines if l]
    return links

def run_test(data):
    links = parse_input(data)
    board = Board()
    for link in links:
        board.apply_link(link)
    print(sum([1 for x in board.points.values() if x >= 2]))

def main():
    run_test(test_input)
    with open("input_05.txt") as f:
        run_test(f.read())

if __name__ == "__main__":
    main()
