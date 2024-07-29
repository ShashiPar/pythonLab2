# dictOperations.py

def merging_Dict(*args):
    """Merge multiple dictionaries into one."""
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result

def common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    common = set(args[0].keys())
    for dictionary in args[1:]:
        common.intersection_update(dictionary.keys())
    return common

def invert_dict(d):
    """Invert a dictionary, swapping keys and values. Group keys in a list if multiple keys have the same value."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted

def common_key_value_pairs(*args):
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    common = set(args[0].items())
    for dictionary in args[1:]:
        common.intersection_update(dictionary.items())
    return dict(common)
