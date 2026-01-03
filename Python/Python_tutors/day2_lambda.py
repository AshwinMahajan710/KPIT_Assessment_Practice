# 1. how actually lambda works
numbers = [1,2,3,4,5,6,7,8,9]
is_odd = lambda x: x % 2 != 0
print(list(filter(is_odd, numbers)))

# # 2. more complex --> for sorting using the different key 
# objects = [{'name':'John','age':25}, {'name':'John','age':15}, {'name':'John','age':95}, {'name':'John','age':35}]
# print(sorted(object, key=lambda x: x[1]))

# 3. also can use map function
a = [1,2,3,4,5]
r = list(map(lambda x:x**2, a))
print(r)

# 4. functool modules
from functools import reduce # --> opposite of map
sumNumbers = lambda x,y: x+y
l1 = [1,2,3,4,4,5,6]
resultList = reduce(sumNumbers,l1)
print(resultList)

# 4. functool modules with lambda inside
from functools import reduce # --> opposite of map
l1 = [1,2,3,4,4,5,6]
resultList = reduce(lambda x,y: x-y,l1)
print(resultList)

# using the filetr function
fruits = ['apple', 'banana', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))
print(a_fruits)

#  python next function along with remove --> use any function to find the first occurance only 