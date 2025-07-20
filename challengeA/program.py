#!/usr/bin/env python3

''' program that determins how many buildings have a view of the sunset'''
import sys

def main():
    ''' parses input '''
    for line in sys.stdin:
        heights = [int(x) for x in line.strip().split()]

        # traverse from back to front, seeing which buildings are blocked
        curr = len(heights) - 1
        
        curr_tallest = 0
        buildings_blocked = 0
        while curr >= 0:
            if curr_tallest >= heights[curr]:
                buildings_blocked += 1
            else:
                curr_tallest = heights[curr]
            curr -= 1
        
        not_blocked = len(heights) - buildings_blocked

        print(not_blocked)

if __name__ == "__main__":
    main()


