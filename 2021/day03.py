
def getInputA():
    with open('day03.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def getInputB():
    return getInputA()


def get_thing(nums):
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
            gamma += "1"
            epsilon += "0"
        count = 0

    return gamma, epsilon


def day3a():
    print("    Part A")
    nums = getInputA()
    gamma, epsilon = get_thing(nums)

    print(gamma)
    print(epsilon)
    #3529
    #566
    #not 1,855,944
    #1, 997, 414


def day3b():
    print("\n    Part B")
    nums = getInputB()

    for idx in range(len(nums[0])):
        gamma, _ = get_thing(nums)
        nums = [n for n in nums if n[idx] == gamma[idx]]
        if len(nums) == 1:
            print(nums)
            break

    if len(nums) != 1:
        print(nums)

    nums = getInputB()
    for idx in range(len(nums[0])):
        _, epsilon = get_thing(nums)
        nums = [n for n in nums if n[idx] == epsilon[idx]]
        if len(nums) == 1:
            print(nums)
            break

    if len(nums) != 1:
        print(nums)

    #3531
    #567
    #not 2,002,077

    #3573
    #289
    #1,032,597


if __name__ == '__main__':
    day3a()
    day3b()
