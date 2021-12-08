import itertools


perms = sorted(_ for _ in set(itertools.permutations("abcdefg")))
mappings = [{p: l for p, l in zip(perm, "abcdefg")} for perm in perms]


def get_input():
    with open('day08.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_val(wiring_map, digit_code):
    # Use the encoding given in the problem description as the "correct" encoding.
    # The mapping maps the scrambled letters to the correct ones.
    lit = "".join(sorted([wiring_map[s] for s in digit_code]))
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
    return None


def is_mapping_valid(wiring_map, codes):
    for code in codes:
        if get_val(wiring_map, code) is None:
            return False
    return True


def crack(signal, code):
    signal = signal + code

    wiring_map = None
    for mapping in mappings:
        if is_mapping_valid(mapping, signal):
            assert wiring_map is None  # Catch if there is more than 1 valid mapping.
            wiring_map = mapping

    value = int("".join([str(get_val(wiring_map, digit)) for digit in code]))

    return wiring_map, value


def day8a():
    print("    Part A")
    data = get_input()
    codes = [line.split("| ")[1] for line in data]
    codes = [line.split(" ") for line in codes]
    agg = 0
    for code in codes:
        filtered_digits = [d for d in code if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7]
        agg += len(filtered_digits)
    print(agg)
    assert agg == 525
    return agg


def day8b():
    print("\n    Part B")
    data = get_input()
    lines = [line.split(" | ") for line in data]
    signals = [signal.split(" ") for signal, _ in lines]
    codes = [code.split(" ") for _, code in lines]

    agg = 0
    for signal, code in zip(signals, codes):
        agg += crack(signal, code)[1]

    print(agg)
    assert agg == 1083859
    return agg


if __name__ == '__main__':
    day8a()
    day8b()
