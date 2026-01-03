import re

text = "In 2025, Alex_T went to Room-42 at 10:30 AM to check sensor-data, but he noticed something strange! The device ID was 'A9B-77?' and the system displayed errors like E1, E12, and E123. Later, he wrote notes such as: temp=29C, humidity=70%, and status=OK. However, after 5 minutes, the sensor stopped responding... again! .error " 

# # 1. extracting using .  
# # op = r"." #--> list of all seperate characters
# op = r"e.r" # --> anything where this pattern followed
# result = re.findall(op,text)
# print(result)

# # 2. extracting using ? --> not a standalone like '.'
# op = r"a?nd" # --> 0 or 1 --> means first finds right side.... if it starts with left side then print with it or else print only right side --> ex. above output ---> ['and', 'and', 'and', 'nd'] --> in short ('a' is optional)
# result = re.findall(op,text)
# print(result)

# # 3. extracting using + --> not a standalone like '.'
# op = r"p+" # --> starts and with more occurances of same letter --> ex. ['p', 'p', 'pp', 'p']
# result = re.findall(op,text)
# print(result)

# # 4. extracting using * --> not a standalone like '.'
# op = r"di*" # --> 0 or more occurances of patter to left
# result = re.findall(op,text)
# print(result)

# # 5. extracting using '\w' --> for all alphanumeric values
# op = r"\w\wa" # --> general use case for ends with or start with kind of operations
# result = re.findall(op,text)
# print(result)

# # 6. extracting using '\W' --> for all non-alphanumeric values
# op = r"\Wa" # --> general use case for ends with or start with kind of operations
# result = re.findall(op,text)
# print(result)

# # 7. 8. Same with \d and \D like operations

# # [...] for any charater inside 

# # [^...] for any character which is not inside

