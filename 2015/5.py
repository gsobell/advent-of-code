#!/usr/bin/env python3
from sys import setrecursionlimit
from functools import reduce

with open ("5.in") as f:
    a = list(f.read().split())

# setrecursionlimit(len(a) * 2 )

def is_nice(word : str) -> bool:
    return vowel_count(word) and double_letter(word) and not bad_word(word) 

def vowel_count(word: str) -> bool:
    i = 0
    for letter in word:
        if letter in 'aeiou':
            i += 1
    return True if i >= 3 else False

def double_letter(word: str) -> bool:
    for k, letter in enumerate(word):
        if not k:
            continue
        if letter == word[k - 1]:
            return True
    return False

def bad_word(word: str) -> bool:
    for bad in ('ab', 'cd', 'pq', 'xy'):
        if bad in word:
            return True
    return False    

def nice_count(words : list) -> int:
    return len([word for word in words if is_nice(word)])


def is_nice2(word : str) -> bool:
    return double_letter2(word) and repeat_with_gap(word)


def double_letter2(word: str) -> bool:
    for k, letter in enumerate(word):
        if k <= 2:
            continue
        if word[k - 2: k] in word[:k - 2] + word[k + 1 :]:
            return True
    return False

def repeat_with_gap(word: str) -> bool:
    for k, letter in enumerate(word):
        if k <= 2:
            continue
        if letter == word[k - 2]:
            return True
    return False

def nice_count2(words : list) -> int:
    return len([word for word in words if is_nice2(word)])

print(nice_count(a))
print(nice_count2(a))




