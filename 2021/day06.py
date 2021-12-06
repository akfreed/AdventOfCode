
def get_input():
    with open('day06.txt', 'r') as file:
        return [int(n) for n in file.readline().strip().split(',')]


def run_fish(fish_list, num_generations):
    adult_fish = {i: sum(map(lambda n: 1 if n == i else 0, fish_list)) for i in range(7)}
    baby_fish = {i: 0 for i in range(7)}

    for i in range(num_generations):
        day = i % 7
        baby_fish[(day + 2) % 7] = adult_fish[day]
        adult_fish[day] += baby_fish[day]
        baby_fish[day] = 0

    return sum(adult_fish.values()) + sum(baby_fish.values())


def day6a():
    print("    Part A")
    fish_list = get_input()
    num = run_fish(fish_list, 80)
    print(num)
    assert num == 352872


def day6b():
    print("\n    Part B")
    fish_list = get_input()
    num = run_fish(fish_list, 256)
    print(num)
    assert num == 1604361182149


if __name__ == '__main__':
    day6a()
    day6b()
