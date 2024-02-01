#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
    a = argv[1]
    b = argv[3]
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    if argv[2] == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    if argv[2] == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    if argv[2] == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit (1)

