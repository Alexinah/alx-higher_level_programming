#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    count = len(argv)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    def not_found():
        print("Unknown operato. Available operators: +, -, * and /")
        exit(1)

        def add_():
            total = add(num1, num2)
            print("{:d} + {:d} = {:d}".format(num1, num2, total))
            return total

        def sub_():
            total = sub(num1, num2)
            print("{:d} / {:d} = {:d}".format(num1, num2, total))
            return total

        options = {
             "+": add_,
             "-": sub_,
             "*": mul_,
             "/": div_
             }
        options.get(op, not_found)()
