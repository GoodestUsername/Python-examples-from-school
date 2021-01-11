import math


def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def handle_operator_selection(operator, a, b):
    if operator == 1:
        return calculate_hypotenuse(a, b)
    if operator == 2:
        return a + b
    if operator == 3:
        return a - b
    if operator == 4:
        return a * b
    if operator == 5:
        return a / b


def main():
    print("1 to calculate hypotenuse\n"
          "2 to add\n"
          "3 to subtract"
          "4 to multiply"
          "5 to divide")

    operator = int(input("Enter operator: "))

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(handle_operator_selection(operator, a, b))


if __name__ == "__main__":
    main()
