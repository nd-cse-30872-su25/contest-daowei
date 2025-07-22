#!/usr/bin/env python3
''' outputs all paths that lead to the target'''
import sys
from collections import deque

def __dfs(paths: list, tree: list, target: int, cur_path: list, cur_score: int, index: int):
    cur_val = tree[index]
    if cur_val == 0:
        return
    cur_path.append(tree[index])

    new_score = cur_score + cur_val
    if new_score > target:
        cur_path.pop()
        return
    
    left_child = index*2 + 1
    right_child = index*2 + 2

    # check if leaf node
    has_left_child = (left_child < len(tree)) and (tree[left_child] != 0)
    has_right_child = (right_child < len(tree)) and (tree[right_child] != 0)
    if not (has_left_child or has_right_child):
        if new_score == target:
            paths.append(cur_path.copy())
            cur_path.pop()
            return

    
    if left_child < len(tree):
        __dfs(paths, tree, target, cur_path, new_score, left_child)

    if right_child < len(tree):
        __dfs(paths, tree, target, cur_path, new_score, right_child)
    cur_path.pop()

    return

def find_paths(paths: list, tree: list, target: int):
    ''' uses dfs to find all paths'''
    cur_path = []

    __dfs(paths, tree, target, cur_path, 0, 0)
    
def main():
    for line in sys.stdin:
        target = int(line.strip())

        tree = next(sys.stdin).strip()
        tree = [int(x) for x in tree.split()]

        paths = []

        find_paths(paths, tree, target)
        paths.sort()
        
        for path in paths:
            path = map(str, path)
            print(f"{target}: {", ".join(path)}")


if __name__ == "__main__":
    main()