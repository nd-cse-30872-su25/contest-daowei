#!/usr/bin/env python3

import sys
from collections import defaultdict, deque

# Types
# key: tuple of parent name, list of all their children
Family = defaultdict[str, list[str]]
# Key: Generation level. E.g 0. is eldest. each has a list of all members
Generations = defaultdict[int, list[str]]

def find_presents(family: Family, parent_pairs: dict, person: str, childs_parent: dict)->set[str]:
    presents = set()
    if person in childs_parent:
        person_parent = childs_parent[person]
    elif parent_pairs[person] in childs_parent:
        person_parent = childs_parent[parent_pairs[person]]
    else:
        return presents

    person_sibling = family[person_parent].copy()
    # remove person
    try:
        person_sibling.remove(person)
    except ValueError:
        pass
    # remove spouse
    try:
        person_sibling.remove(parent_pairs[person])
    except (ValueError, IndexError):
        pass

    for person in person_sibling:
        if person in family:
            for niece in family[person]:
                presents.add(niece)

    return presents

def main():
    ''' parsing input '''
    for line in sys.stdin:
        num_fams = int(line.strip())
        if num_fams == 0:
            break
        family: Family = defaultdict(list)
        parent_pairs = defaultdict()
        gift_givers = []

        first_gen = None

        for _ in range(num_fams):
            parents, children = next(sys.stdin).strip().split(":")
            parent1, parent2 = parents.strip().split()
            parent_pairs[parent1] = parent2
            parent_pairs[parent2] = parent1
            if first_gen is None:
                first_gen = (parent1, parent2)
            children = [str(x) for x in children.split()]
            family[parent1] = children
            family[parent2] = children

        # dict of child's parent relationship: key(child) value(parent)
        childs_parent = defaultdict()
        for key, value in family.items():
            for child in value:
                if child not in childs_parent:
                    childs_parent[child] = key 
        
        #print(childs_parent)
        #print(family)
    
        num_gift_givers = int(next(sys.stdin).strip())
        for _ in range(num_gift_givers):
            gift_givers.append(next(sys.stdin).strip())

        # find generation of people in gift_givers
        for person in gift_givers:
            presents = find_presents(family, parent_pairs, person, childs_parent)
            presents = list(presents)
            presents.sort()
            if len(presents) >0:
                print(f"{person} needs to buy gifts for: {", ".join(presents)}")
            else:
                print(f"{person} does not need to buy gifts")

if __name__ == "__main__":
    main()

