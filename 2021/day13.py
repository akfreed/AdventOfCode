from utility import *


def get_input_a():
    with open('day13.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    coords = []
    z = 0
    for i, line in enumerate(lines):
        if line == "":
            z = i
            break
        x, y = line.split(",")
        coords.append(Vector(int(x), int(y)))
    folds = [line.split("fold along ")[1] for line in lines[z+1:]]
    folds = [fold.split('=') for fold in folds]
    folds = [(fold[0], int(fold[1])) for fold in folds]
    return coords, folds


def get_input_b():
    return get_input_a()


def fold_once(dots, fold):
    if fold[0] == 'x':
        for dot in dots:
            if dot.x > fold[1]:
                dot.x -= (dot.x - fold[1]) * 2
    elif fold[0] == 'y':
        for dot in dots:
            if dot.y > fold[1]:
                dot.y -= (dot.y - fold[1]) * 2
    else:
        assert False


def count_dots(dots):
    print(len(dots))
    s = {}
    for dot in dots:
        if dot not in s:
            s[dot] = '##'

    return s


def day13a():
    print("    Part A")
    dots, folds = get_input_a()
    fold_once(dots, folds[0])
    s = count_dots(dots)
    print(len(s))
    # not 748


def day13b():
    print("\n    Part B")
    dots, folds = get_input_a()
    for fold in folds:
        fold_once(dots, fold)

    s = count_dots(dots)
    render_map(s, str, '..')
    pass


if __name__ == '__main__':
    day13a()
    day13b()
