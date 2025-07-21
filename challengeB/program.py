#!/usr/bin/env python3
''' determine if words are isomorphic '''

import sys

def main():
    for line in sys.stdin:
        s, t = line.strip().split()
        s = [x for x in s]
        t = [t for t in t]
        
        if len(s) != len(t):
            print("Not Isomorphic")

        s_to_t = {}
        t_to_s = {}

        is_isomorphic = True
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    is_isomorphic = False
                    break
            else:
                s_to_t[s_char] = t_char

            if t_char in t_to_s:
                if t_to_s[t_char] != s_char:
                    is_isomorphic = False
                    break
            else:
                t_to_s[t_char] = s_char

        if is_isomorphic:
            print("Isomorphic")
        else:
            print("Not Isomorphic")    
if __name__ == "__main__":
    main()
