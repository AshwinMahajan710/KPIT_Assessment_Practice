# # <  - - - - - - - - - - sum of digits of no - - - - - - - - - - >
# no = int(input("Enter the no: "))
# sum = 0
# while no!=0:
#     sum += no % 10
#     no = no // 10
# print(sum)

# # < - - - - - - - - - - reverse the no of string- - - - - - - - - - - - ->
# no = input("enter no: ")
# print(no[::-1])

# # < - - - - - - - - - - reverse the no - - - - - - - - - - - - ->
# no = int(input("Enter the no: "))
# rev_no = 0
# while no!=0:
#     rev_no = (rev_no*10) + (no%10)
#     no = no//10
# print(rev_no)

# # < - - - - - - - - - - - - - - - - - - - - - - - - - failed by me - - - - - - - - - - - - - - - - - - - - - - - - - >
# # # < - - - - - - - - - Calculate frequency of each digit in no - - - - - - - - - - - - >
# no = int(input("Enter the no: "))
# frequencies = {}
# while (no!=0):
#     if no%10 not in frequencies:
#         frequencies[no%10] = 1
#     else:
#         frequencies[no%10] += 1
#     no = no // 10
# print(sorted(frequencies.items(), key=lambda x: x[0]))

# # < - - - - - - - - - Check if a specific element exists in a list. - - - - - - - - - > 
# list1 = [1,2,3,3,5,6,1,7]
# if 8 in list1:
#     print("yes")
# else:
#     print("No")

# # < - - - - - - - - - Remove duplicate elements from a list, maintaining the original order of the remaining elements. - - - - - - - > 
# from functools import reduce
list1 = [1,2,3,4,4,3,2,1,1,2,3,5,6,6,5]
# print(reduce(lambda acc, x: acc + [x] if x not in acc else acc, list1, []))
seen = set()
new_list = []
for ele in list1:
    if ele not in seen:
        new_list.append(ele)
        seen.add(ele)
    else:
        continue
print(new_list)


# # Reverse the order of elements in a list without using the reverse() method or slicing [::-1].
# list2 = [1,2,3,4,5,6]
# listans = []
# for ele in list2:
#     listans.insert(0,ele)
# print(listans)
# # Example: [1, 2, 3] -> [3, 2, 1]
 
# # Check if a specific element exists in a list.
# if 2 in list2:
#     print("2 exist")
# else:
#     print("2 does not exist")

# # Concatenate two lists into a single list. Do not use the + operator.
# list1 = [1,2,3,5]
# list2 = [6,7,8,9]
# # print(list1 * list2) this operation is prohibited
# # print(list1 + list2) # this will work
# list1.append(list2) # will work but list inside list # so add elements manually one by one
# print (list1)

# # Create a new list that contains each element of an existing list repeated a certain number of times.
# list1 = [1,2,3,4,5]
# list2 = []
# for ele in list1:
#     for i in range(3):
#         list2.append(ele)
# print(list2)

# # Given two lists, find the elements that are present in both.
# answerList = [ele for ele in list1 if ele in list2]
# print(answerList)

# # Use list comprehension to create a new list containing only the even numbers from a given list.
# list1 = [1,2,3,4,5,6,7,8,9]
# even_list = [ele for ele in list1 if ele%2 == 0]
# print(even_list)

# # Use list comprehension to create a new list containing the squares of only the odd numbers from a given list.
# list1 = [1,2,3,4,5,6,7,8,9]
# even_list = [(ele*ele) for ele in list1 ]
# print(even_list)
 
# # Given a list of lists, flatten it into a single list.
# # Example: [[1, 2], [3, 4], [5]] -> [1, 2, 3, 4, 5]
# list1 = [[1, 2], [3, 4], [5], 8]
# seperate_ele = []
# for ele in list1:
#     if isinstance(ele,list):
#         for ele2 in ele:
#             seperate_ele.append(ele2)
# print(seperate_ele)
 
# Rotate a list to the right by n positions.
# Example: [1, 2, 3, 4, 5], n = 2 -> [4, 5, 1, 2, 3]
 
# Given a list of integers, group consecutive numbers into sublists.
# Example: [1, 2, 3, 5, 6, 7, 8, 9] -> [[1, 2, 3], [5, 6, 7, 8, 9]]
 
# Merge two sorted lists into a single sorted list without using the built-in sort() method.
 
# #  21. char frequency dictionary comprehensions
# text="Hello World!"
# print({k: text.count(k) for k in text})

# # 22. Invert dict
# text = {'x':1,'y':2, 'z': 2}
# print({v: [k for k in text if text[k]==v] for v in text.values()}) 

# 23. merge dictionaries
text = {'x':1,'y':2, 'z': 2}

