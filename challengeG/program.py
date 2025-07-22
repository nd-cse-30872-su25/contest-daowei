#!/usr/bin/env python3

''' program that uses union find to determine how many isolated circuits '''
import sys

def find_circuits(adj_matrix: list[list[int]], num_vert: int)->int:
    Parent = [int(i) for i in range(num_vert)]

    def find(x: int):
        if Parent[x] != x:
            Parent[x] = find(Parent[x])
            return Parent[x]
        else:
            return x

    def uunion(a: int, b: int):
        ''' makes b part of a '''
        Parent[find(b)] = find(a)

    num_ciruits = num_vert

    for row in range(num_vert):
        for col in range(row+1, num_vert):
            if adj_matrix[row][col] == 1:
                if find(row) != find(col):
                    num_ciruits -= 1
                    uunion(row, col)

    return num_ciruits

def main():
    ''' parse input'''
    sys_count = 0
    for line in sys.stdin:
        num_vert = int(line.strip())

        sys_count += 1
        adj_matrix = []
        for i in range(num_vert):
            read_row = next(sys.stdin).strip().split()
            new_row = [int(x) for x in read_row]
            adj_matrix.append(new_row)

        num_circuits = find_circuits(adj_matrix, num_vert)

        print(f"System {sys_count} isolated circuits: {num_circuits}")

if __name__ == "__main__":
    main()
