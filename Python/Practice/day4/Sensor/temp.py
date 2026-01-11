n = int(input())
keys = input().split(" ")
dict1 = {}
for i in range(n):
    vals = input().split(" ")
    if vals == [""]:
        dict1[keys[i]] = []
    else:
        vals = list(map(float,vals))
        dict1[keys[i]] = vals
print(dict1)