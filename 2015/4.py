#!/usr/bin/env python3
from sys import setrecursionlimit
from functools import reduce
from hashlib import md5

with open("4.in") as f:
    a = str(f.read())

setrecursionlimit(len(a) * 2)

# not the most elegant way, but it works


def hash_find1(a):
    i = 0
    while True:
        if str(md5((a + str(i)).encode()).hexdigest())[0:5] == "00000":
            return i
        i += 1


def hash_find2(a):
    i = 0
    while True:
        if str(md5((a + str(i)).encode()).hexdigest())[0:6] == "000000":
            return i
        i += 1


print(hash_find(a))
