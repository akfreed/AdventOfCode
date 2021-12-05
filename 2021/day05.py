from utility import Vector, render_map


def get_input_a():
    with open('day05.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    lines = [line.split(' -> ') for line in lines]
    coords = []
    for line in lines:
        x, y = [int(n) for n in line[0].split(',')]
        v1 = Vector(x, y)
        x, y = [int(n) for n in line[1].split(',')]
        v2 = Vector(x, y)
        coords.append((v1, v2))
    return coords


def get_input_b():
    return get_input_a()


def day5a():
    print("    Part A")
    coords = get_input_a()
    coords = [coord for coord in coords if coord[0].x == coord[1].x or coord[0].y == coord[1].y]
    grid = {}
    for coord in coords:
        # horizontal
        if coord[0].x == coord[1].x:
            start = coord[0].y if coord[0].y < coord[1].y else coord[1].y
            end = (coord[0].y if coord[0].y > coord[1].y else coord[1].y) + 1
            for y in range(start, end):
                v = Vector(coord[0].x, y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1
        # vertical
        if coord[0].y == coord[1].y:
            start = coord[0].x if coord[0].x < coord[1].x else coord[1].x
            end = (coord[0].x if coord[0].x > coord[1].x else coord[1].x) + 1
            for x in range(start, end):
                v = Vector(x, coord[0].y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1


    #render_map(grid, lambda x: str(x))
    count = 0
    for key in grid:
        if grid[key] > 1:
            count += 1
    print(count)



def day5b():
    print("\n    Part B")
    coords = get_input_b()
    #coords = [coord for coord in coords if coord[0].x == coord[1].x or coord[0].y == coord[1].y]
    grid = {}
    for coord in coords:
        # horizontal
        if coord[0].x == coord[1].x:
            start = coord[0].y if coord[0].y < coord[1].y else coord[1].y
            end = (coord[0].y if coord[0].y > coord[1].y else coord[1].y) + 1
            for y in range(start, end):
                v = Vector(coord[0].x, y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1
        # vertical
        elif coord[0].y == coord[1].y:
            start = coord[0].x if coord[0].x < coord[1].x else coord[1].x
            end = (coord[0].x if coord[0].x > coord[1].x else coord[1].x) + 1
            for x in range(start, end):
                v = Vector(x, coord[0].y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1

        # diagonal
        else:
            start_y = coord[0].y
            end_y = coord[1].y
            if start_y > end_y:
                step_y = -1
            else:
                step_y = 1
            end_y += step_y

            start_x = coord[0].x
            end_x = coord[1].x
            if start_x > end_x:
                step_x = -1
            else:
                step_x = 1
            end_x += step_x

            x_range = [_ for _ in range(start_x, end_x, step_x)]
            y_range = [_ for _ in range(start_y, end_y, step_y)]

            #assert end_x - start_x == end_y - start_y
            for i, x in enumerate(x_range):
                y = y_range[i]
                v = Vector(x, y)
                if v in grid:
                    grid[v] += 1
                else:
                    grid[v] = 1



        #render_map(grid, None, ".")
        #print()
    count = 0
    for key in grid:
        if grid[key] > 1:
            count += 1
    print(count)

    #not 20027


if __name__ == '__main__':
    day5a()
    day5b()
