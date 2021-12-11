s = [
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2",
]

def get_depth_and_distance(l):
    depth = 0
    distance = 0

    for p in l:
        command, value = p.split(' ')
        value = int(value)

        if command == "forward":
            distance += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value
    return depth, distance

def get_depth_and_distance_adv(l):
    depth = 0
    distance = 0
    aim = 0

    for p in l:
        command, value = p.split(' ')
        value = int(value)

        if command == "forward":
            distance += value
            depth += aim * value
        elif command == "up":
            aim -= value
            # depth -= value
        elif command == "down":
            aim += value
            # depth += value
        # print(f'{p=}, {depth=}, {distance=}, {aim=}')
    return depth, distance, aim



def main():
    print(get_depth_and_distance_adv(s))

    with open("input2.txt") as f:
        l = f.readlines()
        d1, d2 = get_depth_and_distance(l)
        print(d1, d2, d1*d2)

        d1, d2, d3 = get_depth_and_distance_adv(l)
        print(d1, d2, d1*d2)

if __name__ == "__main__":
    main()