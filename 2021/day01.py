
def get_input():
    with open('day01.txt', 'r') as file:
        return [int(n) for n in file.readlines()]


def day1a():
    print("Part A")
    count = 0
    distances = get_input()
    for i in range(1, len(distances)):
        if distances[i] - distances[i - 1] > 0:
            count += 1
    print(count)


def day1b():
    print("Part B")
    count = 0
    distances = get_input()
    for i in range(1, len(distances)):
        if sum(distances[i:i+3]) - sum(distances[i-1:i+2]) > 0:
            count += 1
    print(count)


if __name__ == '__main__':
    day1a()
    day1b()
