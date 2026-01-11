# input using string and then convert in int after spliting
def read_ints_from_stdin():
    input_str: str = input("Enter string: ")
    int_strs = input_str.split(" ")
    try:
        int_strs = list(map(lambda x: int(x), int_strs))
    except ValueError as e:
        print("Invalid data parsed: ",e)

# input using string and then convert in int after spliting
def read_floats_from_stdin():
    input_str: str = input("Enter string: ")
    float_strs = input_str.split(" ")
    try:
        float_strs = list(map(lambda x: float(x), float_strs))
        print("List of floats is: ",float_strs)
    except ValueError as e:
        print("Invalid data parsed: ",e)


# read_ints_from_stdin()
read_floats_from_stdin()