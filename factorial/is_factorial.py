def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Example of usage
# try:
#     num = int(input("Enter a positive integer: "))
#     if num < 0:
#         print("Invalid input. Please enter a non-negative integer. ")
#
#     else:
#         result = factorial(num)
#         print(f"The factorial of {num} is {result}.")
# except ValueError:
#     print("Wrong input. Enter a positive integer.")
def main():
    num = int(input("Enter a positive integer: "))
    if num < 0:
        num = int(input("Invalid input. Please enter a non-negative integer: "))
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")