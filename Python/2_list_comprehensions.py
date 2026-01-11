# # for only if --> we can write it after for loop
# # for if-else --> always write it before for loop 

# # Q8. for review

# # 1. creating list of squares of only even no gretaer than 10
# list1 = [3,7,10,15,18,21,22]
# print([ele*ele for ele in list1 if ele>10 and ele%2==0])

# # 2. pass if marks >=50 else fail
# list1 = [45,78,32,90,66]
# print(["pass" if ele >=50 else "Fail" for ele in list1 ])

# # 3. Flattened list of only odd no
# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# print([ele for row in list1 for ele in row if ele%2!=0])

# # 4. list of words with length greater than 5
# list1 = ["apple","banana","cherry","kiwi"]
# print([ele for ele in list1 if len(ele)>=5])

# # 5. remove duplicates with preserving order
# list1 = [1,2,3,2,4,1,5]
# seen = set()
# print([ele for ele in list1 if ele not in seen and not seen.add(ele)])

# # 6. dict comprehension
# list1 = [1,2,3,4,5]
# print({k:k*k for k in list1})

# # 7. filter dictionary such that only students with scores greater than 50
# scores = {"A":45, "B":82, "C":67, "D":30}
# print({k:v for k,v in scores.items() if v>=50})

# # 8. swap keys and values
# dict1 = {"A":45, "B":82, "C":67, "D":30, "B": 45}
# print({v: [k for k,val in dict1.items() if val == v] for v in set(dict1.values())})

# # 9. to count the digits 
# word = "Ashwin Mahajan"
# print({ch: word.count(ch) for ch in word if ch != ' '})

# # 10: reverse without using reverse() or slice
# list1 = [8,2,3]
# print([list1[i] for i in range(len(list1)-1,-1,-1)])

# rotate list by 2
list1 = [1,2,3,4,5]

def helper(lst, start, end):
    while(start<end):
        temp = lst[start]
        lst[start] = lst[end]
        lst[end] = temp
        start += 1
        end -= 1
    return lst

def move_to_right(lst,n):
    lst = helper(lst,0,len(lst)-1)
    lst = helper(lst,0,n-1)
    lst = helper(lst,n,len(lst)-1)
    return lst
print(move_to_right(list1,2))

"race car"