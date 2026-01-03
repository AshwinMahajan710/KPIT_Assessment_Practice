# # <  - - - - - - - - - - sum of digits of no - - - - - - - - - - >
# no = input("Enter the no: ")
# sum = 0
# for i in no:
#     sum = sum + int(i)
# print("Sum is: ",sum)


# # < - - - - - - - - - - reverse the no - - - - - - - - - - - - ->
# no = input("Enter the no: ")
# rev = no[::-1] # start = 0, end = 0, step = -1 (go backward)
# print(rev)

# # < - - - - - - - - - - reverse the integer no - - - - - - - - - - - - ->
# no2 = int(input("Enter the no: "))
# revNo = 0
# while no2!=0:
#     temp = no2%10
#     revNo = revNo*10 + temp
#     no2 = no2//10 # floor division to guaranteer intger no only
# print(revNo)

# # < - - - - - - - - - Calculate frequency of each digit in no - - - - - - - - - - - - >
# no3 = int(input("Enter the no: "))
# val_freq_dict = {}
# while no3!=0:
#     temp = no3 % 10
#     if temp not in val_freq_dict:
#         val_freq_dict[temp] = 1
#     else:
#         val_freq_dict[temp] = val_freq_dict[temp] + 1
#     no3 = no3 // 10
# print(val_freq_dict)

# # < - - - - - - - - - Check if a specific element exists in a list. - - - - - - - - - > 
# list1 = [1,2,3,3,5,6,1,7]
# if 8 in list1:
#     print("yes")
# else:
#     print("No")

# # < - - - - - - - - - Remove duplicate elements from a list, maintaining the original order of the remaining elements. - - - - - - - > 
# list2 = []
# for ele in list1:
#     if ele not in list2:
#             list2.append(ele)


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
 