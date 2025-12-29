# # 1. Square the numbers  
# # Description: Given a list of integers, return a new list with each number squared.  
# # Key concepts: List comprehension or map with a lambda.  
# # Sample: nums = [1, 2, 3, 4] - [1, 4, 9, 16]
# nums = [1, 2, 3, 4] 
# ans = list(map(lambda x:x**2, nums))
# print(ans)

# # --> in filter no need of if else condition , just write one which return true
# # 2. Filter even numbers  
# # Description: From a list of integers, keep only the even ones.  
# # Key concepts: filter with a lambda (or list comprehension).  
# # Sample: nums = [5, 8, 13, 22] – [8, 22]
# nums = [5, 8, 13, 22]
# ans = list(filter(lambda x: x%2 == 0, nums))
# print(ans)

# ---> always import reduce from functool first
# --> reduce always receives 2 values
# # 3. Product of all elements  
# # Description: Compute the product of every element in a numeric list.  
# # Key concepts: reduce with a lambda.  
# # Sample: nums = [2, 3, 4] - 24
# from functools import reduce
# nums = [2, 3, 4]
# ans = reduce(lambda x,y: x*y, nums)
# print(ans)

# --> while using comprehension of for loop, always use it in enclosed brackets ()
# # 4. Concatenate uppercase strings
# # Description: Turn every string in a list to uppercase and concatenate them into a single string.
# # Key concepts: map + reduce (or "".join)
# # Sample: words = ['hello', 'world'] -> "HELLOWORLD"
# # * * * * * * * approch 1 * * * * * * *
# from functools import reduce
# words = ['hello', 'world']
# ans = reduce(lambda x,y: x+y, list(map(lambda x: x.upper(), words)))
# print(ans)
# # * * * * * * * approach 2 * * * * * * *
# words = ['hello', 'world']
# ans = ""
# final_ans = "".join(ele.upper() for ele in words)
# print(final_ans)

# # --> list + list = another list with both elements included 
# # 5. Flatten a 2-D integer matrix
# # Description: Convert a list of lists (matrix) into a flat 1-D list preserving row order.
# # Key concepts: List comprehension (nested) or reduce.
# # Sample: mat = [[1,2],[3,4],[15]] -> [1,2,3,4,5]
# # * * * * * * * approach 1 --> list comprehensions * * * * * * *
# mat = [[1,2],[3,4],[5]]
# ans = list(ele for row in mat for ele in row) 
# print(ans)
# # * * * * * * * * approach 2 --> using reduce* * * * * * * * 
# from functools import reduce
# mat = [[1,2],[3,4],[5]]
# ans = reduce(lambda x,y : x + y, mat) 
# print(ans)

# # 6. Filter strings by length  
# # Description: Return only those strings whose length is ≥ 5.  
# # Key concepts: filter with a lambda.  
# # Sample: words = ['cat', 'house', 'tree', 'elephant'] – ['house', 'elephant']
# words = ['cat', 'house', 'tree', 'elephant']
# ans = list(filter(lambda x: len(x) >= 5, words))
# print(ans)

# # 7. Find the longest string
# # Description: From a list of strings, return the longest one (first encountered on a tie).
# # Key concepts: reduce with a lambda, or max + key.
# # Sample: words = ['apple', 'banana', 'pear'] -> 'banana'
# from functools import reduce
# words = ['apple', 'banana', 'pear']
# ans = reduce(lambda x,y: x if len(x) > len(y) else y, words)
# print(ans)

# # --> whenever there comes word index, keep in mind that we can use enumerate
# # 8. Increment each element by its index  
# # Description: For a list of numbers, add the element’s index to its value.  
# # Key concepts: List comprehension with enumerate.  
# # Sample: nums = [10, 20, 30] _ [10, 21, 32] 
# nums = [10, 20, 30]
# ans = list(ele + idx for ele,idx in enumerate(nums))
# print(ans)

# #  --> good one
# # 9. Count vowels in each word  
# # Description: Produce a list of vowel counts corresponding to each input string.  
# # Key concepts: map with a lambda that uses a generator expression.  
# # Sample: words = ['apple', 'sky', 'aeiou'] _ [2, 0, 5]
# words = ['apple', 'sky', 'aeiou']
# ans = list(map(lambda x: sum(1 for ele in x if ele in "AEIOUaeiou"), words))
# print(ans)

# ---> not necessary to use lambda everytime ... also can use a dedicated function
# # 10. Filter prime numbers  
# # Description: Keep only the prime numbers from an integer list.  
# # Key concepts: filter + a helper lambda (or small helper function).  
# # Sample: nums = [1,2,3,4,5,6,7] - [2,3,5,7] 
# def is_prime(x):
#     for i in range (2,x):
#         if (x%i == 0):
#             return False
#         else:
#             return True
# nums = [1,2,3,4,5,6,7]
# ans = list(filter(is_prime, nums))
# print(ans)

