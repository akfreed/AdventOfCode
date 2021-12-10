def get_input_a():
    with open('day10.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_input_b():
    return get_input_a()


def check_line(line):
    stack = []
    for char in line:
        if char == '(' or char == '{' or char == '[' or char == '<':
            stack.insert(0, char)
        elif char == ')':
            if stack[0] != '(':
                return 3
            stack.pop(0)
        elif char == ']':
            if stack[0] != '[':
                return 57
            stack.pop(0)
        elif char == '}':
            if stack[0] != '{':
                return 1197
            stack.pop(0)
        elif char == '>':
            if stack[0] != '<':
                return 25137
            stack.pop(0)
    #assert len(stack) == 0
    return 0


def check_line2(line):
    stack = []
    for char in line:
        if char == '(' or char == '{' or char == '[' or char == '<':
            stack.insert(0, char)
        elif char == ')':
            if stack[0] != '(':
                return 0
            stack.pop(0)
        elif char == ']':
            if stack[0] != '[':
                return 0
            stack.pop(0)
        elif char == '}':
            if stack[0] != '{':
                return 0
            stack.pop(0)
        elif char == '>':
            if stack[0] != '<':
                return 0
            stack.pop(0)

    pts = 0
    ret = ''
    for char in stack:
        pts *= 5
        if char == '(':
            pts += 1
            ret += ')'
        if char == '[':
            pts += 2
            ret += ']'
        if char == '{':
            pts += 3
            ret += '}'
        if char == '<':
            pts += 4
            ret += '}'

    return pts


def day10a():
    print("    Part A")
    lines = get_input_a()
    agg = 0
    for line in lines:
        agg += check_line(line)
    print(agg)


def day10b():
    print("\n    Part B")
    lines = get_input_b()
    #lines = [line for line in lines if check_line(line) == 0]
    scores = sorted([check_line2(line) for line in lines if check_line2(line) != 0])
    print(scores[len(scores)//2])



if __name__ == '__main__':
    #day10a()
    day10b()
