def getInputA():
    with open('day02.txt', 'r') as file:
        return [line.strip().split(' ') for line in file.readlines()]


def getInputB():
    return getInputA()


def day2a():
    print("Part A")
    dir = getInputA()
    x = 0
    depth = 0
    for d in dir:
        if d[0] == "forward":
            x += int(d[1])
        elif d[0] == "up":
            depth -= int(d[1])
            assert depth >= 0
        elif d[0] == "down":
            depth += int(d[1])
        else:
            assert False
    print(depth)
    print(x)
    print(x * depth)


def day2b():
    print("Part B")
    dir = getInputA()
    x = 0
    depth = 0
    aim = 0
    for d in dir:
        if d[0] == "forward":
            x += int(d[1])
            depth += aim * int(d[1])
            assert depth >= 0
        elif d[0] == "up":
            aim -= int(d[1])
        elif d[0] == "down":
            aim += int(d[1])
        else:
            assert False
    print(depth)
    print(x)
    print(x * depth)


if __name__ == '__main__':
    day2a()
    day2b()
