from dataclasses import dataclass, field
from typing import Union

test_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

@dataclass
class Board:
    board: list
    marked: set = field(default_factory=set)

    def __repr__(self):
        items = dict(self.__dict__.items())

        board = '\n'.join([' '.join([str(x or '') for x in r]) for r in self.board])
        kws = [f"{key}={value!r}" for key, value in items.items()]
        return f"{type(self).__name__}(board=\n{board}\n, marked={self.marked}"

    def is_win(self):
        for i, r in enumerate(self.board):
            if all([x is None for x in r]):
                return True
        for j in range(5):
            if all([self.board[x][j] is None for x in range(5)]):
                return True

    def sum(self):
        return sum([sum([x for x in l if x] ) for l in self.board])


    def check(self, n: Union[str, int]):
        for i, r in enumerate(self.board):
            for j, x in enumerate(r):
                if x == n:
                    self.board[i][j] = None
                    self.marked.add(int(n))
                    return



def generate_board(board_lines):
    board = [list(map(int, l.split())) for l in board_lines]
    return Board(board)

def parse_input(data):
    lines = data.split('\n')
    bingo_numbers = list(map(int, lines[0].split(',')))

    return bingo_numbers, [generate_board(lines[l:l+5]) for l in range(2, len(lines), 6)]


def run_bingo(data):
    bingo_numbers, boards = parse_input(data)

    win_counts = 0
    for n in bingo_numbers:
        for board in boards:
            if board.is_win():
                continue
            board.check(n)
            if board.is_win():
                if win_counts == 0:
                    print("WIN", board, board.sum()*n)
                win_counts += 1
                if win_counts == len(boards):
                    print("LOOSE", board, board.sum() * n)


def main():
    run_bingo(test_input)
    with open("input_4.txt") as f:
        run_bingo(f.read())

if __name__ == "__main__":
    main()


