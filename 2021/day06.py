
def get_input_a():
    with open('day06.txt', 'r') as file:
        return [int(n) for n in file.readline().strip().split(',')]


def get_input_b():
    return get_input_a()


class Fish:
    def __init__(self, n=8):
        self.timer = n

    def update1(self):
        self.timer -= 1

    def update2(self):
        if self.timer == -1:
            self.timer = 6


def day6a():
    print("    Part A")
    fish = get_input_a()
    fish = [Fish(n) for n in fish]

    for i in range(80):
        to_add = []
        for f in fish:
            f.update1()
            if f.timer == -1:
                to_add.append(Fish())
            f.update2()
        fish = fish + to_add
    print(len(fish))


def day6b():
    print("\n    Part B")
    fish = get_input_b()
    fish_map = {}
    fish2 = {}
    for n in range(7):
        fish_map[n] = 0
        fish2[n] = 0
    for n in fish:
        fish_map[n] += 1

    for i in range(258):
        day = i % 7
        fish2[(day + 2) % 7] = fish_map[day]
        fish_map[day] += fish2[day]
        fish2[day] = 0

    print(sum(fish_map.values()))


if __name__ == '__main__':
    day6a()
    day6b()
