from utility import *


def get_input():
    with open('day17.txt', 'r') as file:
        return Vector(57, 116), Vector(-198, -148)
        #return Vector(20, 30), Vector(-10, -5)

def in_target(pos, target_x: Vector, target_y):
    if pos.x >= target_x.x and pos.x <= target_x.y and pos.y >= target_y.x and pos.y <= target_y.y:
        return True
    return False


def past_target(pos, target_x, target_y):
    if pos.x > target_x.y or pos.y < target_y.x:
        return True
    return False


def simulate(d: Vector, target_x, target_y):
    pos = Vector(0, 0)
    max_height = 0
    while not past_target(pos, target_x, target_y):
        pos += d
        if pos.y > max_height:
            max_height = pos.y
        if d.x > 0:
            d.x -= 1
        d.y -= 1
        if in_target(pos, target_x, target_y):
            return True, max_height
    return False, max_height




def day17a():
    print("    Part A")
    target_x, target_y = get_input()

    dx_ranges = []
    agg = 0
    d = 0
    while True:
        d += 1
        agg += d
        if agg >= target_x.x and agg <= target_x.y:
            dx_ranges.append(d)
        elif agg > target_x.y:
            break
    print(dx_ranges)
    dy_max = -target_y.x + 1

    highest = 0
    h = Vector(0, 0)
    for dx in dx_ranges:
        for dy in range(dy_max):
            d = Vector(dx, dy)
            hit, height = simulate(d.clone(), target_x, target_y)
            if hit:
                if height > highest:
                    highest = height
                    h = d


    print(h)
    print(highest)



def day17b():
    print("\n    Part B")
    target_x, target_y = get_input()

    dx_ranges = []
    agg = 0
    d = 0
    while True:
        d += 1
        agg += d
        if agg >= target_x.x and agg <= target_x.y:
            dx_ranges.append(d)
        elif agg > target_x.y:
            break
    print(dx_ranges)
    dy_max = -target_y.x + 1

    count = 0
    for dx in range(1000):
        print(dx)
        for dy in range(-500, 500):
            d = Vector(dx, dy)
            hit, height = simulate(d.clone(), target_x, target_y)
            if hit:
                count += 1

    print(count)


if __name__ == '__main__':
    #day17a()
    day17b()
