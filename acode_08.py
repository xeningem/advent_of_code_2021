import math
from collections import defaultdict, Counter
from dataclasses import dataclass, field

test_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''


def parse_input(data):
    return [[x.split(' ') for x in line.split(' | ')] for line in data.split('\n') if line]



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

#      0:      1:      2:      3:      4:
#      aaaa    ....    aaaa    aaaa    ....
#     b    c  .    c  .    c  .    c  b    c
#     b    c  .    c  .    c  .    c  b    c
#      ....    ....    dddd    dddd    dddd
#     e    f  .    f  e    .  .    f  .    f
#     e    f  .    f  e    .  .    f  .    f
#      gggg    ....    gggg    gggg    ....
#
#       5:      6:      7:      8:      9:
#      aaaa    aaaa    aaaa    aaaa    aaaa
#     b    .  b    .  .    c  b    c  b    c
#     b    .  b    .  .    c  b    c  b    c
#      dddd    dddd    ....    dddd    dddd
#     .    f  e    f  .    f  e    f  .    f
#     .    f  e    f  .    f  e    f  .    f
#      gggg    gggg    ....    gggg    gggg
#    a +
#    b
#    c +
#    d +
#    e +
#    f +
#    g +


def deduce_numbers(case):
    simple_numbers_segments_count = {1: 2, 4: 4, 7: 3, 8: 7}
    reversed_len = {v:k for k,v in simple_numbers_segments_count.items()}
    standart_mapping = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bdcf', 5: 'abdfg', 6: 'abdefg',
                        7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}

    segments_to_number = {''.join(sorted(v)):k for k,v in standart_mapping.items()}
    c = [set(x) for x in case[0]]

    original = {}

    simple_case = {reversed_len[len(w)]:set(w) for w in c if len(w) in reversed_len}
    original['a'] = set(simple_case[7]) - set(simple_case[1])

    case_6_9 = [w for w in c if len(w) == 6 and w > (simple_case[4] - simple_case[1])]
    assert(len(case_6_9) == 2)
    case_6_9_check = {x > simple_case[1]:x for x in case_6_9 for i in range(2)}
    case_9 = case_6_9_check[True]
    case_6 = case_6_9_check[False]

    original['c'] = case_9 - case_6
    original['e'] = case_6 - case_9
    original['f'] = simple_case[1] - original['c']

    case_0 = [w for w in c if len(w) == 6 and not w > (simple_case[4] - simple_case[1])][0]
    original['d'] = simple_case[8] - case_0
    original['g'] = case_9 - simple_case[4] - original['a']
    original['b'] = case_0 - simple_case[7] - original['g'] - original['e']

    # print(f'{len(original)=} {original}, {case_0=}, ')

    original = {k:list(v)[0] for k,v in original.items()}
    translate_segments = {v:k for k,v in original.items()}

    answer_words = [''.join(sorted([translate_segments[ch] for ch in w])) for w in case[1]]
    # print(f'{answer_words=}')
    try:
        qqq = [str(segments_to_number[k]) for k in answer_words]
        print(f'{qqq=}')
        return int(''.join(qqq))
    except Exception as e:
        print(f"error with {answer_words=}, {case=} {e=}")
        return 0








def run_test(data):
    simple_numbers_segments_count = {1: 2, 4: 4, 7: 3, 9: 7}
    simple_cases = set(simple_numbers_segments_count.values())
    words = parse_input(data)

    # print(words)
    count_simple_numbers = sum([len(w) in simple_cases for case in words for w in case[1]])
    print(f'{count_simple_numbers=}')

    deduce_result = deduce_numbers([['cfgeda', 'afcbg', 'fbcdaeg', 'gbdfa', 'fdgcba', 'cbdf', 'becga', 'cf', 'gcf', 'gbdefa'], ['bfcd', 'acgdfe', 'cfabg', 'dcbf']])
    print(f"{deduce_result=}")

    result_2 = sum(map(deduce_numbers, words))
    print(f'{result_2=}')



#     96592275
#     96592275


def main():
    run_test(test_input)
    with open("input_08.txt") as f:
        run_test(f.read())

if __name__ == "__main__":
    main()
