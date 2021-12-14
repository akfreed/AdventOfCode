def get_input_a():
    with open('day14.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    template = lines[0]
    lines = lines[2:]
    rules = {}
    for line in lines:
        s = line.split(' -> ')
        rules[s[0]] = s[1]
    return template, rules


def get_input_b():
    return get_input_a()


def expand(template, rules):
    ps = []
    for i in range(1, len(template)):
        x = template[-i - 1]
        y = template[-i]
        ps = [rules[x + y]] + ps

    asdf = ""
    for i, c in enumerate(ps):
        asdf += template[i]
        asdf += c
    asdf += template[-1]

    return asdf



def day14a():
    print("    Part A")
    template, rules = get_input_a()
    for i in range(10):
        template = expand(template, rules)
    ms = {c: template.count(c) for c in "ONSVVHNCFVBHKVPCHCPV"}
    print(max(ms.values()) - min(ms.values()))
    print(ms)
    # not 2107



def day14b():
    print("\n    Part B")
    template, rules = get_input_a()

    superrules = {}
    for key in rules:
        val = key
        for i in range(10):
            val = expand(val, rules)
        superrules[key] = val[1:-1]

    sdrules = {}
    for key in superrules:
        val = key
        for i in range(2):
            val = expand(val, superrules)
        sdrules[key] = val[1:-1]

    s = set()
    for char in rules.values():
        s.add(char)
    s = sorted(list(s))
    print(s)

    sdcount = {}
    for key in sdrules:
        sdcount[key] = {c: sdrules[key].count(c) for c in s}

    template = expand(template, sdrules)


    master_count = {c: 0 for c in s}
    last = None
    for i in range(len(template) - 1):
        x = template[i]
        y = template[i + 1]
        for key in sdcount[x + y]:
            master_count[key] += sdcount[x + y][key]
        master_count[x] += 1
        last = y
    master_count[last] += 1

    print(master_count)
    # 3459174981022 is too high

    print(max(master_count.values()) - min(master_count.values()))


if __name__ == '__main__':
    day14a()
    day14b()
