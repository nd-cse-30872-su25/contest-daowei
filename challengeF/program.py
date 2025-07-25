#!/usr/bin/env python3
''' used min_weight and memoization to calculate the shortest path '''
import sys

def dp(matrix: list[list[int]], min_weight: list[list[int]], store_path: list[list[int]], rows: int, cols: int):
    ''' use DP to calculate min_weight at every point '''
    # min_weight of first col is just matrix first col
    for i in range(rows):
        min_weight[i][0] = matrix[i][0]

    for j in range(1, cols):
        for i in range(rows):
            # top, middle, bottom
            potential_rows = sorted([(i - 1 + rows) % rows, i, (i + 1) % rows])

            row_min = sys.maxsize

            for row in potential_rows:
                if min_weight[row][j-1] < row_min:
                    row_min = min_weight[row][j-1]
                    best_row = row

            min_weight[i][j] = matrix[i][j] + row_min
            store_path[i][j] = best_row

def reconstruct_path(store_path: list[list[int]], find_row: int, cols: int)->list[int]:
    ''' reconstruct path by backtracking store_path'''
    path = []

    current_row = find_row
    for j in range(cols - 1, -1, -1):
        path.append(current_row + 1)
        current_row = store_path[current_row][j]
    
    path.reverse()
    return path

def main():
    ''' parses input '''
    input_data = sys.stdin.read().split()

    index = 0
    while index < len(input_data):
        try:
            rows = int(input_data[index])
            cols = int(input_data[index+1])
            index += 2

            matrix = []
            for i in range(rows):
                input_line = []
                for j in range(cols):
                    input_line.append(int(input_data[index]))
                    index += 1
                matrix.append(input_line)

        except (ValueError, IndexError):
            break
        

        min_weight = [[0] * cols for _ in range(rows)]
        # stores previous row
        store_path = [[0] * cols for _ in range(rows)]

        dp(matrix, min_weight, store_path, rows, cols)
        
        # find row of min_weight
        min_total_weight = sys.maxsize
        find_row = -1
        for i in range(rows):
            if min_weight[i][cols-1] < min_total_weight:
                min_total_weight = min_weight[i][cols-1]
                find_row = i

        path = reconstruct_path(store_path, find_row, cols)
        
        print(min_total_weight)
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()