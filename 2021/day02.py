def get_input():
    with open('day02.txt', 'r') as file:
        commands = [line.strip().split(' ', 1) for line in file.readlines()]
        return [(operation, int(amount)) for operation, amount in commands]


def day2a():
    print("    Part A")
    commands = get_input()
    horizontal = 0
    depth = 0
    for operation, amount in commands:
        if operation == "forward":
            horizontal += amount
        elif operation == "up":
            depth -= amount
            assert depth >= 0
        elif operation == "down":
            depth += amount
        else:
            assert False

    print(f"Final Depth: {depth}")
    print(f"Final Horizontal: {horizontal}")
    print(f"Horizontal * Depth: {depth * horizontal}")
    return depth * horizontal


def day2b():
    print("\n    Part B")
    commands = get_input()
    horizontal = 0
    depth = 0
    aim = 0
    for operation, amount in commands:
        if operation == "forward":
            horizontal += amount
            depth += aim * amount
            assert depth >= 0
        elif operation == "up":
            aim -= amount
            assert depth >= 0
        elif operation == "down":
            aim += amount
        else:
            assert False

    print(f"Final Depth: {depth}")
    print(f"Final Horizontal: {horizontal}")
    print(f"Horizontal * Depth: {depth * horizontal}")
    return depth * horizontal


if __name__ == '__main__':
    day2a()
    day2b()
