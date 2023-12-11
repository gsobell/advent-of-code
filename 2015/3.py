from sys import setrecursionlimit
from functools import reduce

with open("3.in") as f:
    a = list(f.read())

setrecursionlimit(len(a) * 2)


def house_visit(path: list, houses: set = {(0, 0)}, x: int = 0, y: int = 0) -> list:
    if not path:
        return houses
    match path[0].split():
        case ["^"]:
            y += 1
        case ["v"]:
            y -= 1
        case ["<"]:
            x -= 1
        case [">"]:
            x += 1
    houses.add((x, y))
    return house_visit(path[1:], houses, x, y)


print(len(house_visit(a)))
# correct answer for given input is 2572


def robo_deliver(path) -> set:
    santa = [house for k, house in enumerate(a) if k % 2 != 0]
    robot = [house for k, house in enumerate(a) if k % 2 == 0]
    b = house_visit(santa)
    c = house_visit(robot)
    return c.union(b)


print(len(robo_deliver(a)))
