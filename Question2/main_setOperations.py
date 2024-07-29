# main_setOperations.py
from setOperations import (
    add_element, remove_element, union_and_intersection,
    difference, is_subset, set_length, symmetric_difference,
    power_set, unique_subsets
)

def main():
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}

    print("Original sets:")
    print("s1:", s1)
    print("s2:", s2)

    # Add element
    add_element(s1, 5)
    print("\nAfter adding element 5 to s1:", s1)

    # Remove element
    remove_element(s2, 6)
    print("After removing element 6 from s2:", s2)

    # Union and Intersection
    union_set, intersection_set = union_and_intersection(s1, s2)
    print("\nUnion of s1 and s2:", union_set)
    print("Intersection of s1 and s2:", intersection_set)

    # Difference
    diff_set = difference(s1, s2)
    print("\nDifference s1 - s2:", diff_set)

    # Subset check
    subset_check = is_subset({1, 2}, s1)
    print("\nIs {1, 2} a subset of s1?:", subset_check)

    # Length of set
    length_s1 = set_length(s1)
    print("\nLength of s1:", length_s1)

    # Symmetric Difference
    sym_diff_set = symmetric_difference(s1, s2)
    print("\nSymmetric difference of s1 and s2:", sym_diff_set)

    # Power Set
    power_set_s1 = power_set(s1)
    print("\nPower set of s1:", power_set_s1)

    # Unique Subsets
    unique_subsets_s1 = unique_subsets(s1)
    print("\nUnique subsets of s1:")
    for subset in unique_subsets_s1:
        print(subset)

if __name__ == "__main__":
    main()
