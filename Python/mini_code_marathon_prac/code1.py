from typing import List, Dict, Any
from functools import reduce

# function to filter by prefix
def filter_by_prefix(words: List[str], prefix: str)->List[str]:
    return list(filter(lambda x: x.startswith(prefix), words))

# function to get longest string
def get_longest_string(words: List[str]) -> str:
    return reduce(lambda x,y : x if len(x)>len(y) else y, words)

# function to count occurences of particular string in list of strings
def count_occurences(words: List[str], to_count: str) -> int:
    return sum(1 for word in words if word == to_count)

# function to join words in string with seperator given
def join_with_seperator(words: List[str], seperator: str) -> str:
    return reduce(lambda x,y: x+seperator+y, words)

def main():

    print("\n< - - - - Filter by prefix - - - - >")
    print(filter_by_prefix(['apple','ape','banana','cap'],'ap'))
    print(filter_by_prefix(['cat','dog','cow'],'c'))
    print(filter_by_prefix(['test','Test','testig'],'Test'))
    print(filter_by_prefix(['hello','world'],'x'))
    print(filter_by_prefix([],'any'))
    print(filter_by_prefix(['prefix','prequel','prevent'],'pre'))

    print("\n< - - - - - Longest String - - - - - >")
    print(get_longest_string(["hi","hello","hey"]))
    print(get_longest_string(['aaaa','bbb','cc']))
    print(get_longest_string(["one","three",'seven']))
    print(get_longest_string(['a']))
    print(get_longest_string(["long","longer","longest"]))
    
    print("\n< - - - - - Count Occurences - - - - - >")
    print(count_occurences(['a','b','c','a','a'],'a'))
    print(count_occurences(['apple','banana','cherry','banana'],'banana'))
    print(count_occurences(['cat','dog','cow'],'c'))
    print(count_occurences(['x','y','z'],'a'))
    print(count_occurences(['repeat','repeat','repeat'],'repeat'))

    print("\n< - - - - - Join with seperator - - - - - >")
    print(join_with_seperator(['a','b','c'],','))

if __name__=="__main__":
    main()