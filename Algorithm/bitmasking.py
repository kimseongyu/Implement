def main():

    operation = [["add", 1], ["toggle", 5], ["remove", 1]]
    bit = 0
    for i in operation:
        op, n = i
        if op == "add":
            bit = bit | (1 << n)
        elif op == "remove":
            bit = bit & ~(1 << n)
        elif op == "toggle":
            bit = bit ^ (1 << n)
        elif op == "full":
            bit = (1 << 10) - 1
        elif op == "empty":
            bit = 0
        elif op == "check":
            print((bit >> n) & 1)

if __name__ == "__main__":
    main()