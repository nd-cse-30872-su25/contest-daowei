#!/usr/bin/env python3
''' used DP and memoization to calculate the shortest path '''
import sys

def find_path(matrix: list[list[int]], size: tuple[int, int], end: tuple[int, int], min_matrix: list[list[int]])->list[int]:
    path = []

    rows, cols = size
    cols += 1

    row, col = end
    col += 1

    cur_target = min_matrix[row][col]
    while cur_target != 0:
        path.append(row+1)
        cur_target -= matrix[row][col]
        row_up = row - 1
        row_down = row + 1
        # check if need to goes past top or bottom
        if row_up < 0:
            row_up = rows - 1
        if row_down > rows:
            row_down = 0

        if cur_target == min_matrix[row_up][col-1]:
            row = row_up
        elif cur_target == min_matrix[row_down][col-1]:
            row = row_down
        elif cur_target == min_matrix[row][col-1]:
            pass
        col -= 1

    path.reverse()
    return path

def find_min_weight(matrix: list[list[int]], size: tuple[int, int])->list[list[int]]:
    ''' finds the min weight via DP '''
    min_matrix = [row[:] for row in matrix]
    rows, cols = size
    for col in range(1, cols+2):
        for row in range(0, rows+1):
            row_up = row - 1
            row_down = row + 1
            # check if need to goes past top or bottom
            if row_up < 0:
                row_up = rows - 1
            if row_down > rows:
                row_down = 0

            min_matrix[row][col] = matrix[row][col] + min(
                min_matrix[row_up][col-1],
                min_matrix[row][col-1],
                min_matrix[row_down][col-1],
            )

    return min_matrix

def main():
    for line in sys.stdin:
        rows, cols = map(int, line.strip().split())
        target = (rows - 1, cols - 1)

        matrix = [[0 for _ in range(cols+1)] for _ in range(rows)]
        for i in range(rows):
            new_row = [int(x) for x in next(sys.stdin).strip().split()]
            matrix[i][1:] = new_row.copy()

        min_matrix = find_min_weight(matrix, target)

        min = sys.maxsize
        min_row = 0
        for i in range(rows):
            if min_matrix[i][cols] < min:
                min_row = i + 1
                min = min_matrix[i][cols]

        path = find_path(matrix, target, (min_row-1, cols-1), min_matrix)
        
        print(min)
        #print(min_matrix)
        path = [str(x) for x in path]
        print(" ".join(path))

if __name__ == "__main__":
    main()