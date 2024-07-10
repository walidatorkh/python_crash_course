# def f(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return f(n - 1) + f(n - 2)
#
#
# def main():
#     n = int(input("Enter a number: "))
#     print(f"First {n} terms are:")
#
#     for i in range(n):
#         print(f(i))
#
#
# if __name__ == "__main__":
#     main()


def print_fibo(n):
    f = [0] * n
    f[0] = 0
    if n > 1:
        f[1] = 1

    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]

    for i in range(n):
        print(f[i])


def main():
    n = int(input("Enter a number: "))
    print(f"First {n} terms are:")
    print_fibo(n)


if __name__ == "__main__":
    main()
