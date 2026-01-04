from typing import List, Dict, Any
from functools import reduce

# function to get max value
def get_max_val(values: List[int])->int:
    if(len(values)==0):
        return 0
    return reduce(lambda x,y: x if x>y else y, values) 

# function to sum only even no
def sum_of_even(values: List[int])->int:
    return reduce(lambda acc,no: acc + no if no%2==0 else acc, values, 0)

#  function to help rotate
def rotate_helper(values: List[int], start: int, end: int):
    while start < end:
        temp = values[start]
        values[start] = values[end]
        values[end] = temp
        start = start +1
        end = end - 1

# rotating values to right
def rotate_to_right(values: List[int], steps: int) -> List[int]:
    if len(values) == 0:
        return []
    steps = steps%len(values)
    if steps == 0:
        return values
    rotate_helper(values, 0, len(values)-1)
    rotate_helper(values,0,steps-1)
    rotate_helper(values,steps,len(values)-1)
    return values

# finding the median in array
def find_median(values: List[int]) -> float:
    if len(values) == 0:
        return 0
    sorted_values = sorted(values,reverse=False)
    return sorted_values[(len(sorted_values)//2)] if len(sorted_values)%2 != 0 else (sorted_values[(len(sorted_values))//2] + sorted_values[(len(sorted_values)//2) - 1]) / 2.0 

def main():

    print("< - - - - - Max Value - - - - - >")
    print(get_max_val([3,7,2,5]))
    print(get_max_val([-10,-20,-3]))
    print(get_max_val([0]))
    print(get_max_val([]))
    print(get_max_val([5,5,5]))
    print(get_max_val([100,-100,50]))

    print("< - - - - - Sum of evens - - - - - >")
    print(sum_of_even([1,2,3,4,5]))
    print(sum_of_even([2,4,6,8]))
    print(sum_of_even([1,3,5]))
    print(sum_of_even([]))
    print(sum_of_even([0,-2,7]))
    print(sum_of_even([10]))

    print("< - - - - - Rotate Right - - - - - >")
    print(rotate_to_right([1,2,3,4,5],2))
    print(rotate_to_right([10,20,30],3))
    print(rotate_to_right([7,8,9],0))
    print(rotate_to_right([],4))
    print(rotate_to_right([1,2],5))
    print(rotate_to_right([5,6,7,8],6))

    print("< - - - - - Calculate Median - - - - - >")
    print(find_median([3,1,2]))
    print(find_median([4,1,7,2]))
    print(find_median([10]))
    print(find_median([]))
    print(find_median([5,5,5,5]))
    print(find_median([-3,0,3]))

    
if __name__ == "__main__":
    main()