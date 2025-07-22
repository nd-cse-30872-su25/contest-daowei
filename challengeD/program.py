#!/usr/bin/env python3

''' finds all possible ways to achieve a score '''

import sys

def helper(paths: list, cur_score: int, target_score: int, cur_path: list, min_score: int):
    if cur_score == target_score:
        paths.append(cur_path.copy())
        return
    elif cur_score > target_score:
        return    

    for i in [2, 3, 7]:
        if (i >= min_score) and (cur_score + i <= target_score):
            cur_path.append(str(i))
            helper(paths, cur_score + i, target_score, cur_path, i)
            cur_path.pop()

    return
    
def find_ways(score: int)->list[list[str]]:
    paths = []
    cur_path = []

    helper(paths, 0, score, cur_path, 0)

    return paths

def main():
    ''' parse input '''
    for line in sys.stdin:
        score = int(line.strip())

        paths = find_ways(score)
        num_ways = len(paths)
        if num_ways == 1:
            print(f"There is {num_ways} way to achieve a score of {score}:")
        else:
            print(f"There are {num_ways} ways to achieve a score of {score}:")
        for path in paths:
            print(" ".join(path))

if __name__ == "__main__":
    main()