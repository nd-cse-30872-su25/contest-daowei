#!/usr/bin/env python3

import sys

# global variable
SYMBOLS = ["+", "-", "*"]

def get_expression(perm: str)->str:
    expression = f"(((9 {perm[0]} 8) {perm[1]} 7) {perm[2]} 6) {perm[3]} (5 {perm[4]} (4 {perm[5]} (3 {perm[6]} (2 {perm[7]} 1))))"
    return expression

def find_permutation(cur_str: str):
    if len(cur_str) == 8:
        yield cur_str
        return

    for symb in SYMBOLS:
        yield from find_permutation(cur_str + symb)

def find_comb(history: dict[str, int], target: int)->str:
    cur_str = ""
    for perm in find_permutation(cur_str):
        if perm in history:
            answer = history[perm]
            expression = get_expression(perm)
        else:
            expression = get_expression(perm)
            answer = eval(expression)
            history[perm] = answer
        if answer == target:
            return expression

    return ""

def main():
    ''' parses input '''
    history = {}
    for line in sys.stdin:
        target = int(line.strip())

        exp = find_comb(history, target)
        print(f"{exp} = {target}")

if __name__ == "__main__":
    main()