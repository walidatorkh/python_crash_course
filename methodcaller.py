from operator import methodcaller
from timeit import repeat

# List of names
names: list[str] = ['Bob', 'Jonny', 'Billy', 'Sandra', 'Blake', 'Jopa']

# Creating a method caller that checks if a string starts with 'B'
starts_with_a: methodcaller = methodcaller('startswith', 'B')

# Filtering the list of names using the method caller
filtered: filter = filter(starts_with_a, names)
print(list(filtered))  # Printing the filtered list of names starting with 'B'


# Creating a method caller that counts the occurrences of an empty string
count_a: methodcaller = methodcaller('count', '')

# Sorting the list of names based on the count of empty strings (no effect as all counts are 0)
print('Sorted: ', list(sorted(names, key=count_a)))
print('Sorted reverse=True: ', list(sorted(names, key=count_a, reverse=True)))

# Warm-up code to prepare for timing tests
warm_up: str = '''
for i in range(3):
    ...
'''

# Test code for method caller approach
method_caller_test: str = '''
filter(starts_with_a, names)
'''

# Test code for lambda function approach
lambda_test: str = '''
filter(lambda x: x.startswith('B'), names)
'''

# Measuring the time for warm-up, method caller, and lambda function approaches
warm_up_time: float = min(repeat(stmt=warm_up))
method_caller_time: float = min(repeat(method_caller_test, globals=globals()))
lambda_time: float = min(repeat(lambda_test, globals=globals()))

# Printing the time taken by method caller and lambda function approaches
print(f'{method_caller_time=:.3f}')  # Printing method caller execution time
print(f'{lambda_time=:.3f}')  # Printing lambda function execution time
