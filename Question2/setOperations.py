# setOperations.py

def add_element(s, element):
    
    s.add(element)

def remove_element(s, element):
   
    s.discard(element)

def union_and_intersection(s1, s2):
    
    return s1.union(s2), s1.intersection(s2)

def difference(s1, s2):
    
    return s1.difference(s2)

def is_subset(s1, s2):
   
    return s1.issubset(s2)

def set_length(s):
    
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    
    return s1.symmetric_difference(s2)

def power_set(s):
    
    from itertools import chain, combinations
    return set(frozenset(c) for c in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def unique_subsets(s):
   
    from itertools import chain, combinations
    return [set(c) for c in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))]
