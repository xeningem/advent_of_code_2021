import math
from collections import defaultdict, Counter, deque
from dataclasses import dataclass, field
from functools import reduce

test_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''


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
    return [line for line in data.split('\n') if line]


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

def run_test(data):
    lines = parse_input(data)
    result = 0
    autocomplete_score_list = []
    for l in lines:
        incorrect_cost = bracket_cost(find_first_incorrect(l))
        result += incorrect_cost
        if not incorrect_cost:
            auto_completed = find_autocomplete(l)
            autocomplete_score_list.append(calc_autocomplete_cost(auto_completed))
    autocomplete_score_list.sort()
    mid_idx = len(autocomplete_score_list)//2
    print(result, autocomplete_score_list[mid_idx-1:mid_idx+2])



#     96592275
#     96592275


def main():
    run_test(test_input)
    with open("input_10.txt") as f:
        run_test(f.read())

if __name__ == "__main__":
    main()
