import math


def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def main():
    print("This program calculates a hypotenuse given two values.")
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    print("The hypotenuse is %d" % calculate_hypotenuse(a, b))


if __name__ == "__main__":
    main()
