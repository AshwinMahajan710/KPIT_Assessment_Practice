import os

# # 1. opening the file in write mode and write something
# # once opened and written will remove alln previous content
# file = open("Text.txt",'w')
# file.write("Hello Ashwin How are you")
# file.close()

# # 2. opening the file in read mode and reading the content
# file = open("Text.txt",'r')
# print(file.read())
# file.close()

# # 3. opening the file in append mode and write something
# file = open("Text.txt",'a')
# file.write("Hello Ashwin I know you are well\n")
# file.close()

# # 4. reading using r+
# file = open("Text.txt",'r+')
# print(file.read())
# file.close()

# # 5. truncatcating the file
# file = open("Text.txt",'w+')
# print(file.read())

# # 6. opening to see if it exists already then the error will be thrown 
# file = open("Text.txt",'x') # --> will throw error as "Text.txt" is already present 


# # 7. wroting the lines in string using list of lines in string seperated by \n 
# # --> its nature of writelines to keep '\n' if want to remove it we can use .strip() function on each line
# list1 = ["Ashwin Is very great stude\nHello i think you are fine\nThank you dipak dada"]
# file = open("Text.txt",'a+')
# file.writelines(list1)
# file.seek(0)
# print(file.readlines())

# # 8. reading the file line by line
# file = open("Text.txt",'r+')
# print(file.readline())
# print("current location of pointer: ",file.tell())
# print(file.readline())
# print("current location of pointer: ",file.tell())

# # 9. Getting current working directory
# print(os.getcwd())

# for rename and remove using os
# os.rename("info.txt","data.txt")
# os.remove("data.txt")
