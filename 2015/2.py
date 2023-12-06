#!/usr/bin/env python3
from sys import setrecursionlimit
from functools import reduce

with open ("2.in") as f:
    a = [list(map( int, a.split("x"))) for a in f.read().split('\n') if a]

# setrecursionlimit(len(a) * 2 ) 

def cartesian (l, w, h) -> [int]:
    sides = [l, w, h]
    return [sides[a] * sides[b] for a, _ in enumerate(sides) for b, _ in enumerate(sides) if a != b] 

def duplicate_least(sides : [int]) -> [int]:
    return sides + [min(sides)]

def paper(sides: [[int]]) -> int:
    total = 0
    for side in sides:
        total += sum(duplicate_least(cartesian(*side)))
    print(total)

paper(a) # correct answer is: 1588178

def perimeter (l, w, h) -> [int]:
    sides = [l, w, h]
    return [2 * (sides[a] + sides[b]) for a, _ in enumerate(sides) for b, _ in enumerate(sides) if a != b] 


def cubic_feet(l, w, h) -> int:
    return l * w * h

def ribbon(sides: [[int]]) -> int:
    total = 0
    for side in sides:
        total += min(perimeter(*side)) + cubic_feet(*side)
    print(total)

ribbon(a)
