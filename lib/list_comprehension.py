#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens


print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    sentences = [f"{s}!" for s in sentence_list]
    return sentences


print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
