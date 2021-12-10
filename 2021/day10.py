def get_input():
    with open('day10.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def score_line(line):
    """Return the score as a negative if the line is corrupted. Return a positive score if incomplete. 0 otherwise."""
    stack = []
    for char in line:
        if char == '(' or char == '{' or char == '[' or char == '<':
            stack.append(char)
        else:
            if char == ')':
                if stack[-1] != '(':
                    return -3
            elif char == ']':
                if stack[-1] != '[':
                    return -57
            elif char == '}':
                if stack[-1] != '{':
                    return -1197
            elif char == '>':
                if stack[-1] != '<':
                    return -25137
            else:
                assert False
            stack.pop()

    points = 0
    for char in reversed(stack):
        points *= 5
        if char == '(':
            points += 1
        elif char == '[':
            points += 2
        elif char == '{':
            points += 3
        elif char == '<':
            points += 4
        else:
            assert False
    return points


def day10a():
    print("    Part A")
    lines = get_input()
    scores = [score_line(line) for line in lines]
    score = sum([-score for score in scores if score < 0])
    print(score)
    assert score == 288291
    return score


def day10b():
    print("\n    Part B")
    lines = get_input()
    scores = [score_line(line) for line in lines]
    scores = sorted([score for score in scores if score > 0])
    median = scores[len(scores) // 2]
    print(median)
    assert median == 820045242
    return median


if __name__ == '__main__':
    day10a()
    day10b()
