def get_input():
    with open('day07.txt', 'r') as file:
        return [int(n) for n in file.readline().strip().split(',')]


def calc_fuel_a(nums, pos):
    return sum(abs(n - pos) for n in nums)


def calc_fuel_b(nums, pos):
    steps = [abs(n - pos) for n in nums]
    return sum([(n * (n + 1)) / 2 for n in steps])


def day7a():
    print("    Part A")
    nums = get_input()

    costs = {calc_fuel_a(nums, i): i for i in range(min(nums), max(nums) + 1)}
    cheapest = min(costs.keys())

    print(f"Cheapest cost: {cheapest}")
    print(f"Index: {costs[cheapest]}")
    assert cheapest == 340987
    return cheapest


def day7b():
    print("\n    Part B")
    nums = get_input()

    costs = {calc_fuel_b(nums, i): i for i in range(min(nums), max(nums) + 1)}
    cheapest = min(costs.keys())

    print(f"Cheapest cost: {cheapest}")
    print(f"Index: {costs[cheapest]}")
    assert cheapest == 96987874
    return cheapest


if __name__ == '__main__':
    day7a()
    day7b()
