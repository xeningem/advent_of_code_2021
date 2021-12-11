
def count_measumerments(data):
    last_x = data[0]
    count_max = 0
    for x in data[1:]:
        if x > last_x:
            count_max += 1
        last_x = x
    return count_max

def sum3_measure(data):
    window_size = 3

    measures = [sum(data[i: i + window_size]) for i in range(len(data) - window_size + 1)]
    return count_measumerments(measures)

def main():
    with open("acode_input.txt") as f:
        l = [int(x) for x in f.readlines()]
        print(count_measumerments(l))
        print(sum3_measure(l))


if __name__ == "__main__":
    l = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263,]
    # print(count_measumerments(l))
    print(sum3_measure(l))
    main()