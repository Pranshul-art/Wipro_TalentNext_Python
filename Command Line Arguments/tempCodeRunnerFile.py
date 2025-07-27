import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("Sum:", num1 + num2)
    except ValueError:
        print("Please provide valid integer numbers")
