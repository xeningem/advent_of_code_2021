from collections import Counter

def calc(l):
    val_size = len(l[0])
    counters = [Counter() for x in range(val_size)]
    for x in l:
        for i, v in enumerate(x):
            counters[i].update(v)
    gamma_str = ''.join([x.most_common(1)[0][0] for x in counters])
    delta_str = ''.join(['0' if x =='1' else '1' for x  in gamma_str])

    print(f'{gamma_str=}, {delta_str=}')
    gamma, delta = int(gamma_str, 2), int(delta_str, 2)
    return gamma, delta, gamma*delta


def filter_by_most_common_bit(l, bit_number, check_most, default):
    if len(l) == 1:
        return l
    counter = Counter()
    for x in l:
        counter.update(x[bit_number])

    most_commons = counter.most_common(2)
    filter_bit = most_commons[0][0]
    if len(most_commons) == 2:
        if not check_most:
            filter_bit = most_commons[1][0]

        if most_commons[0][1] == most_commons[1][1]:
            filter_bit = default

    return [x for x in l if x[bit_number] == filter_bit]


def filter_list_by_bit(filtered_s, check_most):
    default = '1' if check_most else '0'
    for i in range(len(filtered_s[0])):
        filtered_s = filter_by_most_common_bit(filtered_s, i, check_most, default)

    return filtered_s



def main():
    s = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    print(calc(s))
    o2_str = filter_list_by_bit(s, True)[0]
    co2_str = filter_list_by_bit(s, False)[0]

    print(f'{o2_str=}, {co2_str=}')
    o2, co2 = int(o2_str, 2), int(co2_str, 2)
    print(f'{o2=} * {co2=} = {o2 * co2} ')

    with open("input_3.txt") as f:
        l = f.readlines()
        d = calc([x.strip() for x in l])
        print(d)

        o2_str = filter_list_by_bit(l, True)[0]
        co2_str = filter_list_by_bit(l, False)[0]

        print(f'{o2_str=}, {co2_str=}')
        o2, co2 = int(o2_str, 2), int(co2_str, 2)
        print(f'{o2=} * {co2=} = {o2*co2} ')
        #
        # d1, d2, d3 = get_depth_and_distance_adv(l)
        # print(d1, d2, d1 * d2)


if __name__ == '__main__':
    main()