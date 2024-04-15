import random


# function without params
def print_hello_word():
    print(f"Hello \nword!!")
    pass


print_hello_word()
print_hello_word()
print_hello_word()
print_hello_word()


# function with params
def print_greeting(name: str):
    print(f"Hello, {name.upper()}")


print_greeting("Petro ")


# print_greeting(123)
# print_greeting(True)

# function with params and returns
def sum_two_nums(num1: int, num2: int):
    result = num1 + num2
    print(f"--------> {result}")
    return result


def increase_and_print_result(result: int):
    print(f"Increased result is = {result + 1}")


sum_two_nums(2, 3)

regular_result = sum_two_nums(4, 7)
print("###>", regular_result)
print(f"regular_result == {regular_result}")

increase_and_print_result(regular_result)


# function with return only

def generate_random_num():
    return random.randint(0, 1000000)


print(generate_random_num())


# functions with default params and overwriht

def print_worker_bonus(name: str, bonus: int = 3000):
    print(f"Worker {name.upper()} is going to get bonus of {bonus}")


print(print_worker_bonus("zopa"))
print(print_worker_bonus(bonus=400, name="crap"))

# functions with *args
names = ["crap", "zopa", "blyat", "zaebiz"]


def print_list_of_names(list_of_names: list):
    print(list_of_names)
    print(type(list_of_names))


def print_tuple_of_names(*list_of_names: str):
    print(list_of_names)
    print(type(list_of_names))

print_list_of_names(names)
print_tuple_of_names(names, "szuko")

# function with **kwargs

def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs.items())

print_kwargs(name="ZZZ", age=123, is_joking=True)



