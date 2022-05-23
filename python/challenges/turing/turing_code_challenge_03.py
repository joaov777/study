##  Turing - Code challenge 03

import random as r
import string


def findTheDifference(s: str, t: str) -> str:
    result = ''

    random_letter = r.choice(string.ascii_letters)

    t = s

    result = r.sample(t, len(s))
    result += random_letter

    return random_letter


if __name__ == '__main__':

    s = input().strip()
    t = input().strip()

    print(findTheDifference(s, t))
