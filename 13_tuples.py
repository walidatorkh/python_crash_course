my_tuple = (1, 2, 3, 3, 4, 1, 5)
my_list = [3, 5, 6, 8, 78, 34]
print(my_tuple)
print(id(my_tuple))
print(my_tuple.count(3))
print(my_tuple[2])
list_from_tuple = list(my_tuple)
print(list_from_tuple)
list_from_tuple[-1] = 47
print(list_from_tuple)
my_tuple = tuple(list_from_tuple)
print(my_tuple)
print(id(my_tuple))
