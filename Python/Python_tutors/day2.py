# # function
# def calLength(string1: str):
#     if isinstance(string1, str):
#         return len(string1)
    
# print(calLength("KPIT")) # 4
# print(calLength(10.5)) # None

# # calculate reverse of no using function
# def calReverse(no: int) -> int:
#     return int(str(no)[::-1])

# # calculate reverse by val
# def calReverseVal(no : int) -> int:
#     newNo = 0
#     while(no!=0):
#         temp = no%10
#         newNo = (newNo*10) + temp
#         no = no//10
#     return newNo 

# print( calReverse(125))
# print(calReverseVal(125))

# keyword arguments
def keywordCheck(personname, nickname, age):
    print("personname: ",personname, "nickname: ",nickname, "age: ",age)

keywordCheck(personname="Ashwin",nickname="Mahajan", age=123)

# local and global func
cotactPesron = "Ashwin"
def changePerson():
    cotactPesron = "Hello"
    def changePart2():
        nonlocal cotactPesron
        cotactPesron = "Dnuanesj"
print(cotactPesron)

# // args and kwars
def arguments(*args):
    print (args)

def kwargs(**args):
    print(args)

arguments(1,2,3,4,5,6,7)
kwargs(a="h", b="89")

# working with dictionarys
d1 = {1:89, 2:78, 5:78, 3:55, 2:99, 6:90}
print(d1)
print(d1.values())
print(d1.keys())
print(tuple(d1.values()))
print(set(d1.values()))

# creating list of dictionaries
vehicles = [
    {"make":"Toyota","Model":"Fortuner","year": 2020},
    {"make":"Toyota","Model":"Camry","year": 2021},
    {"make":"Toyota","Model":"hilux","year": 2022},
    {"make":"BMW","Model":"M5","year": 2013}
    ]

# 1. get all dict
def get_all_vehicle():
    return vehicles

def filter_vehicle(make):
    return [v for v in vehicles if v['make'] == make]

