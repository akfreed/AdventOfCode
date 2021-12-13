from utility import Vector, render_map


def get_input():
    with open('day13.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    # Read dot coordinates.
    coords = []
    fold_instructions_idx = 0
    for i, line in enumerate(lines):
        if line == "":
            fold_instructions_idx = i + 1
            break
        x, y = line.split(",")
        coords.append(Vector(int(x), int(y)))

    folds = [line.split("fold along ")[1] for line in lines[fold_instructions_idx:]]
    folds = [fold.split('=') for fold in folds]
    folds = [(axis, int(line)) for axis, line in folds]
    return coords, folds


def fold_once(dots, fold):
    axis, line_num = fold
    if axis == 'x':
        for dot in dots:
            if dot.x > line_num:
                dot.x -= (dot.x - line_num) * 2
    elif axis == 'y':
        for dot in dots:
            if dot.y > line_num:
                dot.y -= (dot.y - line_num) * 2
    else:
        assert False


def deduplicate(dots):
    deduped = {}
    for dot in dots:
        if dot not in deduped:
            # Add dot to the map and set the value to ## (for printing later)
            deduped[dot] = '##'
    return deduped


def day13a():
    print("    Part A")
    dots, folds = get_input()
    fold_once(dots, folds[0])
    dots = deduplicate(dots)
    print(len(dots))
    assert len(dots) == 759
    return len(dots)


def day13b():
    print("\n    Part B")
    dots, folds = get_input()
    for fold in folds:
        fold_once(dots, fold)
        
    dots = deduplicate(dots)
    render_map(dots, str, '  ')


if __name__ == '__main__':
    day13a()
    day13b()
