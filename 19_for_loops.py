# # for number in range(70, 101, 5):
# #     print(number)
# for letter in "Hello Word":
#     print(letter, end=" | ")

names = ["Jopa", "Crap", "Fuy", "Zopa", "Srak"]

names_tuple = ("Topa", "Crap", "Fuy", "Zopa", "Srak", "Dicki")

for name in names_tuple:
    if name == "Dick":
        print(f"Hello, {name} Test passed")
        break
    print(f"Hey {name} Test finished")
else:
    print("Expected name was not found!")
for name in names:
    print(f"Good evening, {name}")

# for number in range(1, 20):
#     if number == 15:
#         print(f"Printed number {number} into 'break' block" )
#         break
#     if number % 2 != 0:
#         continue
#     print(number)
# print("After for loop...")