from Lab.Lab0.hypotenuse import calculate_hypotenuse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def handle_operator_selection(operator, a, b):
    if operator in (1, 2, 3, 4, 5):
        if operator == 1:
            return calculate_hypotenuse(a, b)

        if operator == 2:
            return add(a, b)

        if operator == 3:
            return subtract(a, b)

        if operator == 4:
            return multiply(a, b)

        if operator == 5:
            return divide(a, b)
    else:
        print("Invalid operator")


def main():
    print("1 to calculate hypotenuse\n"
          "2 to add\n"
          "3 to subtract\n"
          "4 to multiply\n"
          "5 to divide\n")

    operator = int(input("Enter operator: "))

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(handle_operator_selection(operator, a, b))


if __name__ == "__main__":
    main()
