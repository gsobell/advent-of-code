#!/usr/bin/env python3
from sys import setrecursionlimit

with open("1.in") as f:
    a = f.read()

setrecursionlimit(len(a) * 2)


def counter(s: str, count: int = 0) -> int:
    if len(s) == 0:
        return count
    elif s[0] == "(":
        count += 1
    elif s[0] == ")":
        count -= 1
    return counter(s[1:], count)


def basement(s: str, count: int = 0, step: int = 0) -> int:
    if count == -1:
        return step
    else:
        step += 1
    if s[0] == "(":
        count += 1
    elif s[0] == ")":
        count -= 1
    return basement(s[1:], count, step)


print(counter(a))
print(basement(a))
