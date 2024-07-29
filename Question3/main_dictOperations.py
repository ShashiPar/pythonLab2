# main_dictOperations.py
from dictOperations import merging_Dict, common_keys, invert_dict, common_key_value_pairs

def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 4}
    dict3 = {'a': 1, 'c': 3, 'e': 5}

    # Demonstrate merging dictionaries
    merged_dict = merging_Dict(dict1, dict2, dict3)
    print("Merged dictionary:", merged_dict)

    # Demonstrate finding common keys
    common_keys_result = common_keys(dict1, dict2, dict3)
    print("Common keys:", common_keys_result)

    # Demonstrate inverting a dictionary
    inverted_dict1 = invert_dict(dict1)
    print("Inverted dict1:", inverted_dict1)

    inverted_dict2 = invert_dict({'x': 1, 'y': 2, 'z': 1})
    print("Inverted dict with grouped keys:", inverted_dict2)

    # Demonstrate finding common key-value pairs
    common_kv_pairs = common_key_value_pairs(dict1, dict3)
    print("Common key-value pairs:", common_kv_pairs)

if __name__ == "__main__":
    main()