# --> in map function we can also pass one or more lists simultaneously with adding argument in lambda
# ---> we can use zip to get things like enumerate
# 11. Pairwise sum of two equal-length lists  
# Description: Given two lists A and B of the same size, return a new list where each element is \( A[i] + B[i] \).  
# Key concepts: map with a lambda taking two arguments, or list comprehension with zip.  
# Sample: A=[1,2,3]; B=[4,5,6] - [5,7,9]
# # * * * * * * * * Approach 1 * * * * * * * * 
# A=[1,2,3]
# B=[4,5,6]
# ans = list(map(lambda x,y : x+y, A, B))
# print(ans)  
# # * * * * * * * * Approach 2 * * * * * * * * 
# ans2 =  list(ele1 + ele2 for ele1,ele2 in zip(A,B))
# print(ans2)

# # 12. Remove duplicates while preserving order  
# # Description: Return a list with duplicates removed, keeping the first occurrence of each element.  
# # Key concepts: reduce with a lambda that builds a result list, or list comprehension with a seen set.  
# # Sample: lst = [3,1,2,3,2,4] - [3,1,2,4]  
# lst = [3,1,2,3,2,4]
# # * * * * * * * * approach 1 --> using reduce * * * * * * * *
# from functools import reduce
# ans = reduce(lambda x, y: x + [y] if y not in x else x, lst, [])
# print(ans)
# # * * * * * * * * approach 2 --> using list comprehension * * * * * * * *
# seen = set()
# ans = list (x for x in lst if not (x in seen or seen.add(x)))
# print(ans)
 
# # 13. Convert a list of "key=value" strings to a dictionary  
# # Description: Each item is formatted like "name=John"; produce a dict (name: "John", ...).  
# # Key concepts: map with lambda to split; then dict (or comprehension).  
# # Sample: pairs = ['a=1', 'b=2'] - ['a':'1', 'b':'2']  
# pairs = ['a=1', 'b=2']
# ans = dict(map(lambda x: x.split('='), pairs))
# print(ans)

# # 14. Filter rows in a 2-D list by a column condition  
# # Description: For a matrix of integers, keep only rows where the third column > 10.  
# # Key concepts: filter with a lambda that indexes the sub-list.  
# # Sample: mat = [[1,2,5],[3,4,12],[7,8,9]] - [[3,4,12]]  
# mat = [[1,2,5],[3,4,12],[7,8,9]]
# print(list(filter(lambda x: x[2] > 10,mat)))

# # 15. Compute the sum of squares of odd numbers  
# # Description: From a numeric list, select odd numbers, square them, and sum the results.  
# # Key concepts: Combination of filter, map, and reduce (or a single comprehension + sum).  
# # Sample: nums = [1,2,3,4,5] - 35 (1+3+5+5)
# from functools import reduce
# nums = [1,2,3,4,5]
# print(reduce(lambda x,y : x+y,list(map(lambda x: x**2,list(filter(lambda x: x%2 != 0,nums))))))

# # --> [ expression for item in iterable if condition ] --> format for list comprehension
# # 16. Generate a multiplication table (2‑D list)
# # Description: Produce an n × n matrix where element [i][j] equals (i-1)*(j-1).
# # Key concepts: Nested list comprehension.
# # Sample: n = 3 → [[1,2,3],[2,4,6],[3,6,9]]
# # * * * * * * * * Normal way * * * * * * * * 
# n = 3
# ans = []
# for i in range (0,n):
#     row = [0]*3
#     for j in range (0,n):
#         row[j] = (i+1)*(j+1)
#     ans.append(row)
# print(ans)
# # * * * * * * * * by list comprehention * * * * * * * *
# ans = [[(i+1)*(j+1) for j in range (n)] for i in range (n)]
# print(ans) 

# # 17. Find the string with the most vowels
# # Description: Return the word that contains the highest number of vowels.
# # Key concepts: reduce with a lambda that counts vowels, or max + custom key.
# # Sample: words = ['boat', 'education', 'sky'] → 'education'
# # * * * * * * * * * * Approach 1 ---> reduce approach * * * * * * * * * * *
# words = ['boat', 'education', 'sky']
# from functools import reduce
# ans = reduce(lambda x,y: x if sum(1 for chr in x if chr in 'AEIOUaeiou') > sum(1 for chr in y if chr in 'AEIOUaeiou') else y, words )
# print(ans)
# # * * * * * * * * * * Approach 2 ---> max + key * * * * * * * * * * *
# words = ['boat', 'education', 'sky']
# ans = max(words,  key= lambda w: sum(1 for chr in w if chr in 'AEIOUaeiou'))
# print(ans)

# 18. Transform a list of timestamps (seconds) to time strings
# Description: Convert each integer representing seconds into a zero‑padded time string.
# Key concepts: map with a lambda using divmod.
# Sample: times = [3661, 45] → ['01:01:01', '00:00:45']

# # 19. Produce a list of cumulative sums (running total)
# # Description: For [a, b, c,...] generate [a, a+b, a+b+c,...].
# # Key concepts: reduce that returns an intermediate list (or itertools accumulate).
# # Sample: nums = [2,4,6] → [2,6,12]
# nums = [2,4,6]
# from functools import reduce
# ans = reduce(lambda x,y: ,nums)
# 20. Filter a mixed‑type list to keep only strings that start and end with the same letter
# Description: Input may contain ints, floats, and strings, return only the qualifying strings.
# Key concepts: filter with a lambda that checks type and string slicing.
# Sample: data = ['to', 'level', 'test', 'radar', 3.14] → ['level', 'radar']