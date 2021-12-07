
def get_input_a():
    with open('day07.txt', 'r') as file:
        return [int(n) for n in file.readline().strip().split(',')]


def get_input_b():
    return get_input_a()


def calc_fuel(nums, pos):
    fuel = 0
    for n in nums:
        fuel += abs(n - pos)
    return fuel


def calc_fuel2(nums, pos):
    fuel = 0
    for n in nums:
        steps = abs(n - pos)
        fuel += (steps * (steps + 1)) / 2
    return fuel


def day7a():
    print("    Part A")
    nums = sorted(get_input_a())
    print(len(nums))
    #print(nums[499:501])
    print(nums)
    print(calc_fuel(nums, 499))
    print(calc_fuel(nums, 500))
    min1 = min(nums)
    max1 = max(nums)
    least = 1000000000
    for i in range(min1, max1 + 1):
        if calc_fuel(nums, i) < least:
            least = calc_fuel(nums, i)
            print(i)
    print(least)


def day7b():
    print("\n    Part B")
    nums = get_input_b()
    min1 = min(nums)
    max1 = max(nums)
    least = 1000000000000
    for i in range(min1, max1 + 1):
        if calc_fuel2(nums, i) < least:
            least = calc_fuel2(nums, i)
            print(i)
    print(least)

# not 478567


if __name__ == '__main__':
    day7a()
    day7b()
