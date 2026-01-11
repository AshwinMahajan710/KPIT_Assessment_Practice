x = 10
def main():
    global x
    print(x)
    x = 20
    v = 10
    def init():
        print(v)
        def init2():
            v = 30
            print(v)
    init()
main()
print(x)