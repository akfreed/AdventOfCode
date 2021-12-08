import itertools


perms = sorted(_ for _ in set(itertools.permutations("abcdefg")))
mappings = [{p: l for p, l in zip(perm, "abcdefg")} for perm in perms]


def get_input_a():
    with open('day08.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_input_b():
    return get_input_a()


def day8a():
    print("    Part A")
    data = get_input_a()
    codes = [line.split("| ")[1] for line in data]
    codes = [line.split(" ") for line in codes]
    agg = 0
    for i in range(len(codes)):
        codes[i] = [c for c in codes[i] if len(c) == 2 or len(c) == 3 or len(c) == 4 or len(c) == 7]
        agg += len(codes[i])
    print(agg)

    sums = sum([sum([len(c) for c in code]) for code in codes])
    print(sums)
    assert agg == 525


class Digit:
    def __init__(self):
        self.display = {l: False for l in "abcdefg"}
        self.mapping = {l: l for l in "abcdefg"}

    def reset_display(self):
        self.display = {l: False for l in "abcdefg"}

    def light_display(self, sig):
        for s in sig:
            self.display[self.mapping[s]] = True

    def is_valid(self, signal):
        for s in signal:
            self.reset_display()
            self.light_display(s)
            lit = "".join(sorted([k for k in self.display if self.display[k] == True]))
            if lit == "abcefg" or \
                    lit == "cf" or \
                    lit == "acdeg" or \
                    lit == "acdfg" or \
                    lit == "bcdf" or \
                    lit == "abdfg" or \
                    lit == "abdefg" or \
                    lit == "acf" or \
                    lit == "abcdefg" or \
                    lit == "abcdfg":
                pass
            else:
                return False
        return True

    def get_val(self, c):
        self.reset_display()
        self.light_display(c)
        lit = "".join(sorted([k for k in self.display if self.display[k] == True]))
        if lit == "abcefg":
            return 0
        if lit == "cf":
            return 1
        if lit == "acdeg":
            return 2
        if lit == "acdfg":
            return 3
        if lit == "bcdf":
            return 4
        if lit == "abdfg":
            return 5
        if lit == "abdefg":
            return 6
        if lit == "acf":
            return 7
        if lit == "abcdefg":
            return 8
        if lit == "abcdfg":
            return 9
        assert False


def crack(signal, code):
    both = signal + code
    # sure_mappings = {}
    # for b in both:
    #     n = sorted(b)
    #     # 1
    #     if len(n) == 2:
    #         sure_mappings[n[0]] = "c"
    #         sure_mappings[n[1]] = "f"
    d = Digit()

    for mapping in mappings:
        d.mapping = mapping
        if d.is_valid(both):
            break

    agg = ""
    for i, c in enumerate(code):
        agg += str(d.get_val(c))

    return int(agg)


def day8b():
    print("\n    Part B")
    data = get_input_b()
    lines = [line.split(" | ") for line in data]
    signals = [signal.split(" ") for signal, _ in lines]
    codes = [code.split(" ") for _, code in lines]
    agg = 0
    for signal, code in zip(signals, codes):
        value = crack(signal, code)
        agg += value
    print(agg)
    assert agg == 1083859



if __name__ == '__main__':
    day8a()
    day8b()
    #not 3850
