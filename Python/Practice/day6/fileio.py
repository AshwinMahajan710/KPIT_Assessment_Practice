# w -> write
# w+ -> write + read
# r -> read
# r+ -> read
# a -> 
# a+ -> append + read
# seek(0)

# open file
# import fileio

# opening and writing the file and reading it similarly
file = open("read.txt",'w+') 
file.write("Hello Ashwin How are you!")
file.seek(0)
print(file.readline())
file.seek(0,2) # 
file.write("Ashwin Mahajn")
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())

for line in file.readlines():
        print(line.rstrip("\n"))
