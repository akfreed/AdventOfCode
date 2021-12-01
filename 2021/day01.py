
def getInput():
    with open('day01.txt', 'r') as file:
        return [int(n) for n in file.readlines()]


def day1a():
    print("Part A")
    count = 0
    distances = getInput()
    for i in range(1, len(distances)):
        if distances[i] - distances[i - 1] > 0:
            count += 1
    print(count)


def window_sum(distances, i):
    a = sum(distances[i:i+3])
    #print(a)
    return a

def day1b():
    print("Part B")
    agg = 0
    distances = getInput()
    for i in range(1, len(distances)):
        if window_sum(distances, i) - window_sum(distances, i - 1) > 0:
            agg += 1
    print(agg)


if __name__ == '__main__':
    day1a()
    day1b()
