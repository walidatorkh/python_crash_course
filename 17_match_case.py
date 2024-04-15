# value = "crap"
# print(type(value))
# value = 5
value = 5.5
# value = []
# print(type(value))
# value = True
# # print(type(value))
#
# if type(value) is str:
#     print("Value is string")
# elif type(value) is int or type(value) is float:
#     print("Value is number")
# elif type(value) is bool:
#     print("Value is bool")
# elif type(value) is list:
#     print("Value is list")
# elif type(value) is float:
#     print("Value is float")
# else:
#     print("Value is unknown")

match type(value):
    case __builtins__.str:
        print("Value is string")
    case __builtins__.int | __builtins__.float:
        print("Value is number")
    case __builtins__.bool:
        print("Value is bool")
    case __builtins__.list:
        print("Value is list")
    case _:
        print("Value is unknown")

if isinstance(value, str):
    print("Value is string")
elif isinstance(value, int):
    print("Value is int")
elif isinstance(value, bool):
    print("Value is bool")
elif isinstance(value, list):
    print("Value is list")
elif isinstance(value, float):
    print("Value is float")
else:
    print("Value is unknown")
