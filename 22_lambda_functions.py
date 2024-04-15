# def print_hello(name: str):
#     print(f"hello world! {name}!")
#
# print_hello("Zopa")
#
# lambda_print_function = lambda name: print(f"hello world! {name}")
# lambda_print_function("crap")
def sum_of_nums(num1: int, num2: int):
    return num1 + num2


print(sum_of_nums(2, 6))

lambda_sum_of_nums = lambda num1, num2: num1 + num2
print(lambda_sum_of_nums(10, 40))

original_list = [10, 20, 30, 40, 50]

# def filtering(elem: int):
#    return elem > 25
# filtered_result = list(filter(filtering, original_list))
filtered_result = list(filter(lambda elem: elem > 25, original_list))
print(filtered_result)
