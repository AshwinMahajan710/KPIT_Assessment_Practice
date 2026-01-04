from typing import Dict, List, Any

# Getting value from dictionary
def get_value(pairs: Dict[str,int], key: str, value: int):
    if key not in pairs.keys():
        return value
    else:
        return pairs[key]

# Inverting dictionary
def invert_dictionary(pairs: Dict[str,int]) -> Dict[int,List[str]]:
    new_pairs:Dict[int, List[str]] = {}
    for pair in pairs.items():
        key, val = pair
        if val not in new_pairs.keys():
            new_pairs[val] = [key]
        else:
            new_pairs[val].append(key)
    return new_pairs

# Merging 2 dictionaries
def merge_dictionaries(pairs1: Dict[str,int], pairs2: Dict[str,int]) -> Dict[str,int]:
    new_merged_dictionary: Dict[str,int] = {}
    for pair in pairs1.items():
        key, val = pair
        new_merged_dictionary[key] = val
    for pair in pairs2.items():
        key, val = pair
        if key in new_merged_dictionary.keys():
            new_merged_dictionary[key] = new_merged_dictionary[key] + val
        else:
            new_merged_dictionary[key] = val
    return new_merged_dictionary

# function to filter dictionary items w.r.t. values in each pair
def filter_by_value(data: Dict[str,int], threshold: int):
    return dict(filter(lambda x: x[1]>=threshold, data.items()))

def main():

    # To get value from dictionary
    print("\n< - - - - - Get Values - - - - - >")
    print(get_value({'a':3, 'b': 5, 'c': 23}, 'a', 0))
    print(get_value({}, 'any', 8))

    # To invert dictionary values
    print("\n< - - - - - Inverting dictionary - - - - - >")
    print(invert_dictionary({'a':1,'b':2, "c": 1}))

    # merging dictionaries
    print("\n< - - - - - Merging Dictionaries - - - - - >")
    print(merge_dictionaries({"a":1,"b":2},{"b":3,"c":4}))

    # Filter by value
    print("\n< - - - - - Filtering by values - - - - - >")
    print(filter_by_value({'a':5,'b':3,'c':8},5))

if __name__=="__main__":
    main()

