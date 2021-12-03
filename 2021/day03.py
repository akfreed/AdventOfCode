
def get_input():
    with open('day03.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_gamma_epsilon(nums, is_part_b: bool = False):
    gamma = ""
    epsilon = ""
    count = 0
    for idx in range(len(nums[0])):
        for num in nums:
            if num[idx] == "1":
                count += 1
            else:
                count -= 1
        if count > 0:
            gamma += "1"
            epsilon += "0"
        elif count < 0:
            gamma += "0"
            epsilon += "1"
        else:
            assert is_part_b  # Part A makes no mention of how to handle ambiguity. If it happens, it's an error.
            gamma += "1"
            epsilon += "0"
        count = 0

    return gamma, epsilon


def day3a():
    print("    Part A")
    nums = get_input()
    gamma, epsilon = get_gamma_epsilon(nums)

    print(f"gamma: {gamma}, ({int(gamma, 2)})")
    print(f"epsilon: {epsilon}, ({int(epsilon, 2)})")
    print(f"result: {int(gamma, 2) * int(epsilon, 2)}")


def day3b():
    print("\n    Part B")
    nums = get_input()

    reduction = nums[:]
    for idx in range(len(nums[0])):
        gamma, _ = get_gamma_epsilon(reduction, is_part_b=True)
        reduction = [n for n in reduction if n[idx] == gamma[idx]]
        if len(reduction) == 1:
            break

    assert len(reduction) == 1
    oxy_gen_rating = reduction[0]

    reduction = nums[:]
    for idx in range(len(nums[0])):
        _, epsilon = get_gamma_epsilon(reduction, is_part_b=True)
        reduction = [n for n in reduction if n[idx] == epsilon[idx]]
        if len(reduction) == 1:
            break

    assert len(reduction) == 1
    co2_scrub_rating = reduction[0]

    print(f"oxygen generator rating: {oxy_gen_rating}, ({int(oxy_gen_rating, 2)})")
    print(f"CO2 scrubber rating: {co2_scrub_rating}, ({int(co2_scrub_rating, 2)})")
    print(f"result: {int(oxy_gen_rating, 2) * int(co2_scrub_rating, 2)}")


if __name__ == '__main__':
    day3a()
    day3b()
