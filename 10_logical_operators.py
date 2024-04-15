# not / or / and / not


# print(f"not True -> {not True}")
# print(f"not False -> {not False}")
# print(not 5 == 5)
#
#
# print(f"True or True -> {True or True}")
# print(f"True or False -> {True or False}")
# print(f"False or True -> {False or True}")
# print(f"False or False -> {False or False}")
# print(f"True or (False or False) -> {True or (False or False)}")
#
# num_1 = 5
# num_2 = 10
#
# if num_1 == 5 or num_2 == 10:
#     print("as expected")
# else:
#     print("not as expected")


# print(f"True and True -> {True and True}")
# print(f"True and False -> {True and False}")
# print(f"False and True -> {False and True}")
# print(f"False and False -> {False and False}")
# print(f"True and (False and False) -> {True and (False and False)}")
#
# num_1 = 3
# num_2 = 10
#
# if num_1 == 5 and num_2 == 10:
#     print("as expected")
# else:
#     print("not as expected")

# numbers = int(input("Enter a number: "))
#
# if numbers >= 0 and numbers <= 20:
#     print("in range of 0 - 20")
# elif numbers > 20 and numbers <= 50:
#     print("range between 20 - 50")
# elif 50 < numbers<= 100:
#     print("range between 50 - 100")
# else:
#     print("n valid numbers entered")

input_username = input("Input your user name: ")
input_password = input("Input your password: ")

correct_username = "vasya"
correct_password = "123"

if input_username == correct_username and input_password == correct_password:
    print(f"Welcome {correct_username} to the system ")
else:
    print("some entered credentials is wrong!!!")

